import streamlit as st
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(
    page_title="CSV Data Quality Assistant",
    page_icon="📊",
    layout="wide"
)

# Title and description
st.title("📊 CSV Data Quality Assistant")
st.markdown("Upload your CSV file to analyze data quality and get cleaning suggestions.")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type=['csv'])

if uploaded_file is not None:
    try:
        # Read the CSV file
        df = pd.read_csv(uploaded_file)
        
        # Success message
        st.success("✅ File uploaded successfully!")
        
        # Create tabs for better organization
        tab1, tab2, tab3, tab4 = st.tabs(["📋 Overview", "🔍 Data Quality", "📊 Statistics", "💡 Suggestions"])
        
        # TAB 1: OVERVIEW
        with tab1:
            st.header("Data Preview")
            st.markdown("**First 10 rows of your dataset:**")
            st.dataframe(df.head(10), use_container_width=True)
            
            st.header("Dataset Dimensions")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Rows", f"{len(df):,}")
            with col2:
                st.metric("Total Columns", len(df.columns))
            with col3:
                duplicates = df.duplicated().sum()
                st.metric("Duplicate Rows", duplicates)
        
        # TAB 2: DATA QUALITY
        with tab2:
            st.header("Missing Values Analysis")
            
            # Calculate missing values
            missing_data = pd.DataFrame({
                'Column': df.columns,
                'Missing Count': df.isnull().sum().values,
                'Missing Percentage': (df.isnull().sum().values / len(df) * 100).round(2)
            })
            
            # Filter to show only columns with missing values
            missing_data_filtered = missing_data[missing_data['Missing Count'] > 0]
            
            if len(missing_data_filtered) > 0:
                st.warning(f"⚠️ Found missing values in {len(missing_data_filtered)} column(s)")
                st.dataframe(missing_data_filtered, use_container_width=True, hide_index=True)
            else:
                st.success("✅ No missing values found!")
            
            st.header("Data Types")
            dtype_df = pd.DataFrame({
                'Column': df.columns,
                'Data Type': df.dtypes.values.astype(str),
                'Non-Null Count': df.count().values,
                'Unique Values': [df[col].nunique() for col in df.columns]
            })
            st.dataframe(dtype_df, use_container_width=True, hide_index=True)
        
        # TAB 3: STATISTICS
        with tab3:
            st.header("Summary Statistics")
            
            # Get numeric columns
            numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
            
            if len(numeric_cols) > 0:
                st.markdown(f"**Statistics for {len(numeric_cols)} numeric column(s):**")
                st.dataframe(df[numeric_cols].describe(), use_container_width=True)
                
                # Additional statistics
                st.subheader("Additional Numeric Insights")
                stats_df = pd.DataFrame({
                    'Column': numeric_cols,
                    'Mean': [df[col].mean() for col in numeric_cols],
                    'Median': [df[col].median() for col in numeric_cols],
                    'Std Dev': [df[col].std() for col in numeric_cols],
                    'Min': [df[col].min() for col in numeric_cols],
                    'Max': [df[col].max() for col in numeric_cols]
                })
                st.dataframe(stats_df.round(2), use_container_width=True, hide_index=True)
            else:
                st.info("ℹ️ No numeric columns found in the dataset.")
            
            # Categorical columns summary
            categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
            if len(categorical_cols) > 0:
                st.subheader("Categorical Columns Summary")
                cat_df = pd.DataFrame({
                    'Column': categorical_cols,
                    'Unique Values': [df[col].nunique() for col in categorical_cols],
                    'Most Common': [df[col].mode()[0] if len(df[col].mode()) > 0 else 'N/A' for col in categorical_cols],
                    'Most Common Count': [df[col].value_counts().iloc[0] if len(df[col]) > 0 else 0 for col in categorical_cols]
                })
                st.dataframe(cat_df, use_container_width=True, hide_index=True)
        
        # TAB 4: SUGGESTIONS
        with tab4:
            st.header("Data Cleaning Suggestions")
            
            suggestions = []
            
            # Check for duplicate rows
            if duplicates > 0:
                suggestions.append({
                    'Issue': 'Duplicate Rows',
                    'Count': duplicates,
                    'Suggestion': f'Remove {duplicates} duplicate row(s) to avoid data redundancy.',
                    'Priority': '🔴 High'
                })
            
            # Check for missing values
            for _, row in missing_data_filtered.iterrows():
                if row['Missing Percentage'] > 50:
                    suggestions.append({
                        'Issue': f"High Missing Values in '{row['Column']}'",
                        'Count': f"{row['Missing Percentage']:.1f}%",
                        'Suggestion': f"Consider removing this column as it has more than 50% missing values.",
                        'Priority': '🔴 High'
                    })
                elif row['Missing Percentage'] > 20:
                    suggestions.append({
                        'Issue': f"Missing Values in '{row['Column']}'",
                        'Count': f"{row['Missing Percentage']:.1f}%",
                        'Suggestion': f"Consider filling missing values with mean/median (numeric) or mode (categorical).",
                        'Priority': '🟡 Medium'
                    })
                else:
                    suggestions.append({
                        'Issue': f"Few Missing Values in '{row['Column']}'",
                        'Count': f"{row['Missing Percentage']:.1f}%",
                        'Suggestion': f"Drop rows with missing values or fill with appropriate method.",
                        'Priority': '🟢 Low'
                    })
            
            # Check for potential data type conversions
            for col in df.columns:
                if df[col].dtype == 'object':
                    # Check if column contains numeric values stored as strings
                    try:
                        pd.to_numeric(df[col].dropna())
                        suggestions.append({
                            'Issue': f"Data Type Issue in '{col}'",
                            'Count': 'All rows',
                            'Suggestion': f"Column appears to contain numeric values but is stored as text. Consider converting to numeric type.",
                            'Priority': '🟡 Medium'
                        })
                    except:
                        pass
            
            # Check for columns with single unique value
            for col in df.columns:
                if df[col].nunique() == 1:
                    suggestions.append({
                        'Issue': f"Constant Column '{col}'",
                        'Count': '1 unique value',
                        'Suggestion': f"This column has only one unique value and may not be useful for analysis. Consider removing it.",
                        'Priority': '🟡 Medium'
                    })
            
            # Display suggestions
            if len(suggestions) > 0:
                st.warning(f"⚠️ Found {len(suggestions)} data quality issue(s)")
                
                # Convert to DataFrame for better display
                suggestions_df = pd.DataFrame(suggestions)
                
                # Sort by priority
                priority_order = {'🔴 High': 0, '🟡 Medium': 1, '🟢 Low': 2}
                suggestions_df['sort_key'] = suggestions_df['Priority'].map(lambda x: priority_order.get(x, 999))
                suggestions_df = suggestions_df.sort_values('sort_key').drop('sort_key', axis=1)
                
                st.dataframe(suggestions_df, use_container_width=True, hide_index=True)
                
                # Summary by priority
                st.subheader("Summary by Priority")
                col1, col2, col3 = st.columns(3)
                with col1:
                    high_priority = len([s for s in suggestions if s['Priority'] == '🔴 High'])
                    st.metric("High Priority", high_priority)
                with col2:
                    medium_priority = len([s for s in suggestions if s['Priority'] == '🟡 Medium'])
                    st.metric("Medium Priority", medium_priority)
                with col3:
                    low_priority = len([s for s in suggestions if s['Priority'] == '🟢 Low'])
                    st.metric("Low Priority", low_priority)
            else:
                st.success("✅ No data quality issues found! Your dataset looks clean.")
            
            # General recommendations
            st.subheader("General Recommendations")
            st.markdown("""
            - **Backup your data** before making any changes
            - **Handle missing values** based on your analysis requirements
            - **Remove duplicates** if they don't represent valid data
            - **Validate data types** to ensure correct analysis
            - **Check for outliers** in numeric columns using the statistics tab
            - **Document your cleaning steps** for reproducibility
            """)
    
    except Exception as e:
        st.error(f"❌ Error reading file: {str(e)}")
        st.info("Please make sure your file is a valid CSV format.")

else:
    # Instructions when no file is uploaded
    st.info("👆 Please upload a CSV file to begin analysis")
    
    st.markdown("### What this app does:")
    st.markdown("""
    - ✅ Display first 10 rows of your data
    - ✅ Show dataset dimensions (rows and columns)
    - ✅ Analyze missing values with counts and percentages
    - ✅ Detect duplicate rows
    - ✅ Display data types for each column
    - ✅ Generate summary statistics for numeric columns
    - ✅ Provide intelligent cleaning suggestions
    """)
    
    st.markdown("### How to use:")
    st.markdown("""
    1. Click the 'Browse files' button above
    2. Select your CSV file
    3. Explore the different tabs to analyze your data
    4. Review the cleaning suggestions
    """)

# Made with Bob

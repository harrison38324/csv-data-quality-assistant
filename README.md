# CSV Data Quality Assistant 📊

> A Streamlit-powered web application for automated CSV data quality analysis and cleaning recommendations - Built for the jtopreport hackathon with IBM Bob

## 🎯 Project Overview

The CSV Data Quality Assistant is an intuitive web application designed to democratize data quality analysis. It empowers users of all skill levels to quickly identify and address data quality issues in their CSV files without requiring programming knowledge or expensive data quality tools.

## 🚨 Problem Statement

Data quality is a critical challenge in data science and analytics:

- **Manual inspection is time-consuming**: Reviewing large datasets row-by-row is impractical
- **Hidden issues**: Missing values, duplicates, and type mismatches often go unnoticed
- **Lack of expertise**: Not everyone knows what to look for or how to fix data problems
- **No standardized approach**: Teams lack consistent methods for data quality assessment
- **Expensive tools**: Enterprise data quality solutions are costly and complex

**Our Solution**: A free, open-source, beginner-friendly tool that automatically analyzes CSV files and provides actionable cleaning recommendations with priority levels.

## ✨ Features

### 📋 Data Overview
- **Preview Display**: View the first 10 rows of your dataset
- **Dimension Metrics**: Total rows, columns, and duplicate count at a glance
- **Quick Assessment**: Instant understanding of dataset structure

### 🔍 Data Quality Analysis
- **Missing Values Detection**: Identifies empty cells with counts and percentages
- **Data Type Validation**: Shows data types and unique value counts for each column
- **Duplicate Detection**: Finds and counts duplicate rows
- **Type Mismatch Detection**: Identifies numeric data stored as text

### 📊 Statistical Insights
- **Numeric Statistics**: Mean, median, standard deviation, min/max, quartiles
- **Categorical Analysis**: Unique value counts and most common entries
- **Distribution Overview**: Comprehensive statistical summaries

### 💡 Intelligent Suggestions
- **Prioritized Recommendations**: Color-coded by severity (🔴 High, 🟡 Medium, 🟢 Low)
- **Actionable Advice**: Specific steps to address each issue
- **Smart Detection**: Identifies constant columns, high missing percentages, and data type issues
- **Summary Dashboard**: Quick overview of issues by priority level

## 🤖 How IBM Bob Accelerated Development

IBM Bob was instrumental in rapidly developing this hackathon project:

### 1. **Rapid Prototyping**
- Bob helped structure the initial Streamlit application layout
- Generated boilerplate code for file upload and data processing
- Suggested optimal tab organization for user experience

### 2. **Code Quality & Best Practices**
- Recommended pandas best practices for efficient data analysis
- Suggested error handling patterns for robust file processing
- Helped implement clean, readable code structure

### 3. **Feature Implementation**
- Assisted in creating the intelligent suggestion algorithm
- Helped design the priority-based recommendation system
- Provided guidance on statistical calculations and data type detection

### 4. **Documentation**
- Generated comprehensive inline comments
- Helped create user-friendly instructions
- Assisted in writing this README

### 5. **Debugging & Optimization**
- Identified potential edge cases in data processing
- Suggested performance optimizations for large datasets
- Helped troubleshoot Streamlit-specific issues

**Time Saved**: What would typically take 2-3 days of development was completed in a few hours with Bob's assistance, allowing more time for testing and refinement.

## 🚀 How to Run Locally

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Installation Steps

1. **Clone or download this repository**
```bash
git clone <repository-url>
cd csv-data-quality-assistant
```

2. **Create a virtual environment (recommended)**
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
streamlit run app.py
```

5. **Open in browser**
- The app should automatically open at `http://localhost:8501`
- If not, manually navigate to that URL in your browser

### Using the App

1. Click "Browse files" to upload your CSV file
2. Explore the four tabs:
   - **Overview**: See your data preview and basic metrics
   - **Data Quality**: Analyze missing values and data types
   - **Statistics**: Review statistical summaries
   - **Suggestions**: Get prioritized cleaning recommendations
3. Follow the suggestions to improve your data quality

## 📁 Project Structure

```
csv-data-quality-assistant/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── README.md          # This file
├── .venv/             # Virtual environment (created locally)
└── sample_data/       # Sample CSV files for testing
```

## 🔮 Future Improvements

### Short-term Enhancements
- [ ] **Export Functionality**: Download cleaned data and quality reports as CSV/PDF
- [ ] **Data Visualization**: Add charts for missing value patterns and distributions
- [ ] **Batch Processing**: Analyze multiple CSV files simultaneously
- [ ] **Custom Thresholds**: Allow users to set their own priority thresholds

### Medium-term Features
- [ ] **Automated Cleaning**: One-click data cleaning based on suggestions
- [ ] **Data Profiling**: More advanced statistical analysis and outlier detection
- [ ] **Column Recommendations**: Suggest data type conversions with preview
- [ ] **Comparison Mode**: Compare data quality across multiple datasets
- [ ] **History Tracking**: Save and compare quality reports over time

### Long-term Vision
- [ ] **Machine Learning Integration**: Predict optimal cleaning strategies
- [ ] **API Development**: RESTful API for programmatic access
- [ ] **Database Support**: Extend beyond CSV to SQL databases and Excel files
- [ ] **Collaborative Features**: Team-based data quality workflows
- [ ] **Integration Plugins**: Connect with popular data tools (Jupyter, Power BI, Tableau)
- [ ] **Real-time Monitoring**: Continuous data quality monitoring for data pipelines

## 🛠️ Technologies Used

- **Streamlit 1.32.0**: Web application framework
- **Pandas 2.2.1**: Data manipulation and analysis
- **NumPy 1.26.4**: Numerical computing

## 📊 Use Cases

- **Data Scientists**: Quick data quality checks before analysis
- **Business Analysts**: Validate data before creating reports
- **Students**: Learn about data quality concepts
- **Small Businesses**: Affordable data quality solution
- **Data Engineers**: Pre-processing validation

## 🤝 Contributing

This is a hackathon project, but contributions are welcome! Feel free to:
- Report bugs or issues
- Suggest new features
- Submit pull requests
- Improve documentation

## 📄 License

Open source - free to use and modify for any purpose.

## 🙏 Acknowledgments

- Built for the **jtopreport hackathon**
- Developed with assistance from **IBM Bob**
- Inspired by the need for accessible data quality tools

---

**Made with ❤️ and IBM Bob** | [Report Issues](../../issues) | [Suggest Features](../../issues/new)
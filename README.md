# CSV Data Quality Assistant 📊

A simple and beginner-friendly Streamlit app for checking CSV data quality, built for the jtopreport hackathon project.

## Features

✅ **Data Preview** - View the first 10 rows of your dataset  
✅ **Dataset Dimensions** - See total rows, columns, and duplicate count  
✅ **Missing Values Analysis** - Identify missing data with counts and percentages  
✅ **Data Types** - View data types and unique value counts for each column  
✅ **Summary Statistics** - Get statistical summaries for numeric columns  
✅ **Cleaning Suggestions** - Receive intelligent recommendations for data cleaning  

## Installation

1. Clone this repository or download the files
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit app:

```bash
streamlit run app.py
```

2. Open your browser (it should open automatically) to `http://localhost:8501`

3. Upload your CSV file using the file uploader

4. Explore the four tabs:
   - **Overview**: Preview data and see basic dimensions
   - **Data Quality**: Analyze missing values and data types
   - **Statistics**: View summary statistics for numeric and categorical columns
   - **Suggestions**: Get prioritized cleaning recommendations

## What the App Checks

### Data Quality Issues
- Missing values (with percentage calculations)
- Duplicate rows
- Incorrect data types (e.g., numbers stored as text)
- Constant columns (single unique value)
- High percentage of missing data (>50%)

### Statistics Provided
- Mean, median, standard deviation
- Min and max values
- Quartiles (25%, 50%, 75%)
- Unique value counts
- Most common values for categorical data

### Cleaning Suggestions
The app provides prioritized suggestions:
- 🔴 **High Priority**: Critical issues like duplicates or columns with >50% missing data
- 🟡 **Medium Priority**: Data type issues or moderate missing values (20-50%)
- 🟢 **Low Priority**: Minor issues like small amounts of missing data (<20%)

## Example Workflow

1. Upload your CSV file
2. Check the **Overview** tab to understand your data structure
3. Review the **Data Quality** tab to identify issues
4. Examine **Statistics** to understand your numeric data
5. Follow the **Suggestions** tab to clean your data

## Requirements

- Python 3.7+
- streamlit 1.32.0
- pandas 2.2.1
- numpy 1.26.4

## Tips for Beginners

- Always backup your original data before cleaning
- Start with high-priority suggestions first
- Use the statistics to identify outliers
- Document your cleaning steps for reproducibility

## Project Structure

```
csv-data-quality-assistant/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Contributing

This is a hackathon project. Feel free to fork and improve!

## License

Open source - feel free to use and modify as needed.

---

Built with ❤️ for the jtopreport hackathon
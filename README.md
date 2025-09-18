# Data Parser


A Python solution for parsing JSON grant submission data into structured CSV format for analysis and decision-making in grant management workflows.

## Overview

This solution processes grant submission data from foundations and grantmakers, extracting key information from nested JSON structures and converting it into a flat CSV format suitable for analysis, reporting, and decision-making processes.

## Features

- **JSON to CSV Conversion**: Transforms complex nested JSON data into structured CSV format
- **Data Extraction**: Extracts key fields including organization details, grant information, and workflow status
- **Date Formatting**: Converts ISO date formats to readable MM/DD/YY format
- **Error Handling**: Gracefully handles missing or malformed data
- **Type Safety**: Full type annotations for maintainability and clarity

## Data Mapping

The parser extracts the following fields from the JSON submissions:

| CSV Column | JSON Source | Description |
|------------|-------------|-------------|
| Organization Legal Name | `nonprofit.legalName` | Legal name of the applying organization |
| Grant Submission Name | `name` | Title of the grant submission |
| Stage | `stage` | Current stage in the grant workflow |
| Requested Amount | `grantAmount.minAmount` | Minimum requested grant amount |
| Awarded Amount | `awardedAmount` | Amount awarded (if any) |
| Grant Type | `grantType` | Type of grant (e.g., OPERATING_GRANT) |
| Tags | `tags` | Comma-separated list of grant tags |
| Pipeline/Workflow Associated | `pipelineInfo.name` | Associated workflow pipeline name |
| Duration Start | `duration.start` | Grant period start date |
| Duration End | `duration.end` | Grant period end date |
| Grant Submission Id | `id` | Unique submission identifier |

## Usage

```bash
python solution.py
```

The script will:
1. Read data from `submissions.json`
2. Process all submission records
3. Generate `submission_output.csv` with the parsed data
4. Display processing statistics and sample data

## Requirements

- Python 3.7+
- No external dependencies (uses only standard library)

## File Structure

```
├── solution.py              # Main parser implementation
├── submissions.json         # Input data file
├── submission_output.csv    # Generated output file
└── README.md               # This file
```

## Implementation Details

The solution uses a class-based approach with clear separation of concerns:

- **Data Loading**: Reads and parses JSON data
- **Field Extraction**: Extracts specific fields with appropriate fallbacks
- **Data Transformation**: Formats dates and handles data type conversions
- **CSV Generation**: Writes structured data to CSV format

## Error Handling

The parser includes robust error handling for:
- Missing or null values in JSON data
- Malformed date strings
- Invalid data types
- File I/O operations

Missing data is handled gracefully with empty string fallbacks, ensuring the CSV output remains consistent and usable.

## Output Format

The generated CSV file includes a header row followed by data rows, with each submission represented as a single row. All data is properly escaped for CSV format, and dates are formatted consistently for readability.

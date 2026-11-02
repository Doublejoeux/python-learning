# Excel Sales Report Generator

A script that reads a sales spreadsheet, cleans it and produces a formatted
Excel report with a summary sheet.

## Features
- Reads an Excel file with pandas.
- Fills missing prices using the median price of the same product.
- Removes rows with missing Units and reports how many were removed.
- Calculates revenue per row, total revenue and revenue per region and product.
- Identifies the best seller by revenue and by units sold.
- Writes a four-sheet report: Summary, Clean Data, By Region, By Product.
- Formats the report: styled headers, auto-sized columns, aligned values,
  thousands separators on total revenue with two decimal places.

## How it works
- Functions: 
    -   `load_data` reads the Excel file.
    -   `clean_data` fills missing prices and drops rows with missing Units.
    -   `summarize` builds the summary table and the region/product totals.
    -   `write_report` writes everything to a temporary file.
    -   `format_report` formats the temporary file and saves it as the final report.
    -   `run_report` runs the steps in order and catches any error.

- Missing prices are filled (a product's price is a stable attribute) but
  missing units are excluded (filling them would invent sales that never
  happened). The number of excluded rows is shown on the Summary sheet.

- The report is written to a temporary file first and only saved under its
  final name after formatting succeeds, so a failed run never leaves a
  broken report that looks finished or overwrites yesterday's good one.

- If the "Total revenue" label is not found during formatting, the script
  raises an error instead of silently skipping it because a changed label
  could mean the report is no longer what it claims to be. The temp file is
  kept on purpose, so the problem can be inspected.

## What I learned
- openpyxl edits the file itself (styles, widths) while pandas works on the data.
- Most pandas methods return a new DataFrame instead of changing the old one.
- Functions should take settings (CONSTANTS) as parameters and return only what the
  next step needs.

## How to run it
1. Install the dependencies: `pip install pandas openpyxl`
2. Run `sample_spreadsheet_data.py` to get `sales_data.xlsx`
3. Run `python excel_report.py`
4. Open `sales_report.xlsx`

## Possible improvements
- Schedule it with the `schedule` library
- Log failures to a file instead of printing them
- Take the input filename from the command line
- Add a chart to the Summary sheet
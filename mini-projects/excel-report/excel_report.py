from openpyxl import load_workbook
import pandas as pd
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter
import os
FILENAME = "sales_data.xlsx"
TOTAL_REVENUE = "Total revenue"
TEMP_REPORT = "sales_report_temp.xlsx"
REPORT = "sales_report.xlsx"

def load_data(filename):
    df = pd.read_excel(filename)
    return df

def clean_data(df):
    df = df.copy()
    df["Price"] = df["Price"].fillna(df.groupby("Product")["Price"].transform("median"))
    new_df = df.dropna(subset=["Units"]).copy()

    rows_before = len(df)
    rows_after = len(new_df)
    rows_dropped = rows_before - rows_after

    new_df["Revenue"] = new_df["Units"] * new_df["Price"]

    return new_df, rows_before, rows_dropped

def summarize(new_df, rows_before, rows_dropped, total_revenue):
    
    regions_totals = new_df.groupby("Region")["Revenue"].sum()
    
    products_totals = new_df.groupby("Product")["Revenue"].sum()
    best_seller_revenue = products_totals.idxmax()
    
    products_totals2 = new_df.groupby("Product")["Units"].sum()
    best_seller_units = products_totals2.idxmax()
    
    revenue_total = new_df['Revenue'].sum()

    summary_df = pd.DataFrame(
        [("Rows in original file", rows_before),
        ("Rows excluded (Missing Units)", rows_dropped),
        (total_revenue, revenue_total),
        ("Best seller by revenue", best_seller_revenue),
        ("Best seller by units", best_seller_units)
        ],
        columns=["Metric", "Value"]
    )

    return summary_df, regions_totals, products_totals

def write_report(summary_df, new_df, regions_totals, products_totals, temp_report):
    with pd.ExcelWriter(temp_report) as writer:
        summary_df.to_excel(writer, sheet_name="Summary", index=False)
        new_df.to_excel(writer, sheet_name="Clean Data", index= False)
        regions_totals.to_excel(writer, sheet_name="By Region")
        products_totals.to_excel(writer, sheet_name="By Product")

def format_report(report, total_revenue, temp_report):
    wb = load_workbook(temp_report)
    for ws in wb.worksheets:
        for cell in ws[1]:
            cell.font = Font(bold=True, color="FFFFFF")
            cell.fill = PatternFill(start_color="305496", end_color="305496", fill_type="solid")

        for column_cells in ws.columns:
            longest = max((len(str(cell.value)) for cell in column_cells if cell.value is not None), default=0)
            letter = get_column_letter(column_cells[0].column)
            ws.column_dimensions[letter].width = longest + 2  
    summary_ws = wb["Summary"]
    found = False
    for label_cell, value_cell in summary_ws.iter_rows(min_row=2,max_col=2):
        if label_cell.value == total_revenue:
            value_cell.number_format = "#,##0.00"
            found = True
        for cell in (label_cell, value_cell):
            cell.alignment = Alignment(horizontal="left")
    if not found:
        raise ValueError(f"Label '{total_revenue}' not found in Summary sheet. Check {temp_report}")
    wb.save(report)
    os.remove(temp_report)

def run_report():
    try:
        df = load_data(FILENAME)
    
        new_df, rows_before, rows_dropped = clean_data(df)
        summary_df, regions_totals, products_totals = summarize(new_df, rows_before, rows_dropped, TOTAL_REVENUE)
        write_report(summary_df, new_df, regions_totals, products_totals, TEMP_REPORT)
        format_report(REPORT, TOTAL_REVENUE, TEMP_REPORT)
    except Exception as e:
        print(f"Something went wrong: {type(e).__name__}: {e}")
        return False
    return True

if __name__ == "__main__":
    run_report()
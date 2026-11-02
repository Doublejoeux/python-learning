from openpyxl import load_workbook
import pandas as pd
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter
FILENAME = "sales_data.xlsx"
TOTAL_REVENUE = "Total revenue"
REPORT = "sales_report.xlsx"

#Loading an Excel File
wb = load_workbook(FILENAME)
ws = wb["Sales"]

for row in ws.iter_rows(min_row=2, values_only=True):
    print(row)

df = pd.read_excel(FILENAME)
print(df)
print(df.info())

print(df.isna().sum()) 

df["Price"] = df["Price"].fillna(df.groupby("Product")["Price"].transform("median"))

# Cleaning the Data
new_df = df.dropna(subset=["Units"]).copy() # Removing rows with empty units column
print(new_df.isna().sum())

rows_before = len(df)
rows_after = len(new_df)
rows_dropped = rows_before - rows_after
print(f"Rows before: {rows_before}, after: {rows_after}, dropped: {rows_dropped}")

new_df["Revenue"] = new_df["Units"] * new_df["Price"] # Adding Revenue column with formula
print(new_df)

# Summarizing the Data
regions_totals = new_df.groupby("Region")["Revenue"].sum() # Getting revenue totals of each region
print(regions_totals)

products_totals = new_df.groupby("Product")["Revenue"].sum() # Getting revenue totals of each product
print(products_totals)
best_seller_revenue = products_totals.idxmax()
print(f"The best selling product by Revenue is: {best_seller_revenue}") # Printing only the product with the highest revenue

products_totals2 = new_df.groupby("Product")["Units"].sum() # Getting total units sold of each product
print(products_totals2)
best_seller_units = products_totals2.idxmax()
print(f"The best selling product by Units sold is: {best_seller_units}") # Printing only the product with the highest units sold

revenue_total = new_df['Revenue'].sum()

summary_df = pd.DataFrame(
    [("Rows in original file", rows_before),
     ("Rows excluded (Missing Units)", rows_dropped),
     (TOTAL_REVENUE, revenue_total),
     ("Best seller by revenue", best_seller_revenue),
     ("Best seller by units", best_seller_units)
     ],
     columns=["Metric", "Value"]
)

# Writing a Report to Excel
with pd.ExcelWriter(REPORT) as writer:
    summary_df.to_excel(writer, sheet_name="Summary", index=False)
    new_df.to_excel(writer, sheet_name="Clean Data", index= False)
    regions_totals.to_excel(writer, sheet_name="By Region")
    products_totals.to_excel(writer, sheet_name="By Product")

# Formatting with openpyxl
wb_2 = load_workbook(REPORT)
for ws in wb_2.worksheets:  # visits every sheet
    for cell in ws[1]: # ws[1] = every cell in row 1
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = PatternFill(start_color="305496", end_color="305496", fill_type="solid")

    for column_cells in ws.columns: # One group of cells per column
        longest = max((len(str(cell.value)) for cell in column_cells if cell.value is not None), default=0)
        letter = get_column_letter(column_cells[0].column)
        ws.column_dimensions[letter].width = longest + 2  
summary_ws = wb_2["Summary"]
found = False
for label_cell, value_cell in summary_ws.iter_rows(min_row=2,max_col=2):
    if label_cell.value == TOTAL_REVENUE: # Locating a cell by it's label
        value_cell.number_format = "#,##0.00"
        found = True
        print("Cell formatted")
    for cell in (label_cell, value_cell):
        cell.alignment = Alignment(horizontal="left") # aligning the numbers and texts in the columns of the 'Summary' sheet
if not found:
    raise ValueError(f"Label '{TOTAL_REVENUE}' not found in Summary sheet")
wb_2.save(REPORT)
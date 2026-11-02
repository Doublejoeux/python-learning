# make_sample_data.py
# Creates a small sales spreadsheet we can practice on.

from openpyxl import Workbook

def create_sample_file(filename="sales_data.xlsx"):
    wb = Workbook()          # a Workbook is the whole Excel file
    ws = wb.active           # ws = the first worksheet (tab)
    ws.title = "Sales"

    # The header row
    ws.append(["Date", "Region", "Product", "Units", "Price"])

    # Data rows. A couple of blanks on purpose, because real data is messy.
    rows = [
        ["2026-10-01", "Lagos",  "Widget", 10, 25.0],
        ["2026-10-01", "Abuja",  "Gadget", 5,  40.0],
        ["2026-10-02", "Lagos",  "Gadget", 8,  40.0],
        ["2026-10-02", "Abuja",  "Widget", None, 25.0],   # missing units
        ["2026-10-03", "Kano",   "Widget", 12, 25.0],
        ["2026-10-03", "Lagos",  "Gizmo",  3,  60.0],
        ["2026-10-04", "Kano",   "Gadget", 7,  None],     # missing price
    ]
    for row in rows:
        ws.append(row)

    wb.save(filename)
    print(f"Created {filename}")

if __name__ == "__main__":
    create_sample_file()
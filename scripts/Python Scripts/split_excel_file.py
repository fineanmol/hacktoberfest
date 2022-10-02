# Import the modules
import xlwings as xw  # pip install xlwings
import os

# Change the directory and jump to the directory where your excel exists
os.chdir(r"C:\Users\Dell\Downloads\Excel")
EXCEl = r"BackUp.xlsx"  # Your Excel file name

# Run a try condition
try:
    excel_app = xw.App(visible=False)  # Create a new excel instance
    wb = excel_app.books.open(EXCEl)  # Open the Excel sheet
    for sheet in wb.sheets:  # Run a loop and iterate over each sheet
        sheet.api.Copy()  # Copy each sheet to a new workbook
        wb_new = xw.books.active  # Activate the new workbook
        wb_new.save(f"{sheet.name}.xlsx")  # Save the new workbook
        wb_new.close()  # Close the workbook

finally:
    excel_app.quit()  # Finally, Quit the workbook

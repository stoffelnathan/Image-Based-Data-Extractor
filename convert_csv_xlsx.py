# Nathan Stoffel
# 1/2/2025
import pandas as pd

# File paths
csv_path = r"D:\Project\Spreadsheets\Output.csv"
xlsx_path = r"D:\Project\Spreadsheets\Output.xlsx"

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_path)

# Write the DataFrame to Excel file
df.to_excel(xlsx_path, index=False, engine="openpyxl")

print(f"CSV file has been successfully converted to XLSX: {xlsx_path}")

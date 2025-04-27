import pandas as pd

# Load the CSV file that you want to convert:
csv_file = 'books.csv'

# Read the CSV file using pandas:
data = pd.read_csv(csv_file)

# Save the data to an Excel file:
excel_file = 'books.xlsx'
data.to_excel(excel_file, index=False)

print(f"Successfully converted '{csv_file}' to '{excel_file}'.")

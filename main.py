# main.py

# Import libraries.
import os
import sys
import time
import tabula
import pandas as pd

# File name.
file_name = sys.argv[1]

# Path to PDF file to extract tables from.
pdf_path = f"samples/{file_name}.pdf"

# Path to directory for JSON table data.
json_table_path = "tables/json/"

# Path to directory for CSV table data.
csv_table_path = "tables/csv/"

# Extract Table(s).

# The following function parses the PDF file using the tabula library's 
# read_pdf function. The function iterates over the contents of the file 
# and sets any tables it finds as a DataFrame object.

dfs = tabula.read_pdf(pdf_path, pages='all')

# Output length.
print(len(dfs))

# Output the first DataFrame.
print(dfs[0])

# Check if directory exists.
if os.path.isdir(f"{csv_table_path}{file_name}") == False:
	os.makedirs(f"{csv_table_path}{file_name}")


# Save each table to CSV file.
for i in range(len(dfs)):
    dfs[i].to_csv(f"{csv_table_path}{file_name}/{i}.csv")

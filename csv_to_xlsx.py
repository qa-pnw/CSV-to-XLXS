# CSV to XLSX Converter
# Put CSV files into a folder. Enter the folder location into a script 
# Script outputs a single XLSX file with a each original CSV file info in its own tab

import glob
import os
import pandas as pd
import xlsxwriter

path = input("Enter the folder path for the CSV files: ")
xlxs_name = input("Enter a filename for the new Excel file: ")

all_files = glob.glob(os.path.join(path, "*.csv"))
writer = pd.ExcelWriter(f"{xlxs_name}.xlsx", engine='xlsxwriter')

for file in all_files:
    df = pd.read_csv(file)
    df.to_excel(writer, sheet_name=os.path.splitext(os.path.basename(file))[0], index=False)
    print(f'Writing file {file}')

writer.save()

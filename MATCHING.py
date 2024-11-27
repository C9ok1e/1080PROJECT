import pandas as pd
import os
import openpyxl

file_path = "STUDENT_INFO.xlsx"
sheet_name = "Sheet1"

df = pd.read_excel(file_path, sheet_name=sheet_name)

if not df.empty:
    print("Positive")

else:
    print("Negative")

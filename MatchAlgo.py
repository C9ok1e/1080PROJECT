import pandas as pd
import os
import openpyxl
#pip install pandas openpyxl
#pip nstall openpyxl

sortby =
file = STUDENT_INFO.xlsx
read_excel(file,


           
df['freq'] = df.groupby('NAME')['NAME'].transform('count')
df_new = df.sort_values('freq')
print("The 5 students")
print(df_new['freq', 'NAME'])


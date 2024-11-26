import pandas as pd
import os
import openpyxl
#pip install pandas openpyxl
#pip nstall openpyxl

print("input 1 if sort by subject, 2 by 
sortby1 = input(int("Input first priority of sort :")
sortby2 = input(int("Input second priority of sort :")
file = STUDENT_INFO.xlsx
read_excel(file,



           
df['freq'] = df.groupby('NAME')['NAME'].transform('count')
df_new = df.sort_values('freq')
print("The 5 students")
print(df_new['freq', 'NAME'])


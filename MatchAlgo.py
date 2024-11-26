import pandas as pd
import os
import openpyxl
#pip install pandas openpyxl
#pip nstall openpyxl

sortby =
file = STUDENT_INFO.xlsx
read_excel(file,


           df['freq'] = df.groupby('studentid')['studentid'].transform('count')

import pandas as pd
import os
import openpyxl
#pip install pandas openpyxl
#pip nstall openpyxl

file = STUDENT_INFO.xlsx
while true:
           print("input 1 if sort by SUBJECT, 2 by LANGUAGE, 3 for BOTH")
           sortby = input(int("Input filter of sort :")
           if sortby == 1:
                      data = pd.read_excel(file)
                      subdata = data[data['SUBJECT'] == ]
                      print(subdata)
           if sortby == 2:
                      data = pd.read_excel(file)
                      subdata = data[data['SUBJECT']]
                      print(subdata)
                                 

           
df = (df.groupby(['SUBJECT','LANGUAGE'])


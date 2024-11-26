import pandas as pd
import os
import openpyxl
#pip install pandas openpyxl
#pip nstall openpyxl

exit = bool(1)
#set exit code
file = STUDENT_INFO.xlsx
data = pd.read_excel(file)
while exit == bool(1):
           print("input 1 if sort by SUBJECT, 2 by LANGUAGE, 3 for BOTH and 4 to EXIT")
           sortby = input(int("Input filter of sort :"))
           if sortby == 1 :
                      subdata = data[data['SUBJECT'] in subject.lower()]
                      # check if at least one subject is same
                      print(subdata)
           elif sortby == 2 :
                      subdata = data[data['LANGUAGE'] in language.lower()]
                      #check if at least one language is same
                      print(subdata)
           elif sortby == 3 :
                      subdata = data[data['LANGUAGE'] in language.lower()] and data[data['SUBJECT'] in subject.lower()]
                      print(subdata)
           elif sortby == 4 :
                      exit == bool(0)
                      exit()
           else :
                      print('error! please try again!')

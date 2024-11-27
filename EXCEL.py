import pandas as pd
import os
import openpyxl
#PLEASE RUN #5 AND #6 IN TERMINAL IF PROGRAM WAS FAILED TO RUN
#pip install pandas openpyxl
#pip install openpyxl

data = {
    "NAME": [],
    "SUBJECT": [],
    "LANGUAGE": [],
    "CONTENT": []
}

# INPUT/INFO~!
print("Welcome to the student matching system! Please enter the student's information")

while True:
    CHECK = input("PRESS ANY BUTTON TO START or TYPE 'DONE' TO LEAVE：")
    if CHECK.lower() == "done":
        break
    name= input("INPUT NAME：")
    subject= input("INPUT SUBJECT：")
    language= input("INPUT LANGUAGE：")
    while True:
        content = input("INPUT CONTENT (MUST BE 8 DIGITS)：")
        if content == "":
            content = None  # User skipped this field
            break
        elif content.isdigit() and len(content) == 8:
            break
        else:
            print("CONTENT must be exactly 8 digits or left empty. Please try again.")

    data["NAME"].append(name.upper())
    data["SUBJECT"].append(subject.upper())
    data["LANGUAGE"].append(language.upper())
    data["CONTENT"].append(content if content else None)

new_df = pd.DataFrame(data)
filename = "STUDENT_INFO.xlsx"

if os.path.exists(filename):

    existing_df = pd.read_excel(filename)
    combined_df = pd.concat([existing_df, new_df], ignore_index=True)
    combined_df.to_excel(filename, index=False)
    print("Your data was succeed to save")
else:
    new_df.to_excel(filename, index=False)
    print("Your data was succeed to save")



print("Do you want to find groupmates with the system?")
a = input("If yes, please input 1 to match find your group mates:")

import subprocess
print(a)

if a == "1":
    print("Now going to the matching system...")

    try:
        subprocess.run(["python", "MATCHING.py"], check=True)
    except subprocess.CalledProcessError as e:
        print("Error executing the script: {e}")
else:
    print("You did not input 1, exiting.")





import pandas as pd
import os
import openpyxl
#pip install pandas openpyxl
#pip nstall openpyxl


data = {
    "NAME": [],
    "SUBJECT": [],
    "LANGUAGE": [],
    "CONTENT": []
}

# INPUT/INFO~!
print("Please enter the student's information and enter DONE to finish.")

while True:
    CHECK = input("PRESS ANY BUTTON TO START OR TYPE 'DONE' TO LEAVE：")
    if CHECK.lower() == "done":
        break
    name.lower() = input("INPUT NAME：")
    subject.lower() = input("INPUT SUBJECT：")
    language.lower() = input("INPUT LANGUAGE：")
    content.lower() = input("INPUT CONTENT：")

    data["NAME"].append(name)
    data["SUBJECT"].append(subject)
    data["LANGUAGE"].append(language)
    data["CONTENT"].append(content)

new_df = pd.DataFrame(data)
filename = "STUDENT_INFO.xlsx"

if os.path.exists(filename):

    existing_df = pd.read_excel(filename)
    combined_df = pd.concat([existing_df, new_df], ignore_index=True)
    combined_df.to_excel(filename, index=False)
    print("INFO was successfully add to the existing file.")
else:
    if not new_df.empty:
        new_df.to_excel(filename, index=False)
        print("INFO saved to the new file.")
    else:
        print("No data entered, no data saved.")

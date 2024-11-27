import pandas as pd
import os
import openpyxl
#pip install pandas openpyxl
#pip install openpyxl

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
    name= input("INPUT NAME：")
    subject= input("INPUT SUBJECT：")
    language= input("INPUT LANGUAGE：")
    content = input("INPUT CONTENT：")

    data["NAME"].append(name.lower())
    data["SUBJECT"].append(subject.lower())
    data["LANGUAGE"].append(language.lower())
    data["CONTENT"].append(content.lower())

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
        print("Your information was succeed to saved to the system.")
    else:
        print("No data entered, no data saved.")

print("Do you want to find groupmates with the system?")
print("if yes, please input 1 to match find your group mates!")
import pandas as pd

file_path = "STUDENT_INFO.xlsx"
df = pd.read_excel(file_path)

print("Please Enter with the same format:")
print("e.g CHI/ ENG/ COMP1080SEF")

print("if you want to search by language, press enter to skip")
user_subject = input("Please Enter the SUBJECT: ").strip()
user_language = input("Please Enter the LANGUAGE: ").strip()

if user_subject and user_language:
    filtered_data = df[(df['SUBJECT'] == user_subject) & (df['LANGUAGE'] == user_language)]
elif user_subject:
    filtered_data = df[df['SUBJECT'] == user_subject]
elif user_language:
    filtered_data = df[df['LANGUAGE'] == user_language]
else:
    filtered_data = pd.DataFrame()

if not filtered_data.empty:
    print("Filtered Results:")
    print(filtered_data[['NAME', 'SUBJECT', 'LANGUAGE', 'CONTENT']])
else:
    print("No matching records found.")

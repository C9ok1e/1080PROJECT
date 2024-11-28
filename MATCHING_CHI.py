import pandas as pd
import random

file_path = "STUDENT_INFO.xlsx"
df = pd.read_excel(file_path)

print("Please Enter with the same format:")
print("e.g CHI/ ENG/ COMP1080SEF")

print("if you want to search by language, press enter to skip")
user_subject = input("Please Enter the SUBJECT: ").strip().upper()
user_language = input("Please Enter the LANGUAGE: ").strip().upper()

if user_subject and user_language:
    filtered_data = df[(df['SUBJECT'] == user_subject) & (df['LANGUAGE'] == user_language)]
elif user_subject:
    filtered_data = df[df['SUBJECT'] == user_subject]
elif user_language:
    filtered_data = df[df['LANGUAGE'] == user_language]
else:
    filtered_data = pd.DataFrame()

if not filtered_data.empty:
    print("Result filtered.")
    choice = input("How many results would you like to display? Enter 'all' for all results: ").strip().lower()

    if choice == 'all':
        # 顯示所有過濾結果
        print(filtered_data[['NAME', 'SUBJECT', 'LANGUAGE', 'CONTENT']])
    else:
        try:
            num = int(choice)
            if num > len(filtered_data):
                print(f"Only {len(filtered_data)} results available. Displaying all.")
                print(filtered_data[['NAME', 'SUBJECT', 'LANGUAGE', 'CONTENT']])
            else:
                sample_data = filtered_data.sample(n=num)
                print(sample_data[['NAME', 'SUBJECT', 'LANGUAGE', 'CONTENT']])
        except ValueError:
            print("Invalid input. Please enter a number or input 'all'.")
else:
    print("No matching records found.")
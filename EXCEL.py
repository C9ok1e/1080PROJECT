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

# INPUT/入資料
print("請輸入學生的資料，完成後輸入DONE結束。")

while True:
    CHECK = input("按下任意按鍵開始輸入 或輸入DONE結束：")
    if CHECK.lower() == "done":
        break
    name = input("輸入 NAME：")
    subject = input("輸入 SUBJECT：")
    language = input("輸入 LANGUAGE：")
    content = input("輸入 CONTENT：")

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
    print("數據已成功追加到現有文件。")
else:
    if not new_df.empty:
        new_df.to_excel(filename, index=False)
        print("數據已保存到新文件。")
    else:
        print("未輸入任何數據，未儲存文件。")

import subprocess
import sys
def show_language_selection():
    print("請選擇語言 / Please choose a language:")
    print("1. 中文 / Chinese")
    print("2. 英文 / English")

    choice = input("輸入‘1’以中文繼續 / Enter'2'to continue as English (1/2): ")

    if choice == "1":
        subprocess.run([sys.executable, 'EXCEL_CHI.py'])
    elif choice == "2":
        subprocess.run([sys.executable, 'EXCEL.py'])
    else:
        print("無效選擇 / Invalid choice. Please choose again.")
        show_language_selection()

if __name__ == "__main__":
    show_language_selection()
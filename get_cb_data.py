# import requests
# from bs4 import BeautifulSoup

# cookies = {
填入自己cookie
# }

# response = requests.get('https://thefew.tw/cb', cookies=cookies, headers=headers)
# main = BeautifulSoup(response.text)
# print(main.text) #這裡可以print看看已抓取到除標籤外的文字

# with open("test.txt", "w") as file:
#     file.write(main.text)

# print("Text file saved successfully.")

import pandas as pd
from datetime import datetime, timedelta
import pickle, pytz

transfer_percentage = 50
transfer_days_than = 180
transfer_gap_percentage = 9

def is_integer_greater_than_10000(s):
    try:
        num = int(s)
        return num > 10000
    except ValueError:
        return False



def is_percentage_greater_than(s):
    try:
        num = float(s.strip('%'))  #去除百分比轉浮點數
        return num < transfer_percentage
    except ValueError:
        return False


def is_greater_than_days(date_string):
    # 將字符串轉換為日期對象
    date = datetime.strptime(date_string, "%Y-%m-%d")
    
    print(date)
    # 獲取當前日期並設置為UTC+8時區
    current_date = datetime.now(pytz.timezone("Asia/Shanghai"))
    current_date = current_date.replace(tzinfo=None)
    print(current_date)
    # 計算日期差距
    delta = date - current_date
    print(delta)
    # 判斷日期差距是否大於180天
    return delta.days > transfer_days_than


def is_gap_percentage_greater_than(s):
    try:
        num = float(s.strip('%'))  #去除百分比轉浮點數
        return abs(num) < transfer_gap_percentage
    except ValueError:
        return False







with open("test.txt", "r") as file:
    # Read the contents of the file
    file_contents = file.read()


lines = file_contents.split("\n")

c0 = []
c1 = []
c2 = []
c3 = []
c4 = []
c5 = []
c6 = []
c7 = []
c8 = []


for i in range(len(lines)):
    if(is_integer_greater_than_10000(lines[i])):
        print(lines[i])
        if(is_percentage_greater_than(lines[i+13]) and is_greater_than_days(lines[i+14]) and is_gap_percentage_greater_than(lines[i+10])):
            c0.append(lines[i])
            c1.append(lines[i+1])
            c2.append(lines[i+8])
            c3.append(lines[i+9])
            c4.append(lines[i+10])
            c5.append(lines[i+11])
            c6.append(lines[i+12])
            c7.append(lines[i+13])
            c8.append(lines[i+14])

        i = i + 14
        
dic = {
    "代碼": c0,
    "名稱": c1,
    "CB收盤價": c2,
    "轉換價值": c3,
    "轉換溢價率": c4,
    "股票收盤價": c5,
    "轉換價": c6,
    "已轉換(%)": c7,
    "到期/提前賣回日": c8
}

df = pd.DataFrame(dic)

df.to_excel('data.xlsx', index=False)  # 將數據框保存為 Excel 檔案，不包含索引

print(df)



# 爬取 "https://thefew.tw/cb"網站，並對其資料作後處理
   - 網站需要登入才可存取完整檔案，因此需要加入自己的cookie
   - 檔案會輸出成data.xlsx格式

# 環境說明
  - 此程式可直接執行原始碼，使用python即可執行
    
# 程式說明

1. 載入lib 
```shell
# import requests
# from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, timedelta
import pickle, pytz

```
2. 填入自己的cookie，可登入"https://thefew.tw/cb"網站後按網頁檢查，取得cookie後到 "https://curlconverter.com/" 將cookie轉換為python格式
```shell
# cookies = {
xxxx
# }

# headers = {
xxxx
# }
```
3. 讀取檔案，並將網頁資訊存為test.txt
```shell
# response = requests.get('https://thefew.tw/cb', cookies=cookies, headers=headers)
# main = BeautifulSoup(response.text)
# print(main.text) #這裡可以print看看已抓取到除標籤外的文字

# with open("test.txt", "w") as file:
#     file.write(main.text)
```

4. 讀取test.txt檔案
```shell
with open("test.txt", "r") as file:
    # Read the contents of the file
    file_contents = file.read()
lines = file_contents.split("\n")
```

5. 開始解析test.txt檔案
```shell
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
```

6. 判斷式含數判斷完後將值寫入dic
   - is_integer_greater_than_10000(lines[i]) #如果找到一個大於10000的代碼，之後的行數代表這個CB的資訊分別為後1-14行
   - is_percentage_greater_than(lines[i+13]) #轉換比例不能大於x % simon說50%
   - s_greater_than_days(lines[i+14]) #到期日不能少於x 天 simon說180days
   - is_gap_percentage_greater_than(lines[i+10]) #價差不能超過x % simon說10%
```shell
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
```
7. 存入xlsx
```shell
df = pd.DataFrame(dic)

df.to_excel('data.xlsx', index=False)  # 將數據框保存為 Excel 檔案，不包含索引

print(df)

```
8. 未來目標，完成"目標1.jpg"

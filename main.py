from package import *
import csv

DEFAULT_URL = "https://judgment.judicial.gov.tw/FJUD/qryresultlst.aspx"

SEARCH_QUERY = [
    "q=b3275316dca5b005627eed79e843eec6",  # 93~98  353
    "q=87518f061a97aac27da2dc392c642642",  # 99
    "q=7e2c7630c8c840f90a41a7d0c59e7d89",  # 100
    "q=f44a6a3093f54d27858ae55ac61ff907",  # 101
    "q=ea5ca033767b978d9088dc49bd3d163e",  # 102
    "q=f9e6f3b0ebd58ae96a5a6a322843aaf6",  # 103
    "q=d2c284580056636eb4917cc80322e495",  # 104
    "q=a8c879657d1fae55eb29e814928f0007",  # 105
    "q=804be600284fcc9a37624437ef104d91",  # 106
    "q=c806bcab3f8eceb6222b83a6ab020440",  # 107
    "q=867b427fd3e40ab57cfda140ff0bf69a",  # 108
    "q=334a3c6e5da349064693b2441e2bd623",  # 109
    "q=85d81e5c2caaa2c2fc3389db2680d813",  # 110
    "q=68aa6e067d0473af418492fd7e1134e7",  # 111
    "q=6172945538432ce7fa1db2a2f70510a6"   # 112
    ]

session = requests.Session()  # 使用 session 來保持連線狀態

'''
#  Done: 暫時註解
for search_query in SEARCH_QUERY:
    print(f"Processing {SEARCH_QUERY.index(search_query)}")
    try:
        response = session.get(f"{DEFAULT_URL}?ty=JUDBOOK&{search_query}")
        extract_and_save(response, "data.csv")

        for page in range(2, 25):
            print(f"page: {page}")
            res = session.get(f"{DEFAULT_URL}?{search_query}&sort=DS&page={page}&ot=in")
            extract_and_save(res, "data.csv")
    except Exception as e:
        print(f"An error occurred: {e}")
'''

# 使用 data.csv 的 api 取得判決書內容
BASE_URL = "https://judgment.judicial.gov.tw/FJUD/"

# Ongoing: 不同長度的 url 有對應不同的 html 格式，需分開處理
# 初始版本：待修

with open('data.csv', newline='') as file:
    reader = csv.reader(file, delimiter=' ')
    contents = list(reader)

    for url in contents:
        url = ', '.join(url)
        print(getDetailInfo(BASE_URL, url))

        # 將取得的判決書資訊另存於新文件中
        # with open('contents.csv', "a", encoding="utf8",) as newfile:
        #     newfile.write(str(data))
        # newfile.close()

file.close()


# Testing
# getDetailInfo(BASE_URL, "data.aspx?ty=JD&id=IPCV%2c98%2c%e6%b0%91%e5%b0%88%e4%b8%8a%e6%9b%b4(%e4%b8%80)%2c6%2c20091231%2c2&ot=in")
print(getDetailInfo(BASE_URL, "data.aspx?ty=JD&id=IPCV%2c98%2c%e6%b0%91%e5%b0%88%e4%b8%8a%e6%9b%b4(%e4%b8%80)%2c6%2c20091231%2c2&ot=in"))
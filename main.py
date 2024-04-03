# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import requests
import sys

print(sys.getdefaultencoding())

DEFAULT_URL = "https://judgment.judicial.gov.tw/FJUD/qryresultlst.aspx"
SEARCH_QUERY = "q=f28fe0e5ff76c77846a142cb764c2f50"

# 擷取 HTML 元素
def extractHTML(res):
    soup = BeautifulSoup(res.text, "html.parser")
    contents = soup.find_all("a", {"class": "hlTitle_scroll"})
    for data in contents:
        print(data['href'])
    writeCsv("data.csv", contents)

# 取得詳細判決書的 API 後存入 CSV
def writeCsv(filename, dataList):
    with open("data.csv","a", encoding='utf-8',) as file:
        for data in dataList:
            file.write(str(data['href'] + '\n'))
    file.close()

# 回傳第一面搜尋結果
response = requests.get(DEFAULT_URL + "?ty=JUDBOOK&" + SEARCH_QUERY)
extractHTML(response)

# 回傳第 2 ~ 25 面搜尋結果，與第一面 API 不同
# Todo: 自動抓取搜尋最大頁數，目前設定超出上限頁數不會跳出預期外行為
# Todo: 當該搜尋結果超過 500 筆時，將不再顯示搜尋結果，需重設條件後抓取
for page in range(2,25):
    print(f"page: {page}")
    res = requests.get(DEFAULT_URL + "?" + SEARCH_QUERY +"&sort=DS&page="+ str(page) +"&ot=in")
    extractHTML(res)

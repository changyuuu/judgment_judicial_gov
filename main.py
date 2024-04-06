from bs4 import BeautifulSoup
import requests
import csv

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
# response = requests.get(DEFAULT_URL + "?ty=JUDBOOK&" + SEARCH_QUERY)
# extractHTML(response)

# 回傳第 2 ~ 25 面搜尋結果，與第一面 API 不同
# Todo: 自動抓取搜尋最大頁數，目前設定超出上限頁數不會跳出預期外行為
# Todo: 當該搜尋結果超過 500 筆時，將不再顯示搜尋結果，需重設條件後抓取
for page in range(2,25):
    print(f"page: {page}")
    res = requests.get(DEFAULT_URL + "?" + SEARCH_QUERY +"&sort=DS&page="+ str(page) +"&ot=in")
    extractHTML(res)

# 使用 data.csv 的資料取得判決書的詳細內容
BASE_URL = "https://judgment.judicial.gov.tw/FJUD/"

with open('data.csv', newline='') as file:
    reader = csv.reader(file, delimiter=' ')
    contents = list(reader)
    for url in contents:
        url = ', '.join(url)
        res = requests.get(BASE_URL + url)
        data = BeautifulSoup(res.text, "html.parser").find("div", {"id": "jud"})
        print(data)

        # 將取得的判決書資訊另存於新文件中
        with open('contents', "a", encoding="utf8",) as newfile:
            newfile.write(str(data))
        newfile.close()
file.close()
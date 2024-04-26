from package import *
import csv

DEFAULT_URL = "https://judgment.judicial.gov.tw/FJUD/qryresultlst.aspx"

SEARCH_QUERY = [
    "q=561da78895d41383d5d3e773bd90a239",  # 93, 44
    "q=5cb216948f013c3704e44f02c0dc8a2c",  # 94, 88
    "q=05bb553ff905299ab7d072e46f88d739",  # 95, 102
    "q=eb6e869d936ba559be62b6ffd439861c",  # 96, 109
    "q=cbd2cb29d468b9cdde99e9dad9759414",  # 97, 257
    "q=925488997d315aa4cf4aa6181925d3b5",  # 98, 319
    "q=2b8937c8a94b15cf260b6c0c0130b24a",  # 99, 325
    "q=074a96ffd8bfbd306623bf9ac1c9cf0a",  # 100, 451
    "q=72fdc29fa218860b2d9c671a9f4d3c48",  # 101, 359
    "q=1634381fe050990f9fb2e2b9ab479b84",  # 102, 413
    "q=38b7e39655c452b1f5e62a4682e2e4fe",  # 103, 332
    "q=cf9794e4f8c976604a52d1dbea1adb10",  # 104, 300
    "q=cc25374bfa7a3438b49b37eeecf0d511",  # 105, 271
    "q=44f8f47e7b7435d38f02923935f34841",  # 106, 245
    "q=25c71da148182f965f4cae72cd3cfd97",  # 107, 331
    "q=d654819a406810cfdabc59f731efdc16",  # 108, 289
    "q=035d244fa67cb9fc824690a7dc6a9739",  # 109, 387
    "q=6693664abf0fbbb4785d2c0c9957dfd8",  # 110, 300
    "q=9fd03c0bb74c55bf937989155396f1da",  # 111, 195
    "q=85ab7c57abde8a5e805f2d2012d09aa8"   # 112, 231
    ]

session = requests.Session()  # 使用 session 來保持連線狀態

'''#  Done: 暫時註解
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
        print(f"An error occurred: {e}")'''

# 使用 data.csv 的 api 取得判決書內容
BASE_URL = "https://judgment.judicial.gov.tw/FJUD/"

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
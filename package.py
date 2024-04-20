from bs4 import BeautifulSoup
import requests
import time
import re
import requests

# 擷取搜尋結果並寫入 CSV
def extract_and_save(res, filename):
    soup = BeautifulSoup(res.text, "html.parser")
    contents = soup.find_all("a", {"class": "hlTitle_scroll"})

    with open(filename, "a", encoding='utf-8') as file:
        for data in contents:
            file.write(data['href'] + '\n')
            print(data['href'])
    file.close()
    time.sleep(1)

# Todo: 不同長度的 url 有對應不同的 html 格式，需分開處理
def getDetailInfo(BASE_URL, url):
    
    print(len(url))
    data_list_1 = []
    data_list_2 = []

    res = requests.get(BASE_URL + url)
    soup = BeautifulSoup(res.text, "html.parser").find("div", {"id": "jud"})

    rows = soup.find_all("div", {"class": "row"})[:3]
    for item in rows:
        col_td = item.find("div", {"class":"col-td"}).get_text(strip=True)   # Get 判決號、時間、刑由
        data_list_1.append(col_td)
        # print(col_td)
    
    contents = soup.find_all('div', {"class": "jud_content"})
    if contents:
        content = contents[0].find_all("div")
        # [print(item.get_text(strip=True)) for item in content]
        data_list_2.extend([item.get_text(strip=True) for item in content])

    # new_list = data_list.copy()[:5]
    data_list_ = clean_text(data_list_2.copy())[:5]

    new_list = [word for item in data_list_ for word in item.split()][:30]

    return data_list_1, new_list

def clean_text(text_list):
    cleaned_list = []
    for text in text_list:
        cleaned_text = re.sub(r'[^a-zA-Z0-9\u4e00-\u9fff]+', ' ', text) # 使用正規表達式替换非字母字符为空格
        cleaned_list.append(cleaned_text.strip())
        
    return cleaned_list

'''
def getDetailInfo_Way_two(BASE_URL, url):
    
    print(len(url))
    data_list = []
    
    res = requests.get(BASE_URL + url)
    soup = BeautifulSoup(res.text, "html.parser").find("div", {"id": "jud"})

    rows = soup.find_all("div", {"class": "row"})[:3]
    for item in rows:
        col_td = item.find("div", {"class":"col-td"}).get_text(strip=True)   # Get 判決號、時間、刑由
        data_list.append(col_td)
    
    contents = soup.find_all('div', {"class": "htmlcontent"})
    if contents:
        content = contents[0].find_all("div")
        # [print(item.get_text(strip=True)) for item in content]
        data_list.extend([item.get_text(strip=True) for item in content])

    print(data_list)
    return data_list
'''

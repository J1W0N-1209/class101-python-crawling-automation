import requests
from bs4 import BeautifulSoup
import openpyxl

fpath = r"04.python_crawling\data.xlsx"

wb = openpyxl.load_workbook(fpath)
ws = wb["Sheet1"]
index = 2

# 종목 코드 리스트
codes = [
    '005930',
    '000660',
    '035720'
]

for code in codes:
    url = f"https://finance.naver.com/item/sise.naver?code={code}"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html,'html.parser')
    price = soup.select_one("#_nowVal").text
    price = price.replace(',','')
    ws["B" + str(index)] = price
    index = index + 1
wb.save(fpath)
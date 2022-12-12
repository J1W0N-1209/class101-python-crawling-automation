from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

import time
import pyautogui
import pyperclip

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach",True)

# 불필요한 에러 메세지 없애기
chrome_options.add_experimental_option("excludeSwitches",['enable-logging'])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service,options=chrome_options)

# 웹페이지 해당 주소 이동
driver.implicitly_wait(5) # 웹페이지가 로딩 될 때까지 5초는 기다림
driver.maximize_window() # 화면 최대화
driver.get("https://www.naver.com")

# 쇼핑 매뉴 클릭
driver.find_element(By.CSS_SELECTOR,"#NM_FAVORITE > div.group_nav > ul.list_nav.type_fix > li:nth-child(5) > a").click()
time.sleep(2)

# 검색창 클릭
search = driver.find_element(By.CSS_SELECTOR,"#__next > div > div.header_header__24NVj > div > div > div._gnb_header_area_150KE > div > div._gnbLogo_gnb_logo_3eIAf > div > div._gnbSearch_gnb_search_3O1L2 > form > fieldset > div._gnbSearch_inner_2Zksb > div > input")
search.click()

# 검색어 입력
search.send_keys('아이폰 13')
pyautogui.press('enter')

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")

# 아이디 입력창
id = driver.find_element(By.CSS_SELECTOR,"#id")
id.click()
pyperclip.copy("")
pyautogui.hotkey("ctrl","v")
time.sleep(1)

# 비밀번호 입력창
pw = driver.find_element(By.CSS_SELECTOR,"#pw")
pw.click()
pyperclip.copy("")
pyautogui.hotkey("ctrl","v")
time.sleep(1)

# 로그인 버튼
login_btn = driver.find_element(By.CSS_SELECTOR,"#log\.login")
login_btn.click()
time.sleep(1)

# 로그인 완료

# 키워드 : 재테크
# 정렬 : 블로그,최신순
search_url = "https://m.search.naver.com/search.naver?where=m_blog&query=%EC%9E%AC%ED%85%8C%ED%81%AC&sm=mtb_viw.blog&nso=so%3Add%2Cp%3Aall"

driver.get(search_url)
time.sleep(1)

# 블로그 아이디 클릭
driver.find_element(By.CSS_SELECTOR,".sub_txt.sub_name").click()
time.sleep(2)

try:
    # 이웃 추가 버튼 클릭
    driver.find_element(By.CSS_SELECTOR,".link__RsHMX.add_buddy_btn__oGR_B").click()

    # 서로 이웃 버튼 클릭
    driver.find_element(By.CSS_SELECTOR,"#bothBuddyRadio").click()

    input_message = "재테크에 관심있는 학생 입니다."
    textarea = driver.find_element(By.CSS_SELECTOR,".textarea_t1")
    textarea.send_keys(Keys.CONTROL,'a')
    time.sleep(1)
    textarea.send_keys(Keys.DELETE)
    time.sleep(1)
    textarea.send_keys(input_message)

    # 확인 버튼 클릭
    driver.find_element(By.CSS_SELECTOR,".btn_ok").click()
except:
    pass 



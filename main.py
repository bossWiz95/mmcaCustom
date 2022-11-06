from time import sleep
from item import *
import winsound as sd

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service('/Users/dongbin/Desktop/Auto_chromedriver/chromedriver'), options=chrome_options)

# 해당 기존 URL : https://www.kguide.kr/mmca001/
# 숨겨진 iframe URL : https://www.kguide.kr/svc/list?company_code=1388300313&shop_code=138830031301
driver.get("https://www.kguide.kr/svc/list?company_code=1388300313&shop_code=138830031301")
eleMone = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[3]/a")
driver.execute_script("arguments[0].click();", eleMone)

# framePath = driver.find_element(By.CLASS_NAME, "myiframe")
# driver.switch_to.frame(framePath)

# driver.get("https://www.kguide.kr/svc/detail?idx=199&ids=184,172,199,116,118,119,18&page=2&root=mmca001")

soundVolume = 500
soundDuration = 3000
chkCount = 1
isSuccess = 0
day = 10

chkDay = getName(day)

sleep(2)

driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div[2]/div[1]/div/a"))

sleep(2)
for i in range(99999):
    print(str(chkCount) + "번째 시도입니다.")

    eleDay = driver.find_element(By.ID, "day_" + str(day))
    driver.execute_script("arguments[0].click();", eleDay)

    for i in range(chkDay, chkDay+8, 1):
        print(i)
        if driver.find_element(By.ID, "remain_" + str(i)).text != "매진":
            # 해당 시간대 클릭, 약관 동의, 다음
            driver.execute_script("arguments[0].click();", driver.find_element(By.ID, "seq_" + str(i)))
            driver.execute_script("arguments[0].click();", driver.find_element(By.ID, "chk_agree"))
            driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div[3]/div/a"))
            isSuccess += 1
            break

    if isSuccess > 0:
        sd.Beep(soundVolume, soundDuration)
        break
    else:
        chkCount += 1
        driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div[2]/div[1]/div/a"))
        sleep(200)
# seq_83157 > 라디오버튼
# remain_83157 > 매진여부



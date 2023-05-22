from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd

# Khởi tạo trình duyệt
s = Service('driver_chrome/chromedriver.exe')
driver = webdriver.Chrome(service=s)

driver.get("https://www.chotot.com/mua-ban-laptop")
time.sleep(0.5)

# Click button để tắt modal thông báo đăng tin trong trang 
try:
    close_button = driver.find_element(By.CSS_SELECTOR,'.aw__s1k4y3yn')
    if close_button.is_displayed():
        close_button.click()
        time.sleep(0.5)
except NoSuchElementException: 
    pass

# Ghi các link vào file links.txt (test/official) 
# Mỗi page có 25 sản phẩm tương ứng với 25 link 
with open('02 - Dự đoán giá laptop/raw data/test/links.txt', "a", encoding="utf-8") as f: 
    page_start = 1
    page_end = 2
    for i in range(page_start, page_end):
        driver.get("https://www.chotot.com/mua-ban-laptop?page="+str(i))
        time.sleep(0.5)
        a_elements = []
        a_elements = driver.find_elements(By.CSS_SELECTOR,"[class='AdItem_wrapperAdItem__S6qPH  AdItem_big__70CJq'] > a")
        for a in a_elements:
            f.write(a.get_attribute('href') + "\n")
            
# Đóng trình duyệt
driver.quit()

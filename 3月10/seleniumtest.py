from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

try:
    browser = webdriver.Chrome()#声明浏览器
    browser.get('https://www.baidu.com/')#输入百度网址
    inputs = browser.find_element_by_id('kw')#找到搜索框的节点
    inputs.send_keys('Python')#输入Python
    time.sleep(2)
    inputs.send_keys(Keys.ENTER)#点击确定
    wait = WebDriverWait(browser,10)
    wait.until(EC.presence_of_element_located((By.ID,'page')))#等待搜索的内容加载完成
    time.sleep(2)
#     print(browser.current_url)#获取搜索后的网页
#     print(browser.get_cookies())#获取Cookies
    print(browser.page_source)#获取网页原代码
finally:
    browser.close()
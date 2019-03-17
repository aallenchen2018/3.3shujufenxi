from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pickle
import time
import re
from bs4 import BeautifulSoup

import selenium
#######备注：京东的秒杀，框架没被爬取出‘

browser = webdriver.Chrome()
wait = WebDriverWait(browser,5)

# html = "http://search.dangdang.com/?key=%BB%FA%C6%F7%D1%A7%CF%B0&act=input"
# soup=BeautifulSoup(html,'lxml')

# b=soup.select('#p23898620')
# print(soup)
result=browser.get('http://search.dangdang.com/?key=%BB%FA%C6%F7%D1%A7%CF%B0&act=input')
productid=browser.find_element_by_css_selector('#p23898620').text


print(productid)
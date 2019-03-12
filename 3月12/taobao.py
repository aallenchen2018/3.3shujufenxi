from selenium import webdriver
import time
b= webdriver.Chrome()
b.get('https://www.taobao.com')

time.sleep(90)
input1=b.find_element_by_css_selector('#q') ##定位搜索框1
button=b.find_element_by_css_selector('#J_TSearchForm > div.search-button > button')
input1.send_keys('美食')


time.sleep(3)
input1.clear()
input1.send_keys('haochi')
time.sleep
button.click()

time.sleep(5)
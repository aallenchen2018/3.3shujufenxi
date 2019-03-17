from selenium import webdriver
import time
b= webdriver.Chrome()
b.get('https://www.jd.com')

time.sleep(80)
input1=b.find_element_by_css_selector('#key') ##定位搜索框1
button=b.find_element_by_css_selector('#search > div > div.form > button')

input1.send_keys('美食')


time.sleep(3)
input1.clear()
input1.send_keys('haochi')
time.sleep
button.click()

time.sleep(5)

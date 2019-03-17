from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pickle
import time
import re
from bs4 import BeautifulSoup
import pymongo
import selenium
#######备注：京东的秒杀，框架没被爬取出‘

KEYWORD = input('想要搜索的东西')

browser = webdriver.Chrome()
wait = WebDriverWait(browser,5)

MONGO_URL = 'localhost'
MONGO_DB = 'JingDong'

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]
pagech=int(input('输入你想要的页码'))


def save_info(info):
    if db[KEYWORD].update_one({'name':info['name']},{'$set':info},True):
        print('保存成功',info)



def get_search():
    browser.get('https://www.jd.com/')
    browser.delete_all_cookies()
    with open('cookiesJD.dat','rb') as f:
        cookies=pickle.load(f)
    for cookie in cookies:
        browser.add_cookie(cookie)
    try:
        input=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#key')))
        button=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#search > div > div.form > button > i')))
        print(input)
        input.send_keys(KEYWORD)
        button.click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#J_bottomPage > span.p-num > a.curr')))
        get_info(browser.page_source)
        #提取页码信息
        page=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#J_topPage > span > i')))
        
        print('page: '+str(page))
        ###
        # ####京东的最大页是函数，不一定时最后页，获取不到
        return page
    except TimeoutException:
        print('Error')
        return get_search()


def get_next(pn):
    try:
        # input=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#J_bottomPage > span.p-skip > input')))
        button=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#J_bottomPage > span.p-num > a.pn-next > em')))

        # input.clear()
        # input.send_keys(pn)
        button.click()
        #判断是否加载好
        #wait...
        get_info(browser.page_source)
    except TimeoutException:
        print('Error2')
        get_next(pn)

def get_info(html):
    soup=BeautifulSoup(html,'lxml')
    results=soup.select('#J_goodsList > ul > li')
    for result in results:
        info={
            'price':result.select('#J_goodsList > ul > li > div > div.p-price > strong > i')[0].get_text(),
            'name':result.select('#J_goodsList > ul > li > div > div.p-name.p-name-type-2 > a > em')[0].get_text()


        }



        save_info(info)
    




def main():
    page=get_search()
    for pn in range(2,pagech):
        print(pn)
        get_next(pn)
        time.sleep(5)
    browser.close()
    

if __name__=='__main__':
    main()

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

KEYWORD = '美食'

browser = webdriver.Chrome()
wait = WebDriverWait(browser,10)

MONGO_URL = 'localhost'
MONGO_DB = 'Taobao'

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

def save_info(info):
    '''
    :param info:
    :return:
    '''
    if db[KEYWORD].update_one({'href':info['href']},{'$set':info},True):
        print('保存成功',info)

def get_search():
    '''
    访问网页，进行搜索
    :return:
    '''
    browser.get('https://www.taobao.com')
    browser.delete_all_cookies()#清空cookies
    with open('cookies.dat','rb') as f:
        cookies=pickle.load(f)#导出包含账号信息的cookie
    for cookie in cookies:
        browser.add_cookie(cookie)#添加cookie
    try:
        input=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#q')))#定位输入框的节点
        #定位搜索按钮的节点
        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#J_TSearchForm > div.search-button > button')))
        input.send_keys(KEYWORD)#输入搜索信息
        button.click()#点击搜索按钮
        #判断页面是否加载好
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-itemlist > div > div > div:nth-of-type(1) > div')))
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > ul > li.item.active > span'),'1'))
        get_info(browser.page_source)#提取第一页的商品信息，并进行保存
        #提取页码信息
        page = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.total'))).text
        page=int(re.search(r'(\d+)',page).group(1))#提取数字信息
        return page
    except TimeoutException:
        return get_search()

def get_next(pn):
    try:
        #定位页码输入框节点
        input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.form > input')))
        #确定翻页按钮的节点
        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')))
        input.clear()#清空输入框
        input.send_keys(pn)#输入下一页信息
        button.click()#点击确定
        # 判断页面是否加载好
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-itemlist > div > div > div:nth-of-type(1) > div')))
        wait.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > ul > li.item.active > span'), str(pn)))
        get_info(browser.page_source)#提取信息
    except TimeoutException:
        get_next(pn)

def get_info(html):
    '''
    提取商品信息，并进行保存
    :param html:
    :return:
    '''
    soup = BeautifulSoup(html,'html.parser')
    #定位所有商品的节点
    results=soup.select('#mainsrp-itemlist > div > div > div.items > div.item')
    for result in results:
        info={
            'price':result.select('.price strong')[0].get_text(),#价格
            'deal':result.select('.deal-cnt')[0].get_text(),#成交量
            'href':result.select('.title > a')[0].attrs['href'],#商品详细的url
            'name':result.select('.title > a')[0].get_text().strip(),#商品的名字
            'shop':result.select('.shop > a')[0].get_text().strip(),#店铺名
            'location':result.select('.location')[0].get_text()#店铺的地理位置
        }
        save_info(info)#进行保存

#主体函数
def main():
    page=get_search()#从首页进入，搜索关键字，获取当前页的商品信息
    for pn in range(2,page+1):
        print(pn)
        get_next(pn)#进行翻页，提取翻页后的信息
    browser.close()

if __name__=='__main__':
    main()
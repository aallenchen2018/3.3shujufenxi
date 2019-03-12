import time
from Taobaospider import *
import pickle

KEYWORD = '美食'

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)


def get_search():
    browser.get('https://www.taobao.com')
    browser.delete_all_cookies()
    input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#q')))
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button')))
    input.send_keys(KEYWORD)
    button.click()
    time.sleep(10)
    cookies=browser.get_cookies()
    with open('cookies.dat','wb') as f:
        pickle.dump(cookies,f)
    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-itemlist > div > div > div:nth-of-type(1) > div')))
    wait.until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > ul > li.item.active > span'), '1'))


# 主体函数
def main():
    get_search()


if __name__ == '__main__':
    main()
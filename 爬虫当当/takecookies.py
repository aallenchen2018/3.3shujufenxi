import time
from 京东final import *
import pickle

KEYWORD = '笔记本'

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)

def get_search():
    browser.get('https://www.jd.com')
    browser.delete_all_cookies()
    buttonlog=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#ttbar-login > a.link-login')))
    buttonlog.click()
    time.sleep(10)
    cookies=browser.get_cookies()


    input =wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#key')))
    button=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#search > div > div.form > button > i')))
    input.send_keys(KEYWORD)
    button.click()

    with open('cookiesJD.dat','wb') as f:
        pickle.dump(cookies,f)
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#J_bottomPage > span.p-num > a.curr')))
    time.sleep(3)
    browser.close
    
def main():
    get_search()

if __name__=='__main__':
    main()



    
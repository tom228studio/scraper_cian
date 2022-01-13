from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.keys import Keys
from multiprocessing import Pool
from fake_useragent import UserAgent
from random import choice
import requests
import random
import time
import re

with open("/Chromedriver/norm_proxy.txt", "r+") as proxy:
    proxy1 = proxy.read().split(' ')

ua = UserAgent()
options = webdriver.ChromeOptions()

def get_data(url):
    try:
        for i in range(100):
                    proxy = choice(proxy1)
                    options.add_argument("--disable-blink-features=AutomationControlled")
                    options.add_argument(f"user-agent={ua.random}")
                    # options.add_argument(f"--proxy-server={proxy}")
                    options.add_argument("accepts")

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
        driver.get(url=url)
        time.sleep(3)

        try:
            soup = BeautifulSoup(driver.page_source, "lxml")
            pagination = int(soup.find("div", attrs={"data-name": "Pagination"}).find_all("li")[-2].text)
            p = 1
            while p != pagination+2:
                print(p)
                url = f"https://www.cian.ru/cat.php?deal_type=sale&engine_version=2&offer_type=flat&p={p}&region=1&room1=1&room2=1"
                driver.get(url=url)
                soup = BeautifulSoup(driver.page_source, "lxml")
                pagination = int(soup.find("div", attrs={"data-name": "Pagination"}).find_all("li")[-2].text)
                for a in soup.find("div", attrs={"data-name": "Offers"}).find_all("a", class_=re.compile("--link--eoxce")):
                    print(a.get("href"))
                p += 1
        except Exception as ex:
            print(ex)
        time.sleep(random.randrange(1, 6))

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

if __name__ == '__main__':
    time_start = time.time()
    process_count = 1
    url = "https://www.cian.ru/kupit-kvartiru-1-komn-ili-2-komn/"
    urls_list = [url] * process_count
    p = Pool(processes=process_count)
    p.map(get_data, urls_list)
    print(time.time()-time_start)
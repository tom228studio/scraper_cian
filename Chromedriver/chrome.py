# from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.keys import Keys
from multiprocessing import Pool
from fake_useragent import UserAgent
from random import choice
from seleniumwire import webdriver
import random
import time

with open("http_proxies.txt", "r+") as proxy:
    proxy1 = proxy.read().split('\n')
ua = UserAgent()
options = webdriver.ChromeOptions()

def get_data(url):
    try:
        for i in range(100):
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_argument(f"user-agent={ua.random}")
            options.add_argument(f"--proxy-server={choice(proxy1)}")
            options.add_argument("accepts")

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
        # del driver.request.headers['accept']
        # driver.request.headers['accept'] = 'text / html, application / xhtml + xml, application / xml; q = 0.9, image / avif, image / webp, image / apng, * / *;q = 0.8, application / signed - exchange;v = b3;q = 0.9'
        driver.get(url=url)

        time.sleep(random.randrange(1, 6))

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

if __name__ == '__main__':
    process_count = int(input("skoka procesov:"))
    # url = "https://www.cian.ru/cat.php?deal_type=sale&engine_version=2&offer_type=flat&p=1&region=412206&room1=1&room2=1"
    url="https://www.2ip.ru/"
    urls_list = [url] * process_count
    p = Pool(processes=process_count)
    p.map(get_data, urls_list)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.keys import Keys
from multiprocessing import Pool
from fake_useragent import UserAgent
from random import choice
# from seleniumwire import webdriver
import random
import time

with open("../proxy parser/http_proxies.txt", "r+") as proxy:
    proxy1 = proxy.read().split('\n')

ua = UserAgent()
options = webdriver.ChromeOptions()

def get_data(url):
    try:
        for i in range(100):
                    proxy = choice(proxy1)
                    options.add_argument("--disable-blink-features=AutomationControlled")
                    options.add_argument(f"user-agent={ua.random}")
                    options.add_argument(f"--proxy-server={proxy}")
                    options.add_argument("accepts")

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
        # del driver.request.headers['accept']
        # driver.request.headers['accept'] = 'text / html, application / xhtml + xml, application / xml; q = 0.9, image / avif, image / webp, image / apng, * / *;q = 0.8, application / signed - exchange;v = b3;q = 0.9'
        driver.get(url=url)
        try:
            print(driver.find_element_by_class_name("ip"))
            print(choice(proxy1))
            with open("norm_proxy.txt", "a") as file:
                file.write(f" {choice(proxy1)}")
        except Exception as ex:
            print("xyeta")
            print(choice(proxy1))
        time.sleep(random.randrange(1, 6))

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

if __name__ == '__main__':
    process_count = 30
    # url = "https://www.cian.ru/cat.php?deal_type=sale&engine_version=2&offer_type=flat&p=1&region=412206&room1=1&room2=1"
    url="https://www.2ip.ru/"
    urls_list = [url] * process_count
    p = Pool(processes=process_count)
    p.map(get_data, urls_list)

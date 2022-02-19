import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json

driver = webdriver.Chrome()
url = 'https://www.youtube.com/c/joerogan'
driver.get(url + '/videos')

ht=driver.execute_script("return document.documentElement.scrollHeight;")
while True:
    prev_ht=driver.execute_script("return document.documentElement.scrollHeight;")
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(2)
    ht=driver.execute_script("return document.documentElement.scrollHeight;")
    if prev_ht==ht:
        break

links=driver.find_elements_by_xpath('//*[@id="video-title"]')

videos = [link.get_attribute("href") for link in links]

output_dict = {"JRE":videos}

with open('result.json', 'w') as fp:
    json.dump(output_dict, fp)



# for link in links:
#     print(link.get_attribute("href"))

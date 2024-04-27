import os
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

form_link = os.getenv("form_link")
site_url = os.getenv("site_url")

res = requests.get(site_url)
soup = BeautifulSoup(res.text, "html.parser")

listings = soup.find_all(class_="StyledPropertyCardDataArea-anchor")
listing_links = [listing.get("href") for listing in listings]

prices = soup.find_all(class_="PropertyCardWrapper__StyledPriceLine")
costs = [price.text[:6] for price in prices]

properties = soup.find_all(name="address")
addresses = [property.text.strip().replace(" |", "") for property in properties]

houses = [
    {"cost": costs[i], "address": addresses[i], "link": listing_links[i]}
    for i in range(len(costs))
]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(form_link)
time.sleep(4)

for house in houses:
    address_line = driver.find_element(
        By.XPATH,
        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input',
    )
    cost_line = driver.find_element(
        By.XPATH,
        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input',
    )
    link_line = driver.find_element(
        By.XPATH,
        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input',
    )
    submit_btn = driver.find_element(
        By.XPATH,
        value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span',
    )
    address_line.send_keys(house["address"])
    cost_line.send_keys(house["cost"])
    link_line.send_keys(house["link"])
    submit_btn.click()
    time.sleep(1)
    driver.refresh()
    time.sleep(3)
    
driver.quit()
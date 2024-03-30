import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.CSS_SELECTOR, value="#cookie")
money = driver.find_element(By.CSS_SELECTOR, value="#money")

checkpoint = time.time()
timeout = time.time() + 60 * 5  # 5 minutes from now


def get_power_ups():
    power_ups = []
    store = driver.find_elements(By.CSS_SELECTOR, value="#store div b")
    items = [(item.text.split(" - ")) for item in store]
    items.pop(-1)
    for item in items:
        item[1] = int(item[1].replace(",", ""))
        if int(money.text) >= item[1]:
            power_ups.append(item)
    print(power_ups)
    return power_ups


while time.time() < timeout:
    cookie.click()
    if time.time() > checkpoint + 5:
        power_ups = get_power_ups()
        # for item in items:
        if power_ups:
            upgrade = driver.find_element(
                By.CSS_SELECTOR, value=f"#buy{power_ups[-1][0]}"
            )
            upgrade.click()
            upgrade = None
            money = driver.find_element(By.CSS_SELECTOR, value="#money")
            money = int(money.text.replace(",", "")) if int(money.text) > 999 else money
        print("5 sec passed!")
        checkpoint += 5


print(f"FINAL COOKIE AMOUNT: {money.text}")

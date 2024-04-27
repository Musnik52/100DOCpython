import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException as eci_exception


class InstaFollower:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self, password, email):
        self.driver.get("https://instagram.com/")
        time.sleep(4)

        login_email = self.driver.find_element(
            By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input'
        )
        login_email.send_keys(email)

        login_password = self.driver.find_element(
            By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input'
        )
        login_password.send_keys(password)
        time.sleep(2)

        login_submit = self.driver.find_element(
            By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button/div'
        )
        login_submit.click()
        time.sleep(5)

        save_login_prompt = self.driver.find_element(
            by=By.XPATH,
            value="//div[contains(text(), 'לא עכשיו')]",
            # by=By.XPATH, value="//div[contains(text(), 'Not Now')]"
        )
        save_login_prompt.click() if save_login_prompt else ""
        time.sleep(2)

        notifications_prompt = self.driver.find_element(
            by=By.XPATH,
            value="// button[contains(text(), 'לא עכשיו')]",
            # by=By.XPATH, value="// button[contains(text(), 'Not Now')]"
        )
        notifications_prompt.click() if save_login_prompt else ""

    def find_followers(self, insta_name):
        self.driver.get(f"https://instagram.com/{insta_name}/followers")
        time.sleep(5)
        scroll_bar = self.driver.find_element(
            By.XPATH,
            value="/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]",
        )
        for i in range(10):
            self.driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollHeight", scroll_bar
            )
            time.sleep(2)

    def follow(self):
        follow_buttons = self.driver.find_elements(
            By.CSS_SELECTOR, value="._aano button"
        )
        for btn in follow_buttons:
            try:
                btn.click()
                time.sleep(2)
            except eci_exception:
                cancel_btn = self.driver.find_element(
                    by=By.XPATH,
                    value="//button[contains(text(), 'ביטול')]",
                    # by=By.XPATH, value="//button[contains(text(), 'Cancel')]"
                )
                cancel_btn.click()
        pass

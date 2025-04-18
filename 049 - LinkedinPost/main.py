import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# הגדרות לדרייבר
time.sleep(2)
driver = webdriver.Chrome("049 - JobAplicator\chromedriver.exe")
driver.get("https://linkedin.com/")  # כתובת האתר הרצוי

# מסך התחברות
username = driver.find_element(
    By.XPATH, value="//input[@name='session_key']"
)  # זיהוי שורת שם המשתמש
password = driver.find_element(
    By.XPATH, value="//input[@name='session_password']"
)  # זיהוי שורת הסיסמה
submit = driver.find_element(
    By.XPATH, value="//button[@type='submit']"
)  # זיהוי כפתור הכניסה
time.sleep(2)
username.send_keys("YOUR_USERNAME_HERE")  # הכנסת שם המשתמש
password.send_keys("YOUR_PASSWORD_HERE")  # הכנסת הסיסמה
submit.click()  # לחיצה על כפתור הכניסה

time.sleep(2)
post_line = driver.find_element(
    By.XPATH,
    value="//button[@class='artdeco-button artdeco-button--muted artdeco-button--4 artdeco-button--tertiary ember-view share-box-feed-entry__trigger']",  # זיהוי שורת כתיבת הסטטוס
)
post_line.click()  # לחיצה על שורת הפוסט
time.sleep(2)

paragraph = driver.find_elements(By.TAG_NAME, value="p")  # זיהוי פסקאות
with open(
    "linkedin_post\post.txt", "r", encoding="utf8"
) as f:  # פתיחת קובץ טקסט רצוי לפרסום
    # פסקה רצויה + הכנסת נתונים
    paragraph[0].send_keys(f.readlines())
time.sleep(2)
post_btn = driver.find_element(
    By.XPATH,
    value="//button[@class='share-actions__primary-action artdeco-button artdeco-button--2 artdeco-button--primary ember-view']",  # זיהוי כפתור פרסום
)
post_btn.click()  # לחיצה על כפתור הפרסום

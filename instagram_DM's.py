from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

TARGET='TARGET_INSTAGRAM_ACCOUNT'
USERNAME='YOUR_USERNAME'
PASSWORD='YOUR_PASSWORD'

class InstaMessager():
    def __init__(self) -> None:
        self.options = Options()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.options)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        username=self.driver.find_element(By.NAME, "username")
        username.send_keys(USERNAME)
        password=self.driver.find_element(By.NAME, "password")
        password.send_keys(PASSWORD)
        time.sleep(1)
        password.send_keys(Keys.ENTER)

    def message(self):
        time.sleep(2)
        self.driver.get(f'https://www.instagram.com/{TARGET}/')
        time.sleep(4)
        message=self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div')
        message.click()
        time.sleep(4)

    def send_message(self):
        text=self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]')
        text.send_keys("wassupp")
        time.sleep(1)
        text.send_keys(Keys.ENTER)
        time.sleep(1)
        text2=self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]')
        text2.send_keys("hello")
        time.sleep(1)
        text2.send_keys(Keys.ENTER)
            

bot=InstaMessager()
bot.login()
bot.message()
bot.send_message()
    

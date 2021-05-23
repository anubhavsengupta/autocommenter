from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from instaBot import Bot
import time


class Message(Bot):
    def __init__(self, message):
        super().__init__()
        self.message = message
        self.chrome_driver = chrome_driver = "C:\Development\chromedriver_win32\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=chrome_driver)
        self.driver.get("https://www.instagram.com/accounts/login/")
        self.comments = []

    def login(self):
        super().login()

    def messageUser(self, index):
        time.sleep(2)
        DM = self.driver.find_element_by_css_selector(
            '.bqXJH')
        time.sleep(1)
        DM.click()
        time.sleep(4)
        firstUser = self.driver.find_elements_by_css_selector('.R19PB')
        firstUser[index].click()
        for i in range(12):
            messagebox = self.driver.find_element_by_css_selector('.X3a-9 textarea')
            messagebox.send_keys(self.message)

            time.sleep(1)
            messagebox.send_keys(Keys.ENTER)



m = Message("t")

m.login()
m.messageUser(1)

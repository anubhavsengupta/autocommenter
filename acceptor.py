from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from instaBot import Bot
import time


class Acceptor(Bot):
    def __init__(self, allComments=True, amount=0):

        super().__init__()
        self.all = allComments
        self.amount = amount
        self.chrome_driver = chrome_driver = "C:\Development\chromedriver_win32\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=chrome_driver)
        self.driver.get("https://www.instagram.com/accounts/login/")

    def login(self):
        super().login()

    def navigate(self):
        time.sleep(1)
        hrt = self.driver.find_element_by_class_name("_0ZPOP kIKUG ")
        print(hrt)
        hrt.click()
        time.sleep(4)

        request = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[4]/div/div[2]/div[2]/div/div/div/div/div[1]/div[1]/div')
        request.click()


acceptor = Acceptor()

acceptor.login()
acceptor.navigate()

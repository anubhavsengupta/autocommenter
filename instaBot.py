from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time


class Bot:
    def __init__(self):
        self.chrome_driver = chrome_driver = "C:\Development\chromedriver_win32\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=chrome_driver)
        self.driver.get("https://www.instagram.com/accounts/login/")
        self.comments = []

    def wait(self, element):
        wait = WebDriverWait(self.driver, 20)

        username = wait.until(EC.element_to_be_clickable((By.XPATH, element)))

    # login to instagram
    def login(self):
        # get credentials
        with open('credentials.txt', 'r') as f:
            creds = f.readlines()
            username = creds[0]
            password = creds[1]

        # Find html elements in page
        time.sleep(3)
        user_name = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        pass_word = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        button = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')

        user_name.send_keys(username)
        pass_word.send_keys(password)

        time.sleep(1)

        # click confirmation
        button.click()
        time.sleep(4)

        # other popups
        info_save = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        info_save.click()
        # Click off notification pop up
        notification_btn = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        time.sleep(3)
        notification_btn.click()
    def comment(self):
        # List of comments
        comments = []
        with open("comments.txt", "r") as f:
            for line in f.readlines():
                comments.append(line)
        print(comments)
        try:
            time.sleep(3)
            comment_link = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/section/div/div[2]/div/article[1]/div[3]/section[1]/span[2]/button')

            time.sleep(3)
            print(comment_link)
            time.sleep(1)
            comment_link.click()
            time.sleep(1)
            comment_area = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea')
            time.sleep(1)
            comment_area.click()
            ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)  # exceptions to ignore while
            # handling the updated DOM
            time.sleep(1)
            textbox = self.driver.find_elements_by_css_selector(".X7cDz textarea")
            print(textbox)

            # insert any text
            textbox[0].send_keys("im the slowest acceptor")
            time.sleep(3)
            send_btn = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button')
            self.wait('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button')
            send_btn.click()

            home_btn = self.driver.find_element_by_css_selector(".Fifk5 svg")
            home_btn.click()
            time.sleep(6)
            self.driver.refresh()


        # handle DOM exceptions
        except Exception as e:
            print("error has occured")
            print(e)

            # refresh to home screen

            home_btn = self.driver.find_element_by_css_selector(".Fifk5 svg")
            home_btn.click()
            time.sleep(6)
            self.driver.refresh()

#
b = Bot()
b.login()
for i in range(25):
    b.comment()
if __name__ == '__main__':
    pass

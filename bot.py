from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.action_chains import ActionChains

chrome_driver = "C:\Development\chromedriver_win32\chromedriver.exe"


driver = webdriver.Chrome(executable_path=chrome_driver)

def wait(element):
    wait = WebDriverWait(driver, 20)

    username = wait.until(EC.element_to_be_clickable((By.XPATH, element)))


driver.get("https://www.instagram.com/accounts/login/")


def login():

    time.sleep(3)
    username = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
    password = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
    button = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')

    username.send_keys("1senguptaakk@gmail.com")
    password.send_keys("Indigo234")

    time.sleep(1)

    button.click()
    time.sleep(4)

    info_save = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
    info_save.click()

    notification_btn = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
    time.sleep(3)
    notification_btn.click()
login()
def comment():
    try:
        time.sleep(3)
        comment_link = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/section/div/div[2]/div/article[1]/div[3]/section[1]/span[2]/button')

        time.sleep(3)
        print(comment_link)
        time.sleep(1)
        comment_link.click()
        time.sleep(1)
        comment_area = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea')
        time.sleep(1)
        comment_area.click()
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)  # exceptions to ignore while
        # handling the updated DOM
        time.sleep(1)
        textbox = driver.find_elements_by_css_selector(".X7cDz textarea")
        print(textbox)

        # insert any text
        textbox[0].send_keys("im the slowest acceptor")
        time.sleep(3)
        send_btn = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button')
        wait('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button')
        send_btn.click()

        home_btn = driver.find_element_by_css_selector(".Fifk5 svg")
        home_btn.click()
        time.sleep(6)
        driver.refresh()


    # handle DOM exceptions
    except Exception as e:
        print("error has occured")
        print(e)

        #refresh to home screen

        home_btn = driver.find_element_by_css_selector(".Fifk5 svg")
        home_btn.click()
        time.sleep(6)
        driver.refresh()


for i in range(8):
    comment()
    time.sleep(2)


if __name__ == '__main__':
    pass
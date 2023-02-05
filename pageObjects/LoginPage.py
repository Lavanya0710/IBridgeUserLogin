import time
from selenium.webdriver.common.by import By


class Login:
    txt_username_id = "email"
    txt_password_id = "password"
    btn_signin_xpath = "//span[contains(text(),'Sign In')]"
    btn_user_xpath = '//*[@id="root"]/header/div/div/div[2]/button/span'
    btn_logout_xpath = '//*[@id="menu-appbar"]/div[3]/ul/li'

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.ID, self.txt_username_id).clear()
        self.driver.find_element(By.ID, self.txt_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.txt_password_id).clear()
        self.driver.find_element(By.ID, self.txt_password_id).send_keys(password)

    def clickSignin(self):
        self.driver.find_element(By.XPATH, self.btn_signin_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.btn_user_xpath).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.btn_logout_xpath).click()

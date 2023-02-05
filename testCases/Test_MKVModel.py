import time

from pageObjects.LoginPage import Login
from pageObjects.MKV_page import MKVPage
from utilities.readProperty import ReadConfig


class Test_003_MKV_Model:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    def test_mkv(self, setUp):
        self.driver = setUp
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickSignin()
        time.sleep(2)

        self.mkv = MKVPage(self.driver)
        self.mkv.click_mkv()
        time.sleep(1)
        self.mkv.click_Persanlity()
        time.sleep(1)

        self.driver.quit()


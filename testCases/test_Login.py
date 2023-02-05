
import time
import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from pageObjects.LoginPage import Login
# from utilities.customeLogger import LogGen
from utilities.readProperty import ReadConfig


class Test_001_Login:
    # baseURL = "https://learner.ibridge360.com/sign-in"
    # username = 'subhashkmr16@gmail.com'
    # password = 'aroha9065'

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    # logger = LogGen.loggen()

    def test_homePageTitle(self, setUp):
        # self.logger.info("\n ----------- Test__001_Login -------------- ")
        # self.logger.info("---------- Varifying  Home page title ------------------\n")
        # self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver = setUp
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == 'IBridge3602':
            assert True
            self.driver.close()
            # self.logger.info("---------- Varifying  Home page title is passed ------------------\n")
        else:
            self.driver.save_screenshot("C:\\Users\\subha\\PycharmProjects\\iBridge360Aroha/Screenshots\\" + "testHomeTitle.png")
            self.driver.close()
            # self.logger.error("---------- Varifying  Home page title is Failed  ------------------\n")
            assert False

    def test_login(self, setUp):
        # self.logger.info("---------- Varifying  loging test  ------------------\n")
        # self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver = setUp
        self.driver.get(self.baseURL)

        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickSignin()

        act_title = self.driver.title

        if act_title == 'IBridge360':
            print('Test 2 -- Passed ')
            assert True
            # self.logger.info("---------- Varifying  loging test is Passed ------------------\n")
        else:
            self.driver.save_screenshot("C:\\Users\\subha\\PycharmProjects\\iBridge360Aroha/Screenshots\\" + "test_login.png")
            self.driver.close()
            # self.logger.error("---------- Varifying  loging test is failed  ------------------\n")
            assert False

        time.sleep(2)
        self.lp.clickLogout()
        time.sleep(1)
        self.driver.close()

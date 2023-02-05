import time

from pageObjects.CourseVideoPage import VideoCourse
from pageObjects.LoginPage import Login
from pageObjects.MKV_page import MKVPage
from pageObjects.courseVodeoContents import VideoContentsCourse
from utilities.readProperty import ReadConfig


class Test_002_DataEnggVideo:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    def test_dataEnggVideo(self, setUp):
        self.driver = setUp
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickSignin()

        time.sleep(1)
        self.cvp = VideoCourse(self.driver) #CourseVideoPage for data engineer
        self.cvp.clickDataEngg()
        time.sleep(1)
        # self.cvp.clickPowerBi()
        self.cvp.clickOracleSQL()
        time.sleep(1)
        self.cvp.windowHandle()
        time.sleep(2)

        self.vcc = VideoContentsCourse(self.driver) #VideoContentsCourse
        self.vcc.clickVidoeLink()
        time.sleep(5)
        self.vcc.clickPreviousBtn()
        time.sleep(5)
        self.driver.close()


        self.driver.quit()

import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Ibridge:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://learner.ibridge360.com/sign-in")
    time.sleep(0.4)
    driver.maximize_window()
    time.sleep(0.3)

    UserId = 'subhashkmr16@gmail.com'
    Password = 'aroha9065'

    dataEngg_xpath = '//*[@id="root"]/div[2]/div/div[1]/a/div/div[2]'
    powerBI_xpath = "//*[text()='Power BI']//following::*[text()='View Program Content']"
    videoLinkContent = "//div[@class='jss50']//div[3]//div[1]//div[1]//div"
    #overviewOfPowerBi_xpath = '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div'
    previousBTN_xpath = "//div[1][@class='iconContainer']"
    nextBtn_xpath = "div.MuiContainer-root.courseVideoViewContainer.MuiContainer-maxWidthXl div.courseInfoViewContainer div.MuiGrid-root.MuiGrid-container.MuiGrid-spacing-xs-5 div.MuiGrid-root.MuiGrid-item.MuiGrid-grid-xs-12.MuiGrid-grid-md-8:nth-child(1) div.MuiPaper-root.MuiCard-root.jss36.MuiPaper-elevation1.MuiPaper-rounded div.MuiCardContent-root.jss37 div.courseInfoPaginations > div.iconContainer:nth-child(3)"
    mkv_module_xpath = "//li[2]//a[@class= 'nav-links']"

    def UserLogin(self):
        username = self.driver.find_element(By.ID, 'email')
        username.click()
        time.sleep(0.2)
        username.send_keys(self.UserId)

        password = self.driver.find_element(By.ID, 'password')
        password.send_keys(self.Password)
        time.sleep(0.2)
        password.send_keys(Keys.ENTER)
        time.sleep(0.7)

    def clickDataEngg(self):
        self.driver.find_element(By.XPATH, self.dataEngg_xpath).click()
        time.sleep(0.8)

    def clickPowerBi(self):

        self.driver.find_element(By.XPATH, self.powerBI_xpath).click()
        time.sleep(0.7)


    def windowHandle(self):
        handle = self.driver.window_handles
        for i in handle:
            self.driver.switch_to.window(i)

    def clickVidoeLink(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.videoLinkContent).click()
        time.sleep(5)

    def clickPreviousBtn(self):
        self.driver.find_element(By.XPATH, self.previousBTN_xpath).click()
        time.sleep(5)

    def clickNextBtn(self):
        self.driver.find_element(By.XPATH, self.nextBtn_xpath).click()
        time.sleep(5)

    def windowClose(self):
        time.sleep(5)
        self.driver.quit()

    def click_mkv(self):
        self.driver.find_element(By.XPATH, self.mkv_module_xpath).click()
        time.sleep(6)

ib = Ibridge()
ib.UserLogin()
ib.clickDataEngg()
# ib.clickPowerBi()
# ib.windowHandle()
# ib.clickVidoeLink()
# ib.clickPreviousBtn()
# ib.clickNextBtn()

ib.click_mkv()

ib.windowClose()

from selenium.webdriver.common.by import By

class VideoContentsCourse:
    videoLinkContent = "//div[@class='jss50']//div[3]//div[1]//div[1]//div"
    previousBTN_xpath = "//div[1][@class='iconContainer']"
    nextBtn_xpath = "//div[2][@class='iconContainer']"

    def __init__(self, driver):
        self.driver = driver

    def clickVidoeLink(self):
        self.driver.find_element(By.XPATH, self.videoLinkContent).click()

    def clickPreviousBtn(self):
        self.driver.find_element(By.XPATH, self.previousBTN_xpath).click()

    def clickNextBtn(self):
        self.driver.find_element(By.XPATH, self.nextBtn_xpath).click()


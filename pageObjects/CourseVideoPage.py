from selenium.webdriver.common.by import By


class VideoCourse:
    dataEngg_xpath = '//*[@id="root"]/div[2]/div/div[1]/a/div/div[2]'
    oracleSQL_xpath = "//p[text()='Oracle SQL']//following::span[1]"
    powerBI_xpath = "//*[text()='Power BI']//following::*[text()='View Program Content']"

    def __init__(self, driver):
        self.driver = driver

    def clickDataEngg(self):
        self.driver.find_element(By.XPATH, self.dataEngg_xpath).click()

    def windowHandle(self):
        handle = self.driver.window_handles
        for i in handle:
            self.driver.switch_to.window(i)

    def clickOracleSQL(self):
        self.driver.find_element(By.XPATH, self.oracleSQL_xpath).click()

    # def clickVideo
    def clickPowerBi(self):
        self.driver.find_element(By.XPATH, self.powerBI_xpath).click()




import time

from selenium.webdriver.common.by import By


class MKVPage:
    mkv_module_xpath = "//li[2]//a[@class= 'nav-links']"
    chk_prn_xpath = "//body/div[@id='root']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]"

    def __init__(self, driver):
        self.driver = driver

    def click_mkv(self):
        self.driver.find_element(By.XPATH, self.mkv_module_xpath).click()
        time.sleep(1)

    def click_Persanlity(self):
        self.driver.find_element(By.XPATH,self.chk_prn_xpath)
        time.sleep(3)

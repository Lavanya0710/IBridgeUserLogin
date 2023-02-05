import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager


# @pytest.fixture()
# def setUp(browser):
#     if browser == 'chrome':
#         driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#         # driver = webdriver.Chrome(executable_path="D:\Subhash\selenium\drivers\chromedriver_win32\chromedriver.exe")
#     elif browser == 'firefox':
#         driver = webdriver.Firefox(executable_path="D:\Subhash\selenium\drivers\geckodriver-v0.30.0-win64\geckodriver.exe")
#         # driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
#     else:
#         # driver = webdriver.ie(server=Service(IEDriverManager().install()))
#         driver = ' Not able to call'
#     return driver

# def pytest_addition(parser):
#     parser.addoption("--browser")
#
# @pytest.fixture()
# def browser(request):  #this will return the Browser value to setup method
#     return request.config.getoption("--browser")

#
@pytest.fixture()
def setUp():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # driver = webdriver.Chrome(executable_path="D:\Subhash\selenium\drivers\chromedriver_win32\chromedriver.exe")
    # driver = webdriver.Firefox(executable_path="D:\Subhash\selenium\drivers\geckodriver-v0.30.0-win64\geckodriver.exe")
    # driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    return driver

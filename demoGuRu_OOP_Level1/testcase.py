import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from demoGuRu_OOP_Level1.functions_Support import common_func


class signUpTestCase(common_func):
    @pytest.fixture(scope="class")
    def setup(self):
        global driver
        global signUp
        signUp = common_func
        self.driver= signUp.driver
        driver = webdriver.Chrome("/Users/tminht/PycharmProjects/FiistSeleniumTest/drivers/chromedriver")
        driver.implicitly_wait(10)
        driver.get("http://demo.guru99.com/V4/")
        yield
        driver.quit()
        print("Test completed")

    def test1_signUp(self, setup):
        'sign up, login'
        global passWord
        global userID
        signUp.click(self, "//a[text()='here']")
        signUp.sendkey(self, "//input[@name='emailid']", "thong4333@test.com")
        signUp.sendkey(self, "//input[@name='emailid']", Keys.ENTER)

import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import pytest
import string
import random

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def randomString(nhap_so_kitu):

    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(nhap_so_kitu))
def randomNum(nhapSoLuongNumberVaoDiAThongAhihi):
    nums = string.digits
    return ''.join(random.choice(nums) for i in range(nhapSoLuongNumberVaoDiAThongAhihi))

class Testsample():
    @pytest.fixture(scope="class")
    def setup(self):
        global driver
        driver = webdriver.Chrome("/Users/tminht/PycharmProjects/FiistSeleniumTest/drivers/chromedriver")
        driver.implicitly_wait(10)
        driver.get("http://demo.guru99.com/V4/")
        yield
        driver.quit()
        print("Test completed")


    def test_1(self,setup):
        'sign up, login'
        global passWord
        global userID
        driver.find_element_by_xpath("//a[text()='here']").click()
        driver.find_element_by_xpath("//input[@name='emailid']").send_keys( "thong4333@test.com")
        driver.find_element_by_xpath("//input[@name='emailid']").send_keys(Keys.ENTER)
        userID = driver.find_element_by_xpath("//td[text()='User ID :']//following-sibling::td").text
        passWord = driver.find_element_by_xpath("//td[text()='Password :']//following-sibling::td").text
        print(passWord)
        driver.back()
        driver.back()
        print("UserID= " + userID)
        print("Password= " + passWord)
        driver.find_element_by_xpath("//input[@name='uid']").send_keys(userID)
        driver.find_element_by_xpath("//input[@name='password']").send_keys(passWord)
        driver.find_element_by_xpath("//input[@name='btnLogin']").click()


    # actual_UserID_Text = driver.find_element_by_xpath("//td[text()='Manger Id : " + userID + "\']").text
    # print(actual_UserID_Text)

    # assert_equal(actual_UserID_Text, "Manger Id : " + userID)

    def test_2(self,setup):
        #click new customer
        driver.find_element_by_xpath("//a[text()='New Customer']").click()
        driver.find_element_by_xpath("//input[@name='name']").send_keys("Thong")
        driver.find_element_by_xpath("//input[@value='m']").click()
        driver.find_element_by_xpath("//textarea[@name='addr']").send_keys("tang bat Ho Q5")
        driver.find_element_by_xpath("//input[@name='city']").send_keys("Ho Chi Minh City")
        driver.find_element_by_xpath("//input[@name='emailid']").send_keys("thong" + randomString(3) + "@gmail.com")
        driver.find_element_by_xpath("//input[@name='password']").send_keys(passWord)

        start_date = driver.find_element_by_xpath("//input[@name='dob']")
        start_date.clear()
        start_date.send_keys("08/08/1990")
        driver.find_element_by_xpath("//input[@name='dob']")

        driver.find_element_by_xpath("//input[@name='state']").send_keys("Ho chi minh")
        driver.find_element_by_xpath("//input[@name='pinno']").send_keys(randomNum(6))
        driver.find_element_by_xpath("//input[@name='telephoneno']").send_keys("0978135885")
        time.sleep(5)
        driver.find_element_by_xpath("//input[@value='Submit']").click()

        # verify login success

        # verify add new customer thành công
        try :
            verify_NewCS = driver.find_element_by_xpath("//p[text()='Customer Registered Successfully!!!']").text
            assert verify_NewCS == "Customer Registered Successfully!!!"
        except :
            print("failed")

    def test_3(self,setup):
        global customerID
        'edit customer'
        #edit customer

        try :
            wait = WebDriverWait(driver, 10)
            element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "///td[text()='Customer ID']//following-sibling::td")))
        except :
            print("Failed to load search element")

        customerID = driver.find_element_by_xpath("//td[text()='Customer ID']//following-sibling::td").text
        driver.find_element_by_xpath("//a[text()='Edit Customer']").click()
        driver.find_element_by_xpath("//input[@name='cusid']").send_keys(customerID)
        driver.find_element_by_xpath("//input[@name='AccSubmit']").click()

        driver.find_element_by_xpath("//textarea[@name='addr']").clear()
        driver.find_element_by_xpath("//textarea[@name='addr']").send_keys("Tettt")

        driver.find_element_by_xpath("//input[@name='city']").clear()
        driver.find_element_by_xpath("//input[@name='city']").send_keys("Quan Tan Binh")

        driver.find_element_by_xpath("//input[@name='pinno']").clear()
        driver.find_element_by_xpath("//input[@name='pinno']").send_keys("4567923")

        driver.find_element_by_xpath("//input[@name='emailid']").clear()
        driver.find_element_by_xpath("//input[@name='emailid']").send_keys(
            "thong98797@gmail.com")

        driver.find_element_by_xpath("//input[@name='sub']").click()

        #verify Edit Customer

        try :
            verify_EditCS = driver.find_element_by_xpath("//p[text()='Customer details updated Successfully!!!']").text
            assert verify_EditCS == "Customer details updated Successfully!!!"
        except :
            print("failed")


    def test_4(self,setup):
        'add new account'
        # global addAccount
        driver.find_element_by_xpath("//a[text()='New Account']").click()
        #  addAccount = driver.find_element_by_xpath("//td[text()='Customer ID']//following-sibling::td").text
        driver.find_element_by_xpath("//input[@name='cusid']").send_keys(customerID)
        driver.find_element_by_xpath("//input[@name='inideposit']").send_keys("100000")
        driver.find_element_by_xpath("//input[@name='button2']").click()

        #verify New account successful

        try:
            verify_addNewID = driver.find_element_by_xpath("//p[text()='Account Generated Successfully!!!']").text
            assert verify_addNewID == "Account Generated Successfully!!!"
        except:
            print("failed")




    def test_5(self,setup):
        'edit account'

        global accID
        accID = driver.find_element_by_xpath(
            "//td[text()='Account ID']//following-sibling::td").text  # copy screenshot accID
        driver.find_element_by_xpath("//a[text()='Edit Account']").click()  # click hyperlink Edit Account
        driver.find_element_by_xpath("//input[@name='accountno']").send_keys(accID)  # paste account IT
        driver.find_element_by_xpath("//input[@name='AccSubmit']").click()  # click submit
        # time.sleep(20)

        # trong trang Edit Account
        # option1
        driver.find_element_by_xpath("//select[@name='a_type']/option[text()='Current']").click()  # drop down list
        time.sleep(10)
        driver.find_element_by_xpath("//input[@name='AccSubmit']").click()  # click submit

        # verify Edit account successful

        try:
            verify_editNewID = driver.find_element_by_xpath("//p[text()='Account details updated Successfully!!!']").text
            assert verify_editNewID == "Account details updated Successfully!!!"
        except:
            print("failed")






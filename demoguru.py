from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
import string

class Testsample():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome("/Users/tminht/PycharmProjects/FiistSeleniumTest/drivers/chromedriver")
        driver.get("http://demo.guru99.com/V4/")
        yield
        driver.close()
        driver.quit()
        print("Test completed")


    # def randomString(nhap_so_kitu):
    #   global emailLogin
    #  letters = string.ascii_lowercase
    # return ''.join(random.choice(letters) for i in range(nhap_so_kitu))
    # emailLogin = randomString(10)

    def test_1(self,test_setup):
        driver.find_element_by_xpath("//a[text()='here']").click()
        driver.find_element_by_xpath("//input[@name='emailid']").send_keys("thong123@test.com")
        driver.find_element_by_xpath("//input[@name='emailid']").send_keys(Keys.ENTER)
        userID = driver.find_element_by_xpath("//td[text()='User ID :']//following-sibling::td").text
        passWord = driver.find_element_by_xpath("//td[text()='Password :']//following-sibling::td").text
        driver.back()
        driver.back()
        print("UserID= " + userID)
        print("Password= " + passWord)
        driver.find_element_by_xpath("//input[@name='uid']").send_keys(userID)
        driver.find_element_by_xpath("//input[@name='password']").send_keys(passWord)
        driver.find_element_by_xpath("//input[@name='btnLogin']").click()
        driver.find_element_by_xpath("//a[text()='New Customer']").click()
        driver.find_element_by_xpath("//input[@name='name']").send_keys("Thong")
        driver.find_element_by_xpath("//input[@value='m']").click()
        driver.find_element_by_xpath("//textarea[@name='addr']").send_keys("tang bat Ho Q5")
        driver.find_element_by_xpath("//input[@name='city']").send_keys("Ho Chi Minh City")
      #  driver.find_element_by_xpath("//input[@name='emailid']").send_keys("testttt@gsda.com")
        #  driver.find_element_by_xpath("//input[@name='password']").send_keys(password_SignUp)

        start_date = driver.find_element_by_xpath("//input[@name='dob']")
        start_date.clear()
        start_date.send_keys("08/08/1990")
        driver.find_element_by_xpath("//input[@name='dob']")

        driver.find_element_by_xpath("//input[@name='state']").send_keys("Ho chi minh")
        driver.find_element_by_xpath("//input[@name='pinno']").send_keys("123456")
        driver.find_element_by_xpath("//input[@name='telephoneno']").send_keys("0988845885")

        driver.find_element_by_xpath("//input[@value='Submit']").click()

        # verify login success


    # actual_UserID_Text = driver.find_element_by_xpath("//td[text()='Manger Id : " + userID + "\']").text
    # print(actual_UserID_Text)

    # assert_equal(actual_UserID_Text, "Manger Id : " + userID)

    def test_2(self):


        # verify add new customer thành công
        verify_NewCS = driver.find_element_by_xpath("//p[text()='Customer Registered Successfully!!!']").text
        if (verify_NewCS == "Customer Registered Successfully!!!"):
            print("Tạo mới thành công")
        else:
            print("Failed")

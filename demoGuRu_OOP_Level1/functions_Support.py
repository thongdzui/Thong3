import random
import string


class common_func():
    global driver
    def sendkey(self, xpathName, value):
        driver.find_element_by_xpath(xpathName).send_key(value)


    def click(self, xpathName):
        driver.find_element_by_xpath(xpathName).click()


    def clear(self, xpathName):
        driver.find_element_by_xpath(xpathName).clear()


    def assertNewCS(self):
        driver.find_element_by_xpath("//p[text()='Customer Registered Successfully!!!']").text


    def randomStr(self, nhap_so_kitu):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(nhap_so_kitu))


    def randomNum(self, nhapSoLuongNumberVaoDiAThongAhihi):
        nums = string.digits
        return ''.join(random.choice(nums) for i in range(nhapSoLuongNumberVaoDiAThongAhihi))


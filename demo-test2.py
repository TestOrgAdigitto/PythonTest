import sys
import unittest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# print ("Enter your github userName")
# userName = sys.argv[1]
# print ("Enter your gihub password")
# userName = sys.argv[2]

class loginTest(unittest.TestCase):
	
	def test_permissions(self):
		driver = webdriver.Chrome()
		#WebDriverWait(driver, 60)

		driver.get("https://github.com/login")
		#WebDriverWait(driver, 60)
		userName = driver.find_element_by_id("login_field")
		password = driver.find_element_by_id("password")
		userName.send_keys("spongebob02")
		password.send_keys("Paparazzi@18")
		driver.find_element_by_name('commit').click()
		#wait = WebDriverWait(driver, 60)
		driver.get("https://jenkins-deployment-dev-dev.cloud.rvapps.io/")
		#wait = WebDriverWait(driver, 60)
		driver.get("https://jenkins-deployment-dev-dev.cloud.rvapps.io/manage")
		assert not len(driver.find_element_by_xpath("//h1[contains(text(),'Access Denied')]"))	
	



if __name__ == "__main__":
	unittest.main()

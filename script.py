from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
driver=webdriver.Firefox()
driver.get("http://www.way2sms.com/")

element = driver.find_element_by_name("mobileNo").send_keys("8906713946")
element = driver.find_element_by_name("password").send_keys("loralassan")


submit_button = driver.find_elements_by_xpath('/html/body/div[6]/div[2]/div/div[3]/form/div[2]/div[2]/button')[0]
submit_button.click()

driver.implicitly_wait(10)

#submit_button = driver.find_elements_by_xpath('//*[@id="mobile"]')[0].send_keys("8906713946")
print element
#element = driver.find_element_by_name("message").send_keys("loralassannnn")

submit_button = driver.find_elements_by_xpath('//*[@id="sendButton"]')[0].click()
driver.implicitly_wait(10)

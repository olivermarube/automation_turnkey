import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options


#Launch the web browser
driver = webdriver.Firefox()

#command will fetch the url provided

driver.get("https://turnkey.arifu.com/")

print("browser successfully opened")

driver.maximize_window()
##Browser maximization

#Verify sign in element
element = driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]/div[1]/h3/span")
print(element.is_displayed())

#verify email field

element = driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]/div[2]/form/fieldset/div[1]/div/input")
print(element.is_displayed())

#Verify password field

element = driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]/div[2]/form/fieldset/div[2]/div/input")
print(element.is_displayed())

#verify sign in button
element = driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]/div[2]/form/fieldset/div[3]")
time.sleep(3)
print(element.is_displayed())

#verify arifu logo is displayed

element = driver.find_element_by_xpath("/html/body/div/div/div/div/div[1]/a/img")
time.sleep(3)
print(element.is_displayed())
#time.sleep(5)

#Log in with valid credentials
driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]/div[2]/form/fieldset/div[1]/div/input").send_keys("olly@arifu.com")
time.sleep(3)
print("username successfully added")
##time.sleep(5)
##.send.key is for entering text into a text field
driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]/div[2]/form/fieldset/div[2]/div/input").send_keys("4r1fuD3fault")
time.sleep(3)
print("password successfully added")

##.click() functionality is a command for the action click
driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]/div[2]/form/fieldset/div[3]/button/span[1]/span").click()
time.sleep(3)
driver.quit()





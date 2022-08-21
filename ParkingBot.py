import time
from time import sleep
from unittest import mock 
from selenium import webdriver as wb
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

starttime = time.time() # to track how much time the code takes

driver = wb.Firefox() # initialize driver

# USER DATA
property = "PROPERTYNAME" # Must be a unique identifier for your property or full property name
aptnum = "APARTMENTNUMBER"
make = "CARMAKE"
model = "CARMODEL"
lp = "LICENCEPLATENUMBER"
ConfirmLP = lp
email = "EMAIL@gmail.com"

# START OF DRIVER 
driver.get("https://www.register2park.com/")                               
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div/a").click() 

# ENTER PROPERTY NAME
driver.find_element(By.ID,"propertyName").send_keys(property)
time.sleep(.5)             
driver.find_element(By.ID,"confirmProperty").click()  

# SELECT MATCHING PROPERTY
propertyList = driver.find_elements(By.CSS_SELECTOR, "div[class^='property radio']")  # Create list of all property results
for i in range(len(propertyList)):
    proptext = propertyList[i].text
    if proptext.find(property) >=0:
        wait = WebDriverWait(driver, 10)
        radio = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[class^='property']")))
        time.sleep(.5)
        radio.click()
driver.find_element(By.ID,"confirmPropertySelection").click()  

# SELECT VISITOR PARKING
driver.find_element(By.ID,"registrationTypeVisitor").click()  
time.sleep(.5)

# INPUT VEHICLE INFORMATION
driver.find_element(By.ID,"vehicleApt").send_keys(aptnum)
driver.find_element(By.ID,"vehicleMake").send_keys(make)
driver.find_element(By.ID,"vehicleModel").send_keys(model)
driver.find_element(By.ID,"vehicleLicensePlate").send_keys(lp)
driver.find_element(By.ID,"vehicleLicensePlateConfirm").send_keys(ConfirmLP)
    
# driver.find_element(By.ID,"vehicleInformation").click()  

time.sleep(5)
driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
# driver.minimize_window()
# ip_add=input("Enter the IP address: ")
driver.maximize_window()
ip_add="192.168.1.1"
driver.get("http://"+ip_add+"/")

# user=input("Enter the username: ")
user="admin"
# password=input("Enter the password: ")
password="admin"

driver.find_element(By.XPATH, "//*[@id='Frm_Username']").send_keys(user)
driver.find_element(By.XPATH, "//*[@id='Frm_Password']").send_keys(password)

driver.find_element(By.XPATH,"//*[@id='LoginId']").click()

time.sleep(3)

driver.find_element(By.XPATH, '//*[@id="internet"]').click()

time.sleep(3)

driver.find_element(By.XPATH, '//*[@id="security"]').click()

time.sleep(3)

driver.find_element(By.XPATH, '//*[@id="portForwarding"]').click()
time.sleep(3)

print("1. Add a new port forwarding rule")
print("2. Delete a port forwarding rule")
choice=input("Enter the choice: ")

if(choice=="1"):

    # adding new port forwarding rule
    driver.find_element(By.XPATH, '//*[@id="addInstBar_PortForwarding"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="Alias:2"]').send_keys("test")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="Protocol:2"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="Protocol:2"]/option[3]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="S_Interface:2"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="S_Interface:2"]/option[2]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="S_Interface:2"]/option[2]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="InternalClient:2"]').send_keys("192.168.1.121")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="ExternalPort:2"]').send_keys("8080")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="ExternalPortEndRange:2"]').send_keys("8080")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="InternalPort:2"]').send_keys("8080")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="InternalPortEndRange:2"]').send_keys("8080")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="Btn_apply_PortForwarding:2"]').click()
    time.sleep(3)
else:
    # //*[@id="instDelete_PortForwarding:1"]
    driver.find_element(By.XPATH, '//*[@id="instDelete_PortForwarding:2"]').click()
    time.sleep(3)



time.sleep(3)

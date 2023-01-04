from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
import pytest
import time
#Locators
WEBPAGE_BASEURL = "https://www.trendyol.com/giris"
EMAIL_TEXTAREA = "login-email"
PASSWORD_TEXTAREA = "login-password-input"
TEST_USERNAME = "please write a valid email address"
TEST_PASSWORD = "the password for the corresponding order is defined."
LOGIN_BUTTON = ".q-primary > span"

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

def startPage(): # Open Web Page
    driver.get(WEBPAGE_BASEURL)
 
def loginPage():  # Login the page
    #Username
    username = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, EMAIL_TEXTAREA)))
    username.send_keys(TEST_USERNAME)
    #Password 
    password = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, PASSWORD_TEXTAREA)))
    password.send_keys(TEST_PASSWORD)
    #Login
    driver.find_element(By.CSS_SELECTOR, LOGIN_BUTTON).click()
    sleep(3)
def Scenario1():
    login()
    sleep(2)
    WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div/div/input"))).click()
    WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div/div/input"))).send_keys("Oyuncu Bilgisayarı")
    WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div/div/i"))).click()
    #Choose Monster
    WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[2]/div/div/div/div[1]/div[1]/div/div/div[2]/div[3]/div/div/div[1]/div/a/div[2]"))).click()
    sleep(2)
    # Price Selection
    WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[2]/div/div/div/div[1]/div[1]/div/div/div[3]/div[2]/div/input[1]"))).click()
    WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[2]/div/div/div/div[1]/div[1]/div/div/div[3]/div[2]/div/input[1]"))).send_keys(3000)   
    driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[2]/div/div/div/div[1]/div[1]/div/div/div[3]/div[2]/div/input[2]").send_keys(10000)
    sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[2]/div/div/div/div[1]/div[1]/div/div/div[3]/div[2]/div/button").click()
    sleep(2)
    
    #click Sepete Ekle Button
    driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[5]/div[1]/div/div[1]/div[1]/a/div[1]/div[2]/div[2]").click()
    sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".p-card-wrppr:nth-child(1) .image-overlay-body").click()
    #Look the bucket    
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div/div/div[2]/a/p")
    driver.get("https://www.trendyol.com/")
def Scenario2():
     loginPage()  #login page
     WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div/div/input"))).click()
     WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div/div/input"))).send_keys("Gömlek") #search 'gömlek'
     WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div/div/i"))).click()
     WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#container > div:nth-child(5) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1)"))).click() #pop-up closed
     driver.find_element(By.CSS_SELECTOR, "div.p-card-wrppr:nth-child(2) > div:nth-child(2) > i:nth-child(1)").click()
     sleep(2)
     driver.find_element(By.CSS_SELECTOR, "div.p-card-wrppr:nth-child(3) > div:nth-child(2) > i:nth-child(1)").click()
     sleep(2)
     driver.find_element(By.CSS_SELECTOR, "div.p-card-wrppr:nth-child(4) > div:nth-child(2) > i:nth-child(1)").click()
     sleep(2)
     driver.find_element(By.CSS_SELECTOR, "div.p-card-wrppr:nth-child(5) > div:nth-child(2) > i:nth-child(1)").click()
     driver.find_element(By.CSS_SELECTOR, "a.account-nav-item > div:nth-child(1)").click()
     sleep(4)
def Scenario3():
    # The following tab check steps are done using the array and for cycle. It's an alternative.
    # Save the expected URLs of the tabs to a series
    expected_urls = [
    "https://www.trendyol.com/butik/liste/1/kadin",
    "https://www.trendyol.com/butik/liste/2/erkek",
    "https://www.trendyol.com/butik/liste/3/anne--cocuk",
    "https://www.trendyol.com/butik/liste/12/ev--mobilya"
    ]
    # Check the URL for each tab
    for i in range(4):
    # i'inci sekmeyi seçin
     driver.find_element(By.CSS_SELECTOR, f"li.tab-link:nth-child({i+1}) > a:nth-child(1)").click()

    # Check the URL of the tab
    current_url = driver.current_url
    if current_url == expected_urls[i]:
        print(f"The {i+1}th tab is working.")
        sleep(2)
    else:
        print(f"The {i+1}th tab is not working.")
        sleep(2)

    # The following control step is the most basic control.to run this code, convert the top block to the annotation line.
    loginPage()  #login page
    #Kadin Section Control
    driver.find_element(By.CSS_SELECTOR,"li.tab-link:nth-child(1) > a:nth-child(1)").click()
    expected_url = "https://www.trendyol.com/butik/liste/1/kadin" 
    current_url = driver.current_url
    if current_url == expected_url:
        print("the women's tab is working.")
    else:
        print(" the women's tab is not working.!")
    #Erkek Section Control
    driver.find_element(By.CSS_SELECTOR,"li.tab-link:nth-child(2) > a:nth-child(1)").click()
    expected_url = "https://www.trendyol.com/butik/liste/2/erkek" 
    current_url = driver.current_url
    if current_url == expected_url:
        print(" The man's tab is working!")
    else:
        print(" The man's tab is not working!")
    #Anne&Çocuk Section Control
    driver.find_element(By.CSS_SELECTOR,"li.tab-link:nth-child(3) > a:nth-child(1)").click()
    expected_url = "https://www.trendyol.com/butik/liste/3/anne--cocuk" 
    current_url = driver.current_url
    if current_url == expected_url:
        print(" Woman & Child Tab is working.")
    else:
        print(" Woman & Child Tab is not working.")
    #Ev&Mobilya Section Control
    driver.find_element(By.CSS_SELECTOR,"li.tab-link:nth-child(4) > a:nth-child(1)").click()
    expected_url = "https://www.trendyol.com/butik/liste/12/ev--mobilya" 
    current_url = driver.current_url
    if current_url == expected_url:
        print(" Home & Furniture tab is working.")
    else:
        print(" Home & Furniture tab is not working!")
sleep(4)
startPage()
# Scenario1()
# Scenario2()
# Scenario3()

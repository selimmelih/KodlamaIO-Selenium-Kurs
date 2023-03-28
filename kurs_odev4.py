from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class Odev4:
    def bosGiris(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        #kullaniciAdi
        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(1)
        usernameInput.send_keys("")
        passwordInput.send_keys("")
        loginButton = driver.find_element(By.ID, "login-button")
        sleep(1)
        #passwordInput.click()
        #girisKismi
        loginButton.click()
        #hataMesaji
        errorMessage = driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
        testResult = errorMessage.text == "Epic sadface: Username is required"
        print(errorMessage.text)
        print(f"Test Sonucu: {testResult}")



    def bosSifre(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        # kullaniciAdi
        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(1)
        usernameInput.send_keys("standart_user","locked_out_user","problem_user","performance_glitch_user")
        passwordInput.send_keys("")
        loginButton = driver.find_element(By.ID, "login-button")
        sleep(1)
        # passwordInput.click()
        # girisKismi
        loginButton.click()
        # hataMesaji
        errorMessage = driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
        testResult = errorMessage.text == "Epic sadface: Password is required"
        print(errorMessage.text)
        print(f"Test Sonucu: {testResult}")



    def locked_out(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        # kullaniciAdi
        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(1)
        usernameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        loginButton = driver.find_element(By.ID, "login-button")
        sleep(1)
        loginButton.click()
        errorMessage = driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(errorMessage.text)
        print(f"Test Sonucu: {testResult}")




    def x_ikon_kapat(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        loginButton = driver.find_element(By.ID, "login-button")
        loginButton.click()
        sleep(1)
        errorButton = driver.find_element(By.CLASS_NAME, "error-button")
        errorButton.click()
        sleep(1)



    def standard_user(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(1)
        usernameInput.send_keys("standard_user" )
        passwordInput.send_keys("secret_sauce")
        sleep(1)
        loginButton = driver.find_element(By.ID, "login-button")
        loginButton.click()
        sleep(5)



    def urun_goster(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(1)
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        sleep(1)
        loginButton = driver.find_element(By.ID, "login-button")
        loginButton.click()
        sleep(5)

        listOfEnvanter = driver.find_element(By.CLASS_NAME, "inventory_item")
        print(f" INVENTORY ITEMS NUMBER: {len(listOfEnvanter)}")



odev4s = Odev4()
odev4s.standard_user()

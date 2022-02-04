from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_id = "email"
    textbox_password_id = "password"
    button_login_xpath = "/html/body/div/div/div/div/div/div/form/div[4]/div/button"
    link_forgetpassword_xpath = "(//a[normalize-space()='Forgot password?'])[1]"
    button_admindd_xpath = "(//span[@class='ml-1 nav-user-name hidden-sm'])[1]"
    button_logout_xpath = "(//a[normalize-space()='Logout'])[1]"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickForgetpassword(self):
        self.driver.find_element(By.XPATH, self.link_forgetpassword_xpath).click()

    def clickAdminDD(self):
        self.driver.find_element(By.XPATH, self.button_admindd_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.button_logout_xpath).click()

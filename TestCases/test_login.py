from PageObjects.LoginPage import LoginPage
from Utilities.ReadProperties import ReadConfig
from Utilities.CustomLogger import LogGen


class Test_001_Login:
    BaseURL = ReadConfig.getApplicationURL()
    Username = ReadConfig.getUsername()
    Password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_LoginPageTitle(self, setup):
        self.logger.info("****************Test_001_Login***************")
        self.logger.info("****************Verify_LoginPageTitle***************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.BaseURL)
        actual_title = self.driver.title
        if actual_title == "Login - TMS":
            assert True
            self.driver.close()
            self.logger.info("****************Title Test Case Passed***************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_LoginPageTitle.png")
            self.driver.close()
            self.logger.info("****************Title Test Case Failed***************")
            assert False

    def test_login(self, setup):
        self.logger.info("****************test_Login***************")
        self.logger.info("****************Verify Login in to Application***************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.BaseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.Username)
        self.lp.setPassword(self.Password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard - TMS":
            assert True
            self.driver.close()
            self.logger.info("****************Login Application Test Case Passed***************")

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.info("****************Login Application Test Case Failed***************")
            assert False

    def test_forgetpassword_link(self, setup):
        self.logger.info("****************test_forgetpassword_link***************")
        self.logger.info("****************Verify Forgetpassword Funcationality***************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.BaseURL)
        self.lp = LoginPage(self.driver)
        self.lp.clickForgetpassword()
        act_title = self.driver.title
        if act_title == "Forgot Password - TMS":
            assert True
            self.driver.close()
            self.logger.info("****************Forget Password Test Case Passed***************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_forgetpassword_link.png")
            self.driver.close()
            self.logger.info("****************Forget Password Test Case Failed***************")
            assert False

    def test_logout(self, setup):
        self.logger.info("****************test_logout***************")
        self.logger.info("****************Verify Application Logout Functionality***************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.BaseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.Username)
        self.lp.setPassword(self.Password)
        self.lp.clickLogin()
        self.lp.clickAdminDD()
        self.lp.clickLogout()
        act_title = self.driver.title
        if act_title == "Login - TMS":
            assert True
            self.driver.close()
            self.logger.info("****************Logout Functionality Test Case Passed***************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_logout.png")
            self.driver.close()
            self.logger.info("****************Logout Functionality Test Case Failed***************")
            assert False

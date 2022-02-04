import time

from PageObjects.LoginPage import LoginPage
from Utilities.ReadProperties import ReadConfig
from Utilities.CustomLogger import LogGen
from Utilities import XlUtils


class Test_002_DDT_Login:
    BaseURL = ReadConfig.getApplicationURL()
    path = ".//TestData//LoginData.xlsx"
    logger = LogGen.loggen()

    def test_login_ddt(self, setup):
        self.logger.info("****************Test_002_DDT_Login***************")
        self.logger.info("****************Verify Login DDT in to Application***************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.BaseURL)
        self.lp = LoginPage(self.driver)

        self.rows = XlUtils.getRowCount(self.path, 'Sheet1')
        print("Number of Row in Excel file: ", self.rows)
        lst_status = []

        for r in range(2, self.rows + 1):
            self.user = XlUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XlUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XlUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUsername(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard - TMS"

            if act_title == exp_title:
                if self.exp == 'Pass':
                    self.logger.info("**** passed ****")
                    self.lp.clickAdminDD()
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == 'Fail':
                    self.logger.info("**** failed ****")
                    self.lp.clickAdminDD()
                    self.lp.clickLogout()
                    lst_status.append("Fail")

            elif act_title != exp_title:
                if self.exp == 'Pass':
                    self.logger.info("**** failed ****")
                    lst_status.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info("**** passed ****")
                    lst_status.append("Pass")
            print(lst_status)
        if "Fail" not in lst_status:
            self.logger.info("******* DDT Login test passed **********")
            self.driver.close()
            assert True
        else:
            self.logger.error("******* DDT Login test failed **********")
            self.driver.close()
            assert False

        self.logger.info("******* End of Login DDT Test **********")
        self.logger.info("**************** Completed  TC_LoginDDT_002 ************* ")

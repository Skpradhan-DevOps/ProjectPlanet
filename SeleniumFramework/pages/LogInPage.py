from SeleniumFramework.base.BaseClass import BaseClass
from SeleniumFramework.utilities import CustomLogger as cl


class Login(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _userName = "idp-discovery-username"  # id
    _passWord = "okta-signin-password"  # id
    _userNameSubmit = "idp-discovery-submit"
    _signInSubmit = "okta-signin-submit"
    _skip = "//button[@data-qe='skip-tour-button']"

    def enterUserName(self):
        self.sendText("takehometest@qe.com", self._userName, "id")
        cl.allureLogs("Entered UserName")

    def clickUserSubmit(self):
        self.clickOnElement(self._userNameSubmit, "id")
        cl.allureLogs("Clicked on submit after Username provided")

    def enterPassWord(self):
        self.sendText("Password123#", self._passWord, "id")
        cl.allureLogs("Entered Password")

    def clickSignInSubmit(self):
        self.clickOnElement(self._signInSubmit, "id")
        cl.allureLogs("Clicked on submit to sign in")

    def clickToSkip(self):
        self.clickOnElement(self._skip, "xpath")
        cl.allureLogs("Clicked on Skip to go over the Pop-up")

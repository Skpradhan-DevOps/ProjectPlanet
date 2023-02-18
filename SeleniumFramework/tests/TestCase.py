import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common import keys

from SeleniumFramework.base.DriverClass import WebDriverClass
from SeleniumFramework.utilities import CustomLogger as cl
from SeleniumFramework.base.BaseClass import BaseClass
from SeleniumFramework.pages.LogInPage import Login
from SeleniumFramework.pages.SaveSearch import SaveSearch

wd = WebDriverClass()
driver = wd.getWebDriver("chrome")

bc = BaseClass(driver)
login = Login(driver)
save = SaveSearch(driver)
bc.launchWebPage("https://www.planet.com/explorer")

login.enterUserName()
login.clickUserSubmit()
login.enterPassWord()
login.clickSignInSubmit()
login.clickToSkip()

save.sendSearchLocation()
save.selectLocation()
save.searchSave1()
save.searchSave2()
save.saveSearchLink()
save.checkSaveSearch()
save.updateSavedSearch()
save.saveSearchLink()
save.checkUpdateSearch()


time.sleep(3)
driver.quit()

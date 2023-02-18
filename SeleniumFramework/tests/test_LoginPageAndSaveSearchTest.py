import time
import unittest
import pytest
from SeleniumFramework.base.BaseClass import BaseClass
from SeleniumFramework.pages.LogInPage import Login
from SeleniumFramework.pages.SaveSearch import SaveSearch
from SeleniumFramework.utilities import CustomLogger as cl


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class LogInAndSaveSearchTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.lg = Login(self.driver)
        self.sv = SaveSearch(self.driver)
        self.bp = BaseClass(self.driver)

    @pytest.mark.run(order=1)
    def test_userName(self):
        self.lg.enterUserName()
        self.lg.clickUserSubmit()


    @pytest.mark.run(order=2)
    def test_passAndLogin(self):
        self.lg.enterPassWord()
        self.lg.clickSignInSubmit()
        self.lg.clickToSkip()


    @pytest.mark.run(order=3)
    def test_saveSearch1(self):
        self.sv.sendSearchLocation()
        self.sv.selectLocation()
        self.sv.searchSave1()

    @pytest.mark.run(order=4)
    def test_saveSearch2(self):
        self.sv.searchSave2()
        self.sv.saveSearchLink()
        self.sv.checkSaveSearch()

    @pytest.mark.run(order=5)
    def test_saveSearch2(self):
        self.sv.updateSavedSearch()
        self.sv.saveSearchLink()
        self.sv.checkUpdateSearch()

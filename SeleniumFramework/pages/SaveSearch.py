import time

from SeleniumFramework.base.BaseClass import BaseClass
from SeleniumFramework.utilities import CustomLogger as cl


class SaveSearch(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _searchLocation = "//input[@placeholder='Search for a Location']"
    _afterSearchDropdown = "//span[normalize-space()='San Francisco']"
    _saveSearch1 = "//button[@data-qe='click-save-search-button']"
    _saveSearchNameBox = "//label[contains(text(),'Name')]/following-sibling::div/child::input"
    _saveSearch2 = "//button[@data-cy='dialog-save-search-button']"
    _saveSearchLink = "//button[@value='saved-searches-drawer']//*[name()='svg']"
    _searchResultsBox = "//input[@placeholder='Filter by name']"
    _searchResultList = "//h6[@data-qe='search-list-item-title']"
    _updateSearchButton = "//button[contains(text(),'Update search')]"
    _updateSearch2 = "//button[contains(text(), 'Save as new search')]/following-sibling::button"

    def sendSearchLocation(self):
        self.clickOnElement(self._searchLocation, "xpath")
        cl.allureLogs("Clicked on the text box to search location")
        self.sendTextActions("San Francisco")
        time.sleep(2)
        cl.allureLogs("Location is sent into the search location box")

    def selectLocation(self):
        self.clickOnElement(self._afterSearchDropdown, "xpath")
        time.sleep(2)
        cl.allureLogs("Clicked on the searched location in drop down")

    def searchSave1(self):
        self.clickOnElement(self._saveSearch1, "xpath")

        time.sleep(3)
        cl.allureLogs("Clicked on the Save Search button 1st Time")

    def searchSave2(self):
        global saveName, ele1
        saveName = self.randomName()
        ele1 = self.waitForElement(self._saveSearchNameBox, "xpath")
        cl.allureLogs("Found out the Text Box to rename and save the search")
        time.sleep(2)
        self.clearText(ele1)
        cl.allureLogs("Cleared the text box to enter an Unique name")
        self.driver.execute_script("arguments[0].click();", ele1)
        cl.allureLogs("Clicked on the Text Box to enter the new name")
        self.sendTextActions("Srikant" + saveName)
        cl.allureLogs("Entered the new name to save the recent search and saved the text")
        self.clickOnElement(self._saveSearch2, "xpath")
        cl.allureLogs("Clicked on the Save Search button 2nd Time")

    def saveSearchLink(self):
        self.clickOnElement(self._saveSearchLink, "xpath")
        cl.allureLogs("Clicked on the Save Search link to check the new save search")

    def checkSaveSearch(self):
        self.sendText("Srikant" + saveName, self._searchResultsBox, "xpath")
        cl.allureLogs("Send the save search name in the result Saved Search Text box")
        ele2 = self.waitForElement(self._searchResultList, "xpath")
        cl.allureLogs("Found out the last saved search in result list")
        self.compareText(ele2.text, "Srikant" + saveName)
        cl.allureLogs("Checked and compared the saved search is in the saved list")

    def updateSavedSearch(self):
        global saveName1, ele3, ele6
        self.clickOnElement(self._searchResultList, "xpath")
        cl.allureLogs("Clicked on the saved search in the saved search result")
        saveName1 = self.randomName()
        #self.clickOnElement(self._updateSearchButton, "xpath")
        ele6 = self.waitForElement(self._updateSearchButton, "xpath")
        self.driver.execute_script("arguments[0].click();", ele6)
        cl.allureLogs("Clicked on the Update search button")
        time.sleep(3)
        ele3 = self.waitForElement(self._saveSearchNameBox, "xpath")
        cl.allureLogs("Found out the Text Box to rename and save the search")
        time.sleep(2)
        self.clearText(ele3)
        cl.allureLogs("Cleared the text box to enter an Unique name")
        self.driver.execute_script("arguments[0].click();", ele3)
        cl.allureLogs("Clicked on the Text Box to enter the new name")
        self.sendTextActions("Srikant-Updated" + saveName1)
        cl.allureLogs("Entered the new name to update the saved search and saved the text")
        #self.clickOnElement(self._updateSearch2, "xpath")
        ele7 = self.waitForElement(self._updateSearch2, "xpath")
        self.driver.execute_script("arguments[0].click();", ele7)
        cl.allureLogs("Clicked on the Update button to update the saved Search")

    def checkUpdateSearch(self):
        ele8 = self.waitForElement(self._searchResultsBox, "xpath")
        time.sleep(2)
        self.clearText(ele8)
        time.sleep(2)
        self.sendText("Srikant-Updated" + saveName1, self._searchResultsBox, "xpath")
        cl.allureLogs("Send the save search name in the result Saved Search Text box")
        ele4 = self.waitForElement(self._searchResultList, "xpath")
        cl.allureLogs("Found out the last saved search in result list")
        self.compareText(ele4.text, "Srikant-Updated" + saveName1)
        cl.allureLogs("Checked and compared the saved search is in the saved list")

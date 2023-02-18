import random
import string
import time
from traceback import print_stack

import allure
from allure_commons.types import AttachmentType
from selenium.common import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from SeleniumFramework.utilities import CustomLogger as cl


class BaseClass:
    log = cl.customLogger()

    def __init__(self, driver):
        self.driver = driver

    def launchWebPage(self, url):
        try:
            self.driver.get(url)
            self.log.info("Web Page Launched with URL : " + url)
        except:
            self.log.info("Web Page not Launched with URL : " + url)

    def getLocatorType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "tag":
            return By.TAG_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        elif locatorType == "plink":
            return By.PARTIAL_LINK_TEXT
        else:
            self.log.error("Locator Type : " + locatorType + " entered is not found")
        return False

    def getWebElement(self, locatorValue, locatorType):
        webElement = None
        try:
            locatorType = locatorType.lower()
            locatorByType = self.getLocatorType(locatorType)
            webElement = self.driver.find_element(locatorByType, locatorValue)
            self.log.info("WebElement found with locator value " + locatorValue + " using locatorType " + locatorByType)
        except:
            self.log.error(
                "WebElement not found with locator value " + locatorValue + " using locatorType " + locatorType)
            print_stack()
            self.takeScreenshot(locatorType)
            assert False
        return webElement

    def waitForElement(self, locatorValue, locatorType):
        webElement = None
        try:
            locatorType = locatorType.lower()
            locatorByType = self.getLocatorType(locatorType)
            wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                                 ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
            webElement = wait.until(ec.presence_of_element_located((locatorByType, locatorValue)))
            self.log.info("WebElement found with locator value " + locatorValue + " using locatorType " + locatorType)
        except:
            self.log.error(
                "WebElement not found with locator value " + locatorValue + " using locatorType " + locatorType)
            print_stack()
            self.takeScreenshot(locatorType)
            assert False
        return webElement

    def clickOnElement(self, locatorValue, locatorType):
        try:
            locatorType = locatorType.lower()
            webElement = self.waitForElement(locatorValue, locatorType)
            webElement.click()
            self.log.info(
                "Clicked on WebElement with locator value " + locatorValue + " using locatorType " + locatorType)
        except:
            self.log.error(
                "Unable to Click on WebElement with locator value " + locatorValue + " using locatorType " + locatorType)
            print_stack()
            self.takeScreenshot(locatorType)
            assert False

    def sendText(self, text, locatorValue, locatorType):
        try:
            locatorType = locatorType.lower()
            webElement = self.waitForElement(locatorValue, locatorType)
            webElement.send_keys(text)
            self.log.info(
                "Sent the text " + text + " in WebElement with locator value " + locatorValue + " using locatorType " + locatorType)
        except:
            self.log.error(
                "Unable to Send the text " + text + " in WebElement with locator value " + locatorValue + "using locatorType " + locatorType)
            print_stack()
            self.takeScreenshot(locatorType)
            assert False

    def scrollTo(self, locatorValue, locatorType):
        actions = ActionChains(self.driver)
        try:
            locatorType = locatorType.lower()
            webElement = self.waitForElement(locatorValue, locatorType)
            actions.move_to_element(webElement).perform()
            self.log.info(
                "Scrolled to WebElement with locator value " + locatorValue + " using locatorType " + locatorType)
        except:
            self.log.error(
                "Unable to scroll to WebElement with locator value " + locatorValue + "using locatorType " + locatorType)
            print_stack()
            self.takeScreenshot(locatorType)
            assert False

    def pressEnter(self):
        actions = ActionChains(self.driver)
        try:
            actions.send_keys(Keys.ENTER)
            actions.perform()
            self.log.info("Press ENTER in whole page ")
        except:
            self.log.error("Unable to press ENTER")
            print_stack()
            assert False

    def randomName(self):
        characters = string.ascii_letters + string.digits
        name = ''.join(random.choice(characters) for i in range(8))
        return name

    def clearText(self, element):
        actions = ActionChains(self.driver)
        try:
            #self.driver.implicitly_wait(3)
            actions.move_to_element(element).double_click().click().send_keys(Keys.BACKSPACE).perform()
            actions.click(element).perform()
            self.log.info("Press BACKSPACE to clear text ")
        except:
            self.log.error("Unable to press BACKSPACE")
            print_stack()
            self.takeScreenshot(element)
            assert False

    def getwebElemnts(self, locatorValue, locatorType ):
        webElements = []
        try:
            locatorType = locatorType.lower()
            locatorByType = self.getLocatorType(locatorType)
            wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                                 ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
            webElements = wait.until(ec.presence_of_element_located((locatorByType, locatorValue)))
            self.log.info("WebElements found with locator value " + locatorValue + " using locatorType " + locatorByType)
        except:
            self.log.error(
                "WebElements not found with locator value " + locatorValue + " using locatorType " + locatorType)
            print_stack()
            self.takeScreenshot(locatorType)
            assert False
        return webElements

    def sendTextActions(self, text):
        actions = ActionChains(self.driver)
        try:
            self.driver.implicitly_wait(5)
            actions.send_keys(text)
            actions.perform()
            self.driver.implicitly_wait(5)
            self.log.info("Send Texts using actions class ")

        except:
            self.log.error("Unable to send texts using action class")
            print_stack()
            self.takeScreenshot(text)
            assert False

    def compareText(self, text1, text2):
        try:
            assert(text1 == text2)
            self.log.info("The created saved Search Name " + text2 + " is correct" )
        except:
            self.log.error("The created saved Search Name " + text2 + " is NOT correct" )
            print_stack()
            assert False

    def takeScreenshot(self, text):
        allure.attach(self.driver.get_screenshot_as_png(), name=text, attachment_type=AttachmentType.PNG)



import pytest
import time
from SeleniumFramework.base.BaseClass import BaseClass
from SeleniumFramework.base.DriverClass import WebDriverClass


@pytest.yield_fixture(scope='class')
def beforeClass(request):
    print("Before Class")
    driver1 = WebDriverClass()
    driver = driver1.getWebDriver("chrome")
    bp = BaseClass(driver)
    bp.launchWebPage("https://www.planet.com/explorer")
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    time.sleep(5)
    driver.quit()
    print("After Class")


@pytest.yield_fixture()
def beforeMethod():
    print("Before Method")
    yield
    print("After Method")

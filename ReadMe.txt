1. TestCase.py file contains all methods to Test the Login and Save Search method
2. test_LoginPageAndSaveSearchTest.py contains pytest framework to test both Log in and Save Search method
3. base folder contains Baseclass and Driver class
4. Pages folder conatins Login Page and SaveSearch py files to explain Page Object Model
5. utilities flder contains custom logger class which contains logging feature and allure report
6. reports are generated in allureReports folder
7. conftest.py file conatins pytest feature with class scope and method scope	

Improvement needed in Framework:
1. Test Data reation
2. Browser details and any platform related things to be placed in configuration files

Other Test scenarios:

1. Other buttons like "Access your Basemaps", "Access your host data for analysis", "view or download past orders", "task a high resolution images" etc can be tested
2. Search similar city names in search box. for example washington city is there multiple states in us
3. Filter, Dates options should be tested
4. Sorted functionality  should be tested
5. Select an image using Drop down features should be tested
6. View details of each image should be tested
7. Zoom, toggle map overlays features should be tested
8. Search Options like Enable Notifications, Create a new folder to save search result should be tested
9. Scroll up/down in every page needs to be tested
10. Delete a saved search feature needs to be tested
11. Show full catalog feature should be tested
12. Collapse side bar should be tested
13. Save as new search in Update feature needs to be tested
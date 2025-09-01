# from appium import webdriver
# from appium.options.android import UiAutomator2Options
# from appium.webdriver.common.appiumby import AppiumBy
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as have
# import time

# options = UiAutomator2Options().load_capabilities(
#     {
#         # Specify device and os_version for testing
#         # "platformName": "android",
#         "platformVersion": "9.0",
#         "deviceName": "Google Pixel 3",
#         # Set URL of the application under test
#         "app": "bs://b64d31a50e9f6405e32e18d21a127e12fc4c0dd6",
#         # Set other BrowserStack capabilities
#         "bstack:options": {
#             "projectName": "First Python project",
#             "buildName": "browserstack-build-2",
#             "sessionName": "BStack first_test",
#             # Set your access credentials
#             "userName": "germangrebenyuk_oPzvKO",
#             "accessKey": "dEHs1RB2raa8pKVMHqwz",
#         },
#     }
# )

# driver = webdriver.Remote("https://hub-cloud.browserstack.com/wd/hub", options=options)

# search_element = WebDriverWait(driver, 30).until(
#     have.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia"))
# )
# search_element.click()

# search_input = WebDriverWait(driver, 30).until(
#     have.element_to_be_clickable(
#         (AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")
#     )
# )
# search_input.send_keys("BrowserStack")
# time.sleep(5)
# search_results = driver.find_elements(
#     AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title"
# )
# assert len(search_results) > 0

# # Invoke driver.quit() after the test is done to indicate that the test is completed.
# driver.quit()

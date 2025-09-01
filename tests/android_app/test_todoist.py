# from allure_commons._allure import step
# from appium.webdriver.common.appiumby import AppiumBy
# from selene import browser, be


# def test_search(mobile_management2):
#     with step("Type search"):
#         browser.element((AppiumBy.ID, "com.todoist:id/btn_email")).click()
#         browser.element((AppiumBy.ID, "com.todoist:id/email_login")).click()
#         browser.element(
#             (AppiumBy.XPATH, '//android.widget.EditText[@resource-id="email"]')
#         ).click()
#         browser.element(
#             (AppiumBy.XPATH, '//android.widget.EditText[@resource-id="email"]')
#         ).type("german.grebeniuk.ed@gmail.com")
#         browser.element(
#             (AppiumBy.XPATH, '//android.widget.EditText[@resource-id="password"]')
#         ).type("test1234")
#         browser.element(
#             (AppiumBy.XPATH, '//android.widget.TextView[@text="Log in"]')
#         ).click()

#     with step("Verify content found"):
#         browser.element((AppiumBy.ID, "android:id/button3")).click()
#         browser.element((AppiumBy.ID, "com.todoist:id/fab")).should(be.visible)

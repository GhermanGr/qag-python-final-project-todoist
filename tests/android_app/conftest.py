import pytest
from appium.options.android import UiAutomator2Options
from selene import browser
import os

from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = UiAutomator2Options().load_capabilities({
        "platformName": "Android",
        "appium:automationName": "UiAutomator2",
        "appium:app": "/Users/alfa/Downloads/com.todoist_v11474-11474_minAPI24(nodpi)_apkmirror.com.apk",
        "appium:appPackage": "com.todoist",
        "appium:appActivity": ".alias.HomeActivityDefault",
        "appium:deviceName": "emulator-5554"
        # # Specify device and os_version for testing
        # # "platformName": "android",
        # "platformVersion": "9.0",
        # "deviceName": "Google Pixel 3",
        #
        # # Set URL of the application under test
        # "app": "bs://7fb09f99b17a705b7ab38cffe4fcd26f94b99597",
        #
        # # Set other BrowserStack capabilities
        # 'bstack:options': {
        #     "projectName": "First Python project",
        #     "buildName": "browserstack-build-1",
        #     "sessionName": "BStack first_test",
        #
        #     # Set your access credentials
        #     "userName": "germangrebenyuk_oPzvKO",
        #     "accessKey": "dEHs1RB2raa8pKVMHqwz"
        #}
    })

    # browser.config.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)
    browser.config.driver_remote_url = 'http://127.0.0.1:4723'
    #browser.config.driver_remote_url = 'http://hub.browserstack.com/wd/hub'
    browser.config.driver_options = options

    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    browser.config.driver = webdriver.Remote(
        command_executor=browser.config.driver_remote_url,
        options=browser.config.driver_options
    )

    yield

    browser.quit()

@pytest.fixture(scope='function', autouse=True)
def mobile_management2():
    # Define capabilities for local emulator
    options = UiAutomator2Options().load_capabilities({
        "platformName": "Android",
        "appium:automationName": "UiAutomator2",
        "appium:appPackage": "com.todoist",
        "appium:appActivity": ".alias.HomeActivityDefault",
        "appium:deviceName": "emulator-5554",
        "appium:udid": "emulator-5554",
        "appium:noReset": True,
        "appium:fullReset": False,
        "appium:ensureWebviewsHavePages": True,
        "appium:nativeWebScreenshot": True,
        "appium:newCommandTimeout": 3600,
        "appium:connectHardwareKeyboard": True,
        "appium:uiautomator2ServerInstallTimeout": 60000,
        "appium:uiautomator2ServerLaunchTimeout": 60000,
        "appium:adbExecTimeout": 60000
    })

    # Set Selene configuration for local Appium server
    browser.config.driver_remote_url = 'http://127.0.0.1:4723'  # Local Appium server
    browser.config.driver_options = options
    browser.config.timeout = 10.0  # Set timeout explicitly

    # Initialize the driver
    browser.config.driver = webdriver.Remote(
        command_executor=browser.config.driver_remote_url,
        options=browser.config.driver_options
    )

    yield

    # Clean up
    browser.quit()

def test_search():
    # Example test: Click the email button (adjust ID if needed)
    selene_browser.element((AppiumBy.ID, 'com.todoist:id/btn_email')).click()
    # Add more test steps as needed
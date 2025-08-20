from qag_python_final_project_todoist.web_model.pages.landing_page import LandingPage
from qag_python_final_project_todoist.web_model.pages.login_page import LoginPage
from qag_python_final_project_todoist.web_model.pages.today_page import TodayPage

class Application():
    def __init__(self):
        self.landing_page = LandingPage()
        self.login_page = LoginPage()
        self.today_page = TodayPage()

app = Application()
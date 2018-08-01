from selene import browser
from selene.support import by
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select


class BasePage:
    def click(self, css_selector):
        browser.element(css_selector).click()
        return self

    def set_value(self, css_selector, value):
        browser.element(css_selector).set_value(value)
        return self

    def accept_alert(self):
        browser.driver().switch_to.alert.accept()
        return self

    def is_alert_present(self):
        try:
            self.switch_to_alert()
            return True
        except NoAlertPresentException:
            return False

    def dismiss_alert(self):
        browser.driver().switch_to.alert.dismiss()
        return self

    def switch_to_alert(self):
        return browser.driver().switch_to.alert

    def home_page(self):
        from e2etests.pages.home_page import HomePage
        return HomePage()

    def login_page(self):
        from e2etests.pages.login_page import LoginPage
        return LoginPage()

    def view_profile_page(self):
        from e2etests.pages.view_profile_page import ViewProfilePage
        return ViewProfilePage()

    def task_detail_page(self):
        from e2etests.pages.task_detail_page import TaskDetailPage
        return TaskDetailPage()

    def create_task_page(self):
        from e2etests.pages.create_task_page import CreateTaskPage
        return CreateTaskPage()

    def edit_pofile_page(self):
        from e2etests.pages.edit_profile_page import EditProfilePage
        return EditProfilePage()

    def change_password_page(self):
        from e2etests.pages.change_password_page import ChangePasswordPage
        return ChangePasswordPage()

    def edit_task_page(self):
        from e2etests.pages.edit_task_page import EditTaskPage
        return EditTaskPage()

    def select(self, css_selector, value):
        Select(browser.element(css_selector)).select_by_visible_text(value)
        return self

    def get_value(self, css_selector):
        return browser.element(css_selector).get_attribute('value')

    def get_first_selected_option(self, css_selector):
        return Select(browser.element(css_selector)).first_selected_option.text

    def send_keys(self, css_selector, value):
        browser.element(css_selector).send_keys(value)
        return self

    def read_text(self, css_selector):
        return browser.element(css_selector).text

    def click_by_xpath(self, xpath, value):
        browser.element(by.xpath(xpath.format(value))).click()
        return self

    def read_texts(self, css_selector):
        return [e.text for e in browser.elements(css_selector)]

    def get_elements_count(self, css_selector):
        return browser.elements(css_selector).size()

    def move_to_element(self, css_selector):
        element = browser.element(css_selector)
        ActionChains(browser.driver()).move_to_element(element.get_actual_webelement()).perform()
        return self

    def is_element_displayed(self, css_selector):
        return browser.element(css_selector).is_displayed()

    @staticmethod
    def load_relative_url(path):
        browser.open_url(path)

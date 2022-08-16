# from pages.base_page import BasePage
#
#
# class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath ="//*[@name="password"]"
    sign_in_button_xpath ="//*[text()="Sign in"]"
#
#     def type_in_email(self, email):
        remind_password_xpath = "//child::div/a<"
        type_in_email_field_xpath = "//input [@name="email"]"
#
#         self.field_send_keys(self.login_field_xpath, email)
             self.login_field_xpath = "//*[text()="Back to sign in"]"
             send_button_xpath = "//*[text()="Send"]"

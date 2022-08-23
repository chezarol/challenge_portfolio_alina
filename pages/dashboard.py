import time

from pages.base_page import BasePage


class Dashboard (BasePage):
    main_page_button_xpath = "//*[text()='Main page']"
    players_button_xpath = "//*[text()='Players']"
    language_button_xpath = "//span [text()='Polski']"
    sign_out_button_xpath = "//span [text()='Sign out']"
    add_player_button_xpath = "//span [text()='Add player']"
    logo_scouts_panel_xpath = "//div[starts-with(@style,'background')]"
    tester_tester_hyperlink_xpath = "//a[2]"
    test_testowy_hyperlink_xpath = "//a[3]"
    main_page_players_padding_xpath = "//ul[1]"
    events_count_padding_xpath = "//*[@id='__next']/div[1]/main/div[2]/div[4]/div/div[1]/.."
    test_name_test_surname_hyperlink_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[1]/button/.."
    expected_title = "Scouts panel"
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/en'

    def title_of_page(self):
        time.sleep(5)
        assert self.get_page_title(self.dashboard_url) == self.expected_title
    pass

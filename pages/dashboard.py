from pages.base_page import BasePage


class Dashboard (BasePage):
    main_page_button_xpath = "//*[text()="Main page"]"
    players_button_xpath = "//*[text()="Players"]"
    language_button_xpath = "//span [text()="Polski"]"
    sign_out_button_xpath = "//span [text()="Sign out"]"
    add_player_button_xpath = "//span [text()="Add player"]"
    
    pass
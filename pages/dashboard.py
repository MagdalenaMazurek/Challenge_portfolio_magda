import time
from lib2to3.pgen2 import driver

from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class Dashboard(BasePage):
    futbol_kolektyw_button_xpath = "//*[@title='Logo Scouts Panel']"
    expected_title = "Scouts panel"
    dashboard_url = 'https:scouts-test.futbolkolektyw.pl/'
    Scouts_Panel = "//*[text()='Main page']"
    Players = "//*[text()='Players']"
    Polski = "//*[text()='Polski']"
    Sign_out = "//*[text()='Sign out']"
    PlayersCount = "//*[text()='Players count']"
    Last_created_player = "//*[text()='Last created player']"
    Last_updated_player = "//*[text()='Last updated player']"
    Last_created_match = "//*[text()='Last created match']"
    Last_updated_match = "//*[text()='Last updated match']"
    Last_updated_report = "//*[text()='Last updated report']"
    add_player_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"
    wait = WebDriverWait(driver, 10)
    add_language_button_xpath = "/html/body/div/div[1]/main/div[2]/form/div[2]/div/div[15]/button/span[1]"

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.futbol_kolektyw_button_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def click_add_player_button(self):
        self.click_on_the_element(self.add_player_button_xpath)

    def click_Sign_out(self):
        self.click_on_the_element(self.Sign_out)
        pass


pass
import time
from pages.base_page import BasePage


class Dashboard(BasePage):
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

    def title_of_page(self):
        time.sleep(4)
        assert self.get_page_title(self.dashboard_url) == self.expected_title
pass
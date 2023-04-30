import os
import time
import unittest
from selenium import webdriver

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from pages.add_a_player import AddAPlayer

from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service


class TestAddaPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_a_Player(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user07@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_sing_in_button()
        time.sleep(5)
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_add_player_button()
        time.sleep(5)
        add_player = AddAPlayer(self.driver)
        add_player.title_of_page()
        add_player.type_in_email('testowyemal@gmai.cim')
        add_player.type_in_name('Bartosz')
        add_player.type_in_surname('Rogala')
        add_player.type_in_age('22')
        add_player.type_in_main_position('Striker')
        add_player.click_submit_button()


    @classmethod
    def tearDown(self):
        self.driver.quit()
import time

from pages.base_page import BasePage


class AddAPlayer(BasePage):
    email_field_xpath = "//div[1]/div/div/input"
    name_field_xpath = "//div[2]/div/div/input"
    surname_field_xpath = "//div[3]/div/div/input"
    phone_field_xpath = "//div[4]/div/div/input"
    weight_field_xpath = "//div[5]/div/div/input"
    height_field_xpath = "//div[6]/div/div/input"
    age_field_xpath = "//div[7]/div/div/input"
    leg_listbox_xpath = "//*[@id='mui-component-select-leg']"
    club_field_xpath = "//div[9]/div/div/input"
    level_field_xpath = "//div[10]/div/div/input"
    main_position_field_xpath = "//div[11]/div/div/input"
    second_position_xpath = "//div[12]/div/div/input"
    district_listbox_xpath = "//*[@id='mui-component-select-district']"
    achievements_field_xpath = "//div[14]/div/div/input"
    submit_button_xpath = "//div[3]/button[1]/span[1]"
    add_a_player_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"
    expected_title = 'Add player'
    clear_button_xpath = '/html/body/div/div[1]/main/div[2]/form/div[3]/button[2]/span[1]'

    def type_in_email(self, email):
        self.field_send_keys(self.email_field_xpath, email)

    def type_in_name(self, name):
        self.field_send_keys(self.name_field_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_field_xpath, surname)

    def type_in_phone(self, phone):
        self.field_send_keys(self.phone_field_xpath, phone)

    def type_in_weight(self, weight):
        self.field_send_keys(self.weight_field_xpath, weight)

    def type_in_height(self, height):
        self.field_send_keys(self.height_field_xpath, height)

    def type_in_age(self, age):
        self.field_send_keys(self.age_field_xpath, age)

    def type_in_main_position(self, main_position):
        self.field_send_keys(self.main_position_field_xpath, main_position)

    def click_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)

    def title_of_page(self):
        test_title = self.get_page_title(self.add_a_player_url)
        time.sleep(4)
        assert self.get_page_title(self.add_a_player_url) == self.expected_title

    def type_in_club_field(self, club_field):
        self.field_send_keys(self.club_field_xpath, club_field)
        pass

    def type_in_level_field(self, level_field):
        self.field_send_keys(self.level_field_xpath, level_field)
        pass

    def district_listbox(self, district_listbox):
        self.field_send_keys(self.district_listbox_xpath, district_listbox)
        pass

    def leg_listbox(self, leg_listbox):
        self.field_send_keys(self.leg_listbox_xpath, leg_listbox)
        pass

    def click_clear_button(self):
        self.click_on_the_element(self.clear_button_xpath)
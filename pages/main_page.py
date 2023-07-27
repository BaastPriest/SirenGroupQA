from .base_page import BasePage
from .locators import MainPageLocators, TypeOfProjectLocators, KindOfSiding, SquareFeet, StoriesHouseLocators, Homeowner, FirstLastNameForm, PhoneNumber,ThankYouPage, user_already_exist_db


class MainPageHelper(BasePage):

    def fill_zip_code(self, zip_code_text):
        input_zip_code = self.find_element(MainPageLocators.ZIP_CODE_INPUT)
        input_zip_code.send_keys(zip_code_text)
        return input_zip_code

    def click_on_get_estimate_button(self):
        return self.find_element(MainPageLocators.GET_ESTIMATE_BUTTON, time=2).click()

    def click_on_submit_button_on_question_form(self):
        return self.find_element(TypeOfProjectLocators.LOCATOR_SUBMIT_BUTTON, time=2).click()

    def choose_type_of_project(self):
        return self.find_element(TypeOfProjectLocators.REPLACE_EXISTING_SIDING, time=2).click()

    def choose_kind_of_siding(self):
        return self.find_element(KindOfSiding.VINYL, time=2).click()

    def fill_square_feet(self, fill_text):
        input_square_feet = self.find_element(SquareFeet.INPUT_SIDING_AREA)
        input_square_feet.send_keys(fill_text)
        return input_square_feet

    def select_stories_house(self):
        return self.find_element(StoriesHouseLocators.ONE_STORY, time=2).click()


    def select_homeovner_question(self):
        return self.find_element(Homeowner.YES_HOMEOVNR, time=2).click()


    def fill_first_last_name(self, full_name):
        input_full_name = self.find_element(FirstLastNameForm.FULL_NAME)
        input_full_name.send_keys(full_name)
        return input_full_name

    def fill_email(self, test_email):
        email = self.find_element(FirstLastNameForm.EMAIL)
        email.send_keys(test_email)
        return email

    def fill_phone_number(self, test_phone_num):
        phone_num = self.find_element(PhoneNumber.input_number)
        phone_num.send_keys(test_phone_num)
        return phone_num

    def click_submit_btn_for_phone_number(self):
        return self.find_element(PhoneNumber.LOCATOR_PHONE_NUMBER_SUBMIT_BUTTON, time=2).click()

    def click_submit_btn_for_phone_number_is_correct(self):
        return self.find_element(PhoneNumber.LOCATOR_SUBMIT_PHONE_IS_CORRECT,time=5).click()

    def thank_you_text(self):
        assert self.find_element(ThankYouPage.thank_text), "No thank you text"

    def user_already_exist_in_db(self):
        assert self.find_element(user_already_exist_db.exist_msg), "No user_exist_msg"

    def clear_input_email_filed(self, ):
        return self.find_element(FirstLastNameForm.EMAIL).clear()
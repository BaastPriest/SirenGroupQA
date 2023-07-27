import pages.data
from pages.main_page import MainPageHelper


def test_new_user_sent_form_for_estimate_callback_confirm_phone_number(browser):
    siding_page = MainPageHelper(browser)
    siding_page.go_to_site()
    siding_page.fill_zip_code(pages.data.zip_code)  # zip code 09090
    siding_page.click_on_get_estimate_button()
    siding_page.choose_type_of_project() # answer the questions on the form
    siding_page.click_on_submit_button_on_question_form()
    siding_page.choose_kind_of_siding()
    siding_page.click_on_submit_button_on_question_form()
    siding_page.fill_square_feet(pages.data.square_feet_int_random)
    siding_page.click_on_submit_button_on_question_form()
    siding_page.select_stories_house()
    siding_page.click_on_submit_button_on_question_form()
    siding_page.select_homeovner_question()
    siding_page.click_on_submit_button_on_question_form()
    siding_page.fill_first_last_name(pages.data.create_full_name()) # enter the first and last name
    siding_page.fill_email(pages.data.create_email())# enter an email
    siding_page.click_on_submit_button_on_question_form()
    siding_page.fill_phone_number(pages.data.phone_num_for_is_correct_question)
    siding_page.click_submit_btn_for_phone_number()
    siding_page.click_submit_btn_for_phone_number_is_correct() # (if necessary) confirm the phone number
    siding_page.thank_you_text() # get a "thank you" siding_page


def test_new_user_estimate_siding_cost_callback(browser):
    siding_page = MainPageHelper(browser)
    siding_page.go_to_site()
    siding_page.fill_zip_code(pages.data.zip_code)  # zip code 09090
    siding_page.click_on_get_estimate_button()
    siding_page.choose_type_of_project()  # answer the questions on the form
    siding_page.click_on_submit_button_on_question_form()
    siding_page.choose_kind_of_siding()
    siding_page.click_on_submit_button_on_question_form()
    siding_page.fill_square_feet(pages.data.square_feet_int_random)
    siding_page.click_on_submit_button_on_question_form()
    siding_page.select_stories_house()
    siding_page.click_on_submit_button_on_question_form()
    siding_page.select_homeovner_question()
    siding_page.click_on_submit_button_on_question_form()
    siding_page.fill_first_last_name(pages.data.create_full_name())  # enter the first and last name
    siding_page.fill_email(pages.data.create_email())  # enter an email
    siding_page.click_on_submit_button_on_question_form()
    siding_page.fill_phone_number(pages.data.create_phone_num()) # enter the phone number
    siding_page.click_submit_btn_for_phone_number()
    siding_page.thank_you_text()  # get a "thank you" page


def test_phone_number_email_already_exist_in_our_database_estimate_siding_cost_callback(browser):
    siding_page = MainPageHelper(browser)
    siding_page.go_to_site()
    siding_page.fill_zip_code(pages.data.zip_code)  # zip code 09090
    siding_page.click_on_get_estimate_button()
    siding_page.choose_type_of_project()  # answer the questions on the form
    siding_page.click_on_submit_button_on_question_form()
    siding_page.choose_kind_of_siding()
    siding_page.click_on_submit_button_on_question_form()
    siding_page.fill_square_feet(pages.data.square_feet_int_random)
    siding_page.click_on_submit_button_on_question_form()
    siding_page.select_stories_house()
    siding_page.click_on_submit_button_on_question_form()
    siding_page.select_homeovner_question()
    siding_page.click_on_submit_button_on_question_form()
    siding_page.fill_first_last_name(pages.data.user_permanent)  # enter the first and last name
    siding_page.fill_email(pages.data.email_permanent)  # enter an email
    siding_page.click_on_submit_button_on_question_form()
    siding_page.fill_phone_number(pages.data.phone_num_permanent)  # enter the phone number
    siding_page.click_submit_btn_for_phone_number()
    siding_page.user_already_exist_in_db()
    siding_page.clear_input_email_filed()
    siding_page.fill_email(pages.data.create_email())
    siding_page.click_on_submit_button_on_question_form()
    siding_page.thank_you_text()  # get a "thank you" page
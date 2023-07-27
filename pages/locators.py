from selenium.webdriver.common.by import By

class MainPageLocators():
    MAIN_PAGE_LINK = (By.XPATH, "https://hb-eta.stage.sirenltd.dev/siding")
    ZIP_CODE_INPUT = (By.XPATH, "//input[@id='zipCode']")
    GET_ESTIMATE_BUTTON = (By.CSS_SELECTOR, "button[data-autotest-button-submit-0]")

class TypeOfProjectLocators():
     REPLACE_EXISTING_SIDING = (By.XPATH, '//input[@data-autotest-radio-sdprojecttype-1]/parent::*')
     SIDING_FOR_NEW_ADDITION = (By.CSS_SELECTOR, "input[data-autotest-radio-sdprojecttype-2]")
     REPAIR_SECTIONS_OF_SIDING = (By.CSS_SELECTOR, "input[data-autotest-radio-sdprojecttype-3]")
     SIDING_FOR_NEW_HOME = (By.CSS_SELECTOR, "input[data-autotest-radio-sdprojecttype-4]")
     NOT_SURE = (By.CSS_SELECTOR, "input[data-autotest-radio-sdprojecttype-5]")

     LOCATOR_SUBMIT_BUTTON = (By.XPATH, '//button[@type="submit" and @data-autotest-button-submit-next]') #the same locator for all question forms

class KindOfSiding():
    VINYL = (By.XPATH, "//input[@data-autotest-radio-sdkind-1]/parent::*")


class SquareFeet():
    INPUT_SIDING_AREA = (By.XPATH, '//input[@label="Siding area in sq ft" and @data-autotest-input-squarefeet-tel]')

class StoriesHouseLocators():
    ONE_STORY = (By.XPATH, '//input[@data-autotest-radio-sdstories-1]/parent::*')

class Homeowner():
    YES_HOMEOVNR = (By.XPATH, '//input[@data-autotest-radio-internalowner-1]/parent::*')

class FirstLastNameForm():
    FULL_NAME = (By.XPATH, '//input[@id="fullName"]')
    EMAIL = (By.XPATH, '//input[@id="email"]')

class PhoneNumber():
    input_number = (By.XPATH, '//input[@id="phoneNumber"]')
    LOCATOR_PHONE_NUMBER_SUBMIT_BUTTON = (By.XPATH, '//button[@data-autotest-button-submit-submit-my-request]')
    LOCATOR_SUBMIT_PHONE_IS_CORRECT = (By.XPATH, '//button[@data-autotest-button-submit-phone-number-is-correct]')

class ThankYouPage():
    thank_text = (By.XPATH, '//h4[contains(text(),"Thank you")]')

class user_already_exist_db():
    exist_msg = (By.XPATH, '//h4[contains(text(),"already exist")]')

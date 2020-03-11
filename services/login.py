from config import PASSWORD, EMAIL, PHONE, LOGIN
# from tinder_bot import WebDriverWait, EC, By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def login(bot_driver):
    login_services = ['fb', 'ph', 'go']
    login_class = [FacebookLogin, PhoneLogin, GoogleLogin]
    loginer_class = None
    for login_service in login_services:
        if login_service is LOGIN:
            loginer_class = login_class[login_services.index(login_service)]
    try:
        loginer = loginer_class(bot_driver)
        loginer.login()
    except:
        raise


class FacebookLogin:
    def __init__(self, bot_driver):
        self.driver = bot_driver

    def login(self):
        try:
            fb_btn = self.driver.find_element_by_xpath("//button[@aria-label='Iniciar sesión con Facebook']")
            fb_btn.click()
        except:
            click_mas_opciones(self.driver)
            fb_btn = self.driver.find_element_by_xpath("//button[@aria-label='Iniciar sesión con Facebook']")
            fb_btn.click()

        base_window = self.driver.window_handles[0]
        fb_login_window = self.driver.window_handles[1]

        # We are switching to the popup window who opened to fb login
        self.driver.switch_to.window(fb_login_window)

        WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="email"]')))

        email_field = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_field.send_keys(EMAIL)
        pass_field = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pass_field.send_keys(PASSWORD)

        fb_login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        fb_login_btn.click()

        self.driver.switch_to.window(base_window)


class PhoneLogin:
    def __init__(self, bot_driver):
        self.driver = bot_driver

    def login(self):
        try:
            phone_btn = self.driver.find_element_by_xpath("//button[@aria-label='Iniciar sesión con nº de teléfono']")
            phone_btn.click()
        except:
            pass
        try:
            phone_btn = self.driver.find_element_by_xpath("//button[@aria-label='Inicia sesión con tu teléfono']")
            phone_btn.click()
        except:
            click_mas_opciones(self.driver)
            phone_btn = self.driver.find_element_by_xpath("//button[@aria-label='Iniciar sesión con nº de teléfono']")
            phone_btn.click()

        WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="phone_number"]')))
        phone_field = self.driver.find_element_by_xpath('//input[@name="phone_number"]')
        phone_field.send_keys(PHONE)

        WebDriverWait(self.driver, 120).until(not EC.title_contains('Tinder |'))


class GoogleLogin:
    def __init__(self, bot_driver):
        self.bot = bot_driver

    def login(self):
        # Not implemented yet
        raise Exception


def click_mas_opciones(driver):
    try:
        masOpciones_btn = driver.find_element_by_xpath('//*[@id ="modal-manager"]/div/div/div/div/div[3]/span/button')
        masOpciones_btn.click()
    except:
        raise

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from services.login import login as login_service
import time


class TinderBot:
    def __init__(self):
        self.base_window = None
        self.fb_login_window = None
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # self.driver.implicitly_wait(4)

    def login(self):
        try:
            self.driver.get('https://tinder.com')
        except:
            quit()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-manager"]/div/div')))

        try:
            login_service(self.driver)
        except:
            quit()

    def handle_aferlogin_popups(self):
        # Allow ubication
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Permitir']")))
        allow_ubc_btn = self.driver.find_element_by_xpath("//button[@aria-label='Permitir']")
        allow_ubc_btn.click()

        # Disallow messages and notifications
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='No me interesa']")))
        notif_not_interested_btn = self.driver.find_element_by_xpath("//button[@aria-label='No me interesa']")
        notif_not_interested_btn.click()

    def like(self):
        try:
            like_btn = self.driver.find_element_by_xpath("//button[@aria-label='Like']")
            like_btn.click()
        except:
            self.handle_modals()

    def dislike(self):
        try:
            like_btn = self.driver.find_element_by_xpath("//button[@aria-label='No']")
            like_btn.click()
        except:
            self.handle_modals()

    def superLike(self):
        try:
            super_like_btn = self.driver.find_element_by_xpath("//button[@aria-label='Super Like']")
            super_like_btn.click()
        except:
            self.handle_modals()

    def autolike(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Like']")))
        time.sleep(2)
        while True:
            try:
                self.has_no_photo()
                time.sleep(0.5)
                self.dislike()
            except:
                time.sleep(0.5)
                self.like()

    def handle_modals(self):
        handlers = [self.handle_close_match_modal,
                    self.handle_add_to_main_screen_modal,
                    self.handle_no_more_likes_modal]
        for handler in handlers:
            try:
                handler()
                return
            except:
                pass

    def handle_close_match_modal(self):
        keep_swiping_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        keep_swiping_btn.click()

    def handle_no_more_likes_modal(self):
        no_more_likes_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[3]/button[2]')
        no_more_likes_btn.click()

    def handle_add_to_main_screen_modal(self):
        no_more_likes_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        no_more_likes_btn.click()

    def has_no_photo(self):
        try:
            self.driver.find_element_by_xpath(
                "//div[@style='background-image: "
                "url(\"https://images-ssl.gotinder.com/0001unknown/640x640_pct_0_0_100_100_unknown.jpg\");"
                " background-position: 50% 50%; background-size: auto 100%;']")
        except:
            raise


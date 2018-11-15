import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait as Wait

from Page.BasePage import BasePage


class HomePage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def is_visible(self):
        if self.browser.current_url == "https://dev.to/":
            return True
        else:
            return False

    def search_for(self, query):
        self.browser.find_element(By.XPATH, "//input[@placeholder='search']").send_keys(query, Keys.ENTER)
        Wait(self.browser, self.timeout).until(expected_conditions.url_contains("https://dev.to/search?q="))
        pass

    def filter_posts_by_latest(self):
        latest_feed_filter = self.browser.find_element_by_xpath("//a[@href='/latest']").click()
        pass

    def is_latest_feed_visible(self):
        month_name_and_date = datetime.datetime.now().strftime("%b %d")
        latest_feed_posts = self.browser.find_element_by_xpath(
            "//a[contains(text(),'" + month_name_and_date + "')]")
        return latest_feed_posts.is_displayed()

    def get_key_links(self):
        key_links = self.browser.find_elements(By.XPATH, "(//header[contains(text(), 'key links')]/../div)[1]/a")
        return key_links

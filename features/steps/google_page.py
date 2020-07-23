from selenium import webdriver


class GoogleSearchPage:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def visit(self, url):
        self.driver.get(url)

    def tearDown(self):
        self.driver.close()

    def enter_text(self, text):
        q = self.driver.find_elements_by_name('q')
        q[0].clear()
        q[0].send_keys(text)
        return True

    def text_search(self, text):
        search_buttons = self.driver.find_elements_by_xpath('//input[@name="btnK"]')
        self.enter_text(text)
        search_buttons[0].click()
        return self.driver.find_element_by_tag_name('body').text
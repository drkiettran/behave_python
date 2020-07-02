from behave import given, when, then
import logging
from selenium import webdriver
import unittest


class GoogleSearch:
    def __init__(self, context):
        self.context = context

    def get(self, url):
        self.context.browser.get(url)

    def enter_text(self, text):
        q = self.context.browser.find_elements_by_name('q')
        q[0].clear()
        q[0].send_keys(text)
        return True

    def text_search(self, text):
        search_buttons = self.context.browser.find_elements_by_xpath('//input[@name="btnK"]')
        self.enter_text(text)
        search_buttons[0].click()
        return self.context.browser.find_element_by_tag_name('body').text


@given(u'I have a browser and a website URL "{url}"')
def step_impl(context, url):
    context.url = url
    context.google_search = GoogleSearch(context)


@when(u'I visit the website URL')
def step_impl(context):
    context.google_search.get(context.url)


@then(u'I should be able to enter a search text')
def step_impl(context):
    result = context.google_search.enter_text('selenium webdriver')


@then(u'I should get a search result for "{text}"')
def step_impl(context, text):
    page_text = context.google_search.text_search(text)
    logging.info(page_text)
    # print(page_text)
    assert text in page_text

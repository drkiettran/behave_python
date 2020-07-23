from behave import given, when, then, fixture
import logging
from selenium import webdriver
import unittest
from google_page import GoogleSearchPage


@fixture()
def before_feature(context):
    pass

@fixture()
def after_feature(context):
    context.google_search.tearDown()

@given(u'I have a browser and a website URL "{url}"')
def step_impl(context, url):
    context.url = url
    context.google_search = GoogleSearchPage()


@when(u'I visit the website URL')
def step_impl(context):
    context.google_search.visit(context.url)


@then(u'I should be able to enter a search text')
def step_impl(context):
    result = context.google_search.enter_text('selenium webdriver')


@then(u'I should get a search result for "{text}"')
def step_impl(context, text):
    page_text = context.google_search.text_search(text)
    logging.info(page_text)
    # print(page_text)
    assert text in page_text

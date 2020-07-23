from behave import given, when, then, fixture
import logging


@given(u'I am at the Spring Initializer website "{url}"')
def step_impl(context, url):
    print(url)
    raise NotImplementedError(u'STEP: Given I am at the Spring Initializer website "https://start.spring.io/"')


@when(u'I create a Spring boot with the following attributes')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I create a Spring boot with the following attributes')


@then(u'I should receive a zip file')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should receive a zip file')


@then(u'the file should contain a build.gradle file with version "2.2.8"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the file should contain a build.gradle file with version "2.2.8"')

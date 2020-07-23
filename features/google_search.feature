Feature: Google Search Capability
  As an Internet User,
  I want to search for textual information
  So that I can complete my homework assignment



  Scenario: Able to enter search text
    Given I have a browser and a website URL "https://google.com"
    When I visit the website URL
    Then I should be able to enter a search text


  Scenario: Able to text search
    Given I have a browser and a website URL "https://google.com"
    When I visit the website URL
    Then I should get a search result for "selenium webdriver"

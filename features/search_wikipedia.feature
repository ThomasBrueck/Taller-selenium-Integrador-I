Feature: Search feature
  Scenario: Search article
    Given the user is on the initial page of wikipedia
    When the user enter the article name
    Then the user should be redirected to the article with the name searched

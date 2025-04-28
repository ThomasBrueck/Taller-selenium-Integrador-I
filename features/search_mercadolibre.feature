Feature: Search feature
  Scenario: Search product
    Given the user is on the initial page
    When the user enter the product name
    Then the user should be redirected to the list of products with the name searched

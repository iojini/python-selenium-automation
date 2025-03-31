Feature: Test Scenario for Product Search

  Scenario: User can see product name and image for each search result
    Given navigation to target.com
    When user conducts product search
    Then each product in the search results should have a name and image
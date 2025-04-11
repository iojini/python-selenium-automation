Feature: Cart Tests

#  @smoke
  Scenario: User can see empty cart message
    Given navigation to target main page
    When user clicks on cart icon
    Then Empty cart message is shown
    And Verify cart page opens
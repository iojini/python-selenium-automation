Feature: Test Scenario for Invalid Login

  Scenario: User sees error message if incorrect password is used
    Given open Target sign in page
    When user enters correct email
    And user clicks Continue
    And user enters incorrect password
    And user clicks Sign in with password
    Then error message should be displayed
Feature: Test Scenario for Target Login Functionality

  Scenario: User can login to Target account
    Given user navigates to target home page
    When user clicks on sign in
    And user clicks on sign in button in right navigation menu
    And user enters email
    And user clicks on continue button
    And user enters password
    And user clicks Sign in with password button
    And user clicks Skip link
    Then user should be logged in (sign in form should disappear)

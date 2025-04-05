Feature: Test Scenario for Sign In Navigation

  Scenario: Logged out user can navigate to sign in page
    Given navigation to target home page
    When user clicks on sign in link in header
    And user clicks on sign in button from the right navigation menu
    Then Sign in form should be displayed
Feature: Test Scenario for Sign In Navigation

  Scenario: Logged out user can navigate to sign in page
    Given navigation to target.com
    When user clicks on sign in link
    And user clicks on sign in button from the navigation menu
    Then Sign In page is displayed
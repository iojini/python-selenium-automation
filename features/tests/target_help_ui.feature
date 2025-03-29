Feature: Test Scenario for Target Help Page UI

  Scenario: User can see UI elements
    Given navigation to target help page
    Then user should see target help heading
    And user should see search input field
    And user should see search button
    And user should see the top help tiles
    And user should see the bottom help tiles
    And user should see the browse help heading

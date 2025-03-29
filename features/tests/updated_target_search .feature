Feature: Test Scenario for Search Functionality

  Scenario Outline: User can search for a product on main page
    Given navigation to target.com
    When user searches for <search_word>
    Then user should see search results for <expected_text>
    Examples:
    |search_word  |expected_text  |
    |tea          |tea            |
    |iPhone       |iPhone         |
    |dress        |dress          |
    |laptop       |laptop         |
    |toothpaste   |toothpaste     |
    |shampoo      |shampoo        |
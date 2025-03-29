Feature: Test Scenario for Add to Cart Functionality

  Scenario: User can add product to cart
    Given navigation to target.com
    When user searches for product
    And user selects the product from results
    And user clicks on add to cart button
    And user clicks on view cart & check out button
    Then cart should contain product


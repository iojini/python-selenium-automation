Feature: Tests for Help pages

  @smoke
  Scenario: User can select Help topic Promotions & Coupons
    Given Open Help page for Returns
    Then Verify help Returns page opened
    When Select Help topic Promotions & Coupons
    Then Verify help Current promotions page opened

  @smoke
  Scenario: User can select Help topic Target Circle
    Given Open Help page for Returns
    Then Verify help Returns page opened
    When Select Help topic Target Circle™
    Then Verify help About Target Circle page opened

  @smoke
  Scenario: User can select Help topic Gift Cards
    Given Open Help page for Returns
    Then Verify help Returns page opened
    When Select Help topic Gift Cards
    Then Verify help Target GiftCard balance page opened
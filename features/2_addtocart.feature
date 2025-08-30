Feature: Purchase products from Swag Labs

  Scenario: User should be able to add a product to the cart
    Given the user is on the products page
    When the user clicks on "Add to Cart"
    Then the selected product should be visible in the cart

  Scenario: User should be able to complete the checkout process
    Given the user is on the cart page
    When the user clicks on the "Checkout" button
    And the user enters the details
      | firstname | lastname | zip    |
      | Raman     | Desuza   | 879678 |
    And the user clicks on the "Continue" button
    And the user clicks on the "Finish" button
    Then the order should be successfully placed

Feature: User should able to Login
  Scenario: User should be able to login with valid credentials
  Given the user is on the login page
  When the user enters username "standard_user" and password "secret_sauce"
  And clicks on the login button
  Then the user should be redirected to the products page
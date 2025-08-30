# SauceDemo Automation (Behave + Selenium + Python)

This repository contains automation test scripts for the [SauceDemo](https://www.saucedemo.com/v1/inventory.html) application.  
The project uses **Behave (BDD framework)** with **Selenium WebDriver** to automate end-to-end test scenarios such as login, adding products to cart, and completing checkout.

---

## 🚀 Tech Stack
- **Python 3.x**
- **Selenium WebDriver**
- **Behave (BDD framework)**
- **ChromeDriver**
- **Git & GitHub**
- **HTML Report (behave-html-formatter)**

---

## 📂 Project Structure

SauceDemo/
│
├── features/
│ ├── addtocart.feature # Feature files (BDD scenarios in Gherkin syntax)
| └── login.feature
│ └── steps/
│ ├── addtocart.py # Step definitions for adding the product
| └──login.py
│ 
│
├── environment.py # Hooks (before_all, after_all for WebDriver setup/teardown)
├── reports/ # HTML reports will be stored here
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

## ⚙️ Setup & Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/raushannitish/SauceDemo.git
   cd SauceDemo
   
2.Create and activate a virtual environment
  python -m venv .venv
  .venv\Scripts\activate   # Windows

3.Install dependencies
   pip install -r requirements.txt

4. Ensure ChromeDriver is installed
   (Match your Chrome browser version)


🧪 Running Tests

Run all tests:

behave


Run with pretty format:

behave -f pretty


Run with HTML report:

behave -f behave_html_formatter:HTMLFormatter -o reports/behave_report.html


Then open the report:

reports/behave_report.html




✅ Example Scenarios

Login
Feature: User should able to Login
  Scenario: User should be able to login with valid credentials
  Given the user is on the login page
  When the user enters username "standard_user" and password "secret_sauce"
  And clicks on the login button
  Then the user should be redirected to the products page

Add to cart  
Scenario: User should be able to add a product to the cart
    Given the user is on the products page
    When the user clicks on "Add to Cart"
    Then the selected product should be visible in the cart

Checkout
Scenario: User should be able to complete the checkout process
  Given the user has added a product to the cart
  When the user clicks on checkout
  And enters their details
    | firstname | lastname | zip    |
    | Raman     | Desuza   | 879678 |
  And clicks continue
  And clicks finish
  Then the order should be successfully placed

📊 Reports

HTML reports are generated inside the reports/ folder.
Open behave_report.html in any browser to view the test execution results


# SANCHARI DEY 12023002001302

# Selenium Capstone Assignment 


## Project Title

Automate a Web Application Using Selenium WebDriver with Python

## Project Objective

The objective of this project is to automate an e-commerce purchase workflow using Selenium WebDriver with Python.

The automation covers browser launch, login, product search, adding a product to the cart, cart verification, checkout, order completion, screenshots, test data handling, alert handling, and execution reporting.

## Application Used

SauceDemo

Website:
https://www.saucedemo.com/

## Technologies Used

- Python
- Selenium WebDriver
- Google Chrome
- JSON
- VS Code

## Test Data

Test data is stored in:

`test_data/test_data.json`

The JSON file contains:

- Username
- Password
- Product name

## Automated Test Flow

1. Launch Google Chrome
2. Open SauceDemo
3. Login using test data
4. Verify the Products page
5. Find Sauce Labs Backpack
6. Add the product to the cart
7. Verify the cart contains the product
8. Open the cart
9. Verify the product in the cart
10. Verify the product quantity
11. Capture a cart screenshot
12. Open checkout
13. Enter customer information
14. Continue to checkout overview
15. Verify the checkout product
16. Complete the order
17. Verify order confirmation
18. Capture the order confirmation screenshot
19. Handle alert if available
20. Generate execution report
21. Close the browser

## Test Data File

Example:

```json
{
    "username": "standard_user",
    "password": "secret_sauce",
    "product": "Sauce Labs Backpack"
}

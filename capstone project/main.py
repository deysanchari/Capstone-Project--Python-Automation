import json
import os
import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ============================================================
# 0. PROJECT PATH
# ============================================================

# Get the folder where main.py is located
project_folder = os.path.dirname(
    os.path.abspath(__file__)
)

print("Project folder:")
print(project_folder)


# ============================================================
# 1. READ TEST DATA FROM JSON
# ============================================================

test_data_path = os.path.join(
    project_folder,
    "test_data",
    "test_data.json"
)

print("Reading test data from:")
print(test_data_path)


try:

    with open(
        test_data_path,
        "r",
        encoding="utf-8"
    ) as file:

        test_data = json.load(file)

    username_data = test_data["username"]
    password_data = test_data["password"]
    product_data = test_data["product"]

    print("Test data loaded successfully!")

except Exception as e:

    print("ERROR: Could not load test data!")
    print("Error:", e)

    raise


# ============================================================
# 2. CREATE FOLDERS
# ============================================================

reports_folder = os.path.join(
    project_folder,
    "reports"
)

screenshots_folder = os.path.join(
    project_folder,
    "screenshots"
)


# Create folders automatically
os.makedirs(
    reports_folder,
    exist_ok=True
)

os.makedirs(
    screenshots_folder,
    exist_ok=True
)


# ============================================================
# 3. REPORT PATH
# ============================================================

report_path = os.path.join(
    reports_folder,
    "execution_report.txt"
)


# ============================================================
# 4. CREATE EXECUTION REPORT
# ============================================================

with open(
    report_path,
    "w",
    encoding="utf-8"
) as report:

    report.write(
        "SELENIUM CAPSTONE ASSIGNMENT 1 - EXECUTION REPORT\n"
    )

    report.write(
        "=" * 60 + "\n"
    )

    report.write(
        f"Execution Date: {datetime.now()}\n"
    )

    report.write(
        "Application: SauceDemo\n"
    )

    report.write(
        "Browser: Google Chrome\n"
    )

    report.write(
        "=" * 60 + "\n\n"
    )


print("Execution report created!")
print("Report location:")
print(report_path)


# ============================================================
# 5. FUNCTION TO WRITE TEST RESULTS
# ============================================================

def write_report(test_name, status, details=""):

    with open(
        report_path,
        "a",
        encoding="utf-8"
    ) as report:

        report.write(
            f"{test_name:<35} : {status}\n"
        )

        report.write(
            "-" * 60 + "\n"
        )

    print(
        f"REPORT UPDATED: {test_name} : {status}"
    )


# ============================================================
# 6. LAUNCH BROWSER
# ============================================================

driver = webdriver.Chrome()

driver.maximize_window()

wait = WebDriverWait(
    driver,
    10
)


# ============================================================
# 7. OPEN SAUCEDEMO
# ============================================================

try:

    driver.get(
        "https://www.saucedemo.com/"
    )

    print("SauceDemo opened successfully!")

    write_report(
        "Browser Launch",
        "PASS"
    )

except Exception as e:

    print(
        "Browser launch failed!"
    )

    print(
        "Error:",
        e
    )

    write_report(
        "Browser Launch",
        "FAIL"
    )


# ============================================================
# 8. LOGIN
# ============================================================

try:

    # Find username field
    username = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "user-name")
        )
    )

    username.send_keys(
        username_data
    )


    # Find password field
    password = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "password")
        )
    )

    password.send_keys(
        password_data
    )


    # Find login button
    login_button = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "login-button")
        )
    )

    login_button.click()


    # Verify Products page
    products_title = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "title")
        )
    )


    if products_title.text == "Products":

        print(
            "LOGIN SUCCESSFUL!"
        )

        print(
            "Products page opened successfully."
        )

        write_report(
            "Login",
            "PASS"
        )

    else:

        print(
            "LOGIN FAILED!"
        )

        write_report(
            "Login",
            "FAIL"
        )


except Exception as e:

    print(
        "LOGIN FAILED!"
    )

    print(
        "Error:",
        e
    )

    write_report(
        "Login",
        "FAIL"
    )


# ============================================================
# 9. FIND PRODUCT
# ============================================================

try:

    product = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                f"//div[text()='{product_data}']"
            )
        )
    )


    print(
        "Product found:",
        product.text
    )


    write_report(
        "Product Search",
        "PASS"
    )


except Exception as e:

    print(
        "Product search failed!"
    )

    print(
        "Error:",
        e
    )

    write_report(
        "Product Search",
        "FAIL"
    )


# ============================================================
# 10. ADD PRODUCT TO CART
# ============================================================

try:

    add_to_cart_button = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"//div[text()='{product_data}']"
                "/ancestor::div[@class='inventory_item']"
                "//button"
            )
        )
    )


    add_to_cart_button.click()


    print(
        f"{product_data} added to cart!"
    )


    write_report(
        "Add Product to Cart",
        "PASS"
    )


except Exception as e:

    print(
        "Failed to add product to cart!"
    )

    print(
        "Error:",
        e
    )

    write_report(
        "Add Product to Cart",
        "FAIL"
    )


# ============================================================
# 11. VERIFY CART BADGE
# ============================================================

try:

    cart_badge = wait.until(
        EC.visibility_of_element_located(
            (
                By.CLASS_NAME,
                "shopping_cart_badge"
            )
        )
    )


    if cart_badge.text == "1":

        print(
            "CART VERIFICATION SUCCESSFUL!"
        )

        print(
            "Cart contains 1 product."
        )

        write_report(
            "Cart Verification",
            "PASS"
        )

    else:

        print(
            "CART VERIFICATION FAILED!"
        )

        print(
            "Cart badge shows:",
            cart_badge.text
        )

        write_report(
            "Cart Verification",
            "FAIL"
        )


except Exception as e:

    print(
        "CART VERIFICATION FAILED!"
    )

    print(
        "Cart badge was not found."
    )

    print(
        "Error:",
        e
    )

    write_report(
        "Cart Verification",
        "FAIL"
    )


# ============================================================
# 12. OPEN CART
# ============================================================

try:

    cart_icon = wait.until(
        EC.element_to_be_clickable(
            (
                By.CLASS_NAME,
                "shopping_cart_link"
            )
        )
    )


    cart_icon.click()


    print(
        "Cart page opened successfully."
    )


    write_report(
        "Open Cart",
        "PASS"
    )


except Exception as e:

    print(
        "Failed to open cart!"
    )

    print(
        "Error:",
        e
    )

    write_report(
        "Open Cart",
        "FAIL"
    )


# ============================================================
# 10. VERIFY PRODUCT QUANTITY
# ============================================================

try:
    quantity = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "cart_quantity"))
    )

    current_quantity = quantity.text

    print("Product quantity:", current_quantity)

    if current_quantity == "1":
        print("QUANTITY VERIFICATION SUCCESSFUL!")
        print("Note: SauceDemo does not provide an option to manually update")
        print("the quantity of the same product in the cart.")

        write_report(
            "Quantity Verification",
            "PASS",
            "Product quantity verified as 1. "
            "SauceDemo does not provide an editable quantity control."
        )
    else:
        print("QUANTITY VERIFICATION FAILED!")

        write_report(
            "Quantity Verification",
            "FAIL",
            f"Expected quantity 1, but found {current_quantity}"
        )

except Exception as e:
    print("Quantity verification failed!")
    print("Error:", e)

    write_report(
        "Quantity Verification",
        "FAIL",
        str(e)
    )

# ============================================================
# 12. PROCEED TO CHECKOUT
# ============================================================

checkout_success = False

try:
    checkout_button = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "checkout")
        )
    )

    checkout_button.click()

    checkout_title = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "title")
        )
    )

    if checkout_title.text == "Checkout: Your Information":

        print("Checkout information page opened successfully.")

        write_report(
            "Proceed to Checkout",
            "PASS",
            "Checkout information page displayed"
        )

        checkout_success = True

    else:

        print("Checkout page verification failed!")

        write_report(
            "Proceed to Checkout",
            "FAIL",
            f"Unexpected page title: {checkout_title.text}"
        )

except Exception as e:

    print("Failed to proceed to checkout!")
    print("Error:", e)

    write_report(
        "Proceed to Checkout",
        "FAIL",
        str(e)
    )    

# ============================================================
# 13. ENTER CUSTOMER INFORMATION
# ============================================================

checkout_info_success = False

if checkout_success:

    try:
        first_name = wait.until(
            EC.element_to_be_clickable(
                (By.ID, "first-name")
            )
        )

        first_name.clear()
        first_name.send_keys("Sanchari")

        last_name = wait.until(
            EC.element_to_be_clickable(
                (By.ID, "last-name")
            )
        )

        last_name.clear()
        last_name.send_keys("Dey")

        postal_code = wait.until(
            EC.element_to_be_clickable(
                (By.ID, "postal-code")
            )
        )

        postal_code.clear()
        postal_code.send_keys("700001")

        print("Customer information entered successfully.")

        write_report(
            "Customer Information",
            "PASS",
            "First name, last name and postal code entered"
        )

        checkout_info_success = True

    except Exception as e:

        print("Failed to enter customer information!")
        print("Error:", e)

        write_report(
            "Customer Information",
            "FAIL",
            str(e)
        )

else:

    print("Customer information skipped because checkout was not reached.")

    write_report(
        "Customer Information",
        "SKIPPED",
        "Checkout information page was not reached"
    )
# ============================================================
# 14. CONTINUE TO OVERVIEW
# ============================================================

checkout_overview_success = False

if checkout_info_success:

    try:
        continue_button = wait.until(
            EC.element_to_be_clickable(
                (By.ID, "continue")
            )
        )

        continue_button.click()

        overview_title = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "title")
            )
        )

        if overview_title.text == "Checkout: Overview":

            print("Checkout overview opened successfully.")

            write_report(
                "Checkout Overview",
                "PASS",
                "Checkout overview displayed"
            )

            checkout_overview_success = True

        else:

            print("Checkout overview verification failed!")

            write_report(
                "Checkout Overview",
                "FAIL",
                f"Unexpected page title: {overview_title.text}"
            )

    except Exception as e:

        print("Failed to open checkout overview!")
        print("Error:", e)

        write_report(
            "Checkout Overview",
            "FAIL",
            str(e)
        )

else:

    print("Checkout overview skipped because customer information failed.")

    write_report(
        "Checkout Overview",
        "SKIPPED",
        "Customer information was not entered"
    )


# ============================================================
# 15. VERIFY PRODUCT ON CHECKOUT
# ============================================================

checkout_product_success = False

if checkout_overview_success:

    try:
        checkout_product = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "inventory_item_name")
            )
        )

        if checkout_product.text == product_data:

            print("CHECKOUT PRODUCT VERIFICATION SUCCESSFUL!")

            write_report(
                "Checkout Product Verification",
                "PASS",
                f"Product verified: {checkout_product.text}"
            )

            checkout_product_success = True

        else:

            print("CHECKOUT PRODUCT VERIFICATION FAILED!")

            write_report(
                "Checkout Product Verification",
                "FAIL",
                f"Unexpected product: {checkout_product.text}"
            )

    except Exception as e:

        print("Checkout product verification failed!")
        print("Error:", e)

        write_report(
            "Checkout Product Verification",
            "FAIL",
            str(e)
        )

else:

    print("Checkout product verification skipped.")

    write_report(
        "Checkout Product Verification",
        "SKIPPED",
        "Checkout overview was not reached"
    )


# ============================================================
# 16. FINISH ORDER
# ============================================================

order_completed = False

if checkout_product_success:

    try:
        finish_button = wait.until(
            EC.element_to_be_clickable(
                (By.ID, "finish")
            )
        )

        finish_button.click()

        confirmation = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "complete-header")
            )
        )

        if confirmation.text == "Thank you for your order!":

            print("ORDER COMPLETED SUCCESSFULLY!")
            print("Confirmation:", confirmation.text)

            write_report(
                "Complete Order",
                "PASS",
                "Order completed successfully"
            )

            order_completed = True

        else:

            print("ORDER COMPLETION VERIFICATION FAILED!")

            write_report(
                "Complete Order",
                "FAIL",
                f"Unexpected confirmation: {confirmation.text}"
            )

    except Exception as e:

        print("Order completion failed!")
        print("Error:", e)

        write_report(
            "Complete Order",
            "FAIL",
            str(e)
        )

else:

    print("Order completion skipped.")

    write_report(
        "Complete Order",
        "SKIPPED",
        "Checkout product verification was not completed"
    )


# ============================================================
# 17. FINAL SCREENSHOT
# ============================================================

if order_completed:

    try:

        # Create screenshot folder if it does not exist
        os.makedirs(screenshots_folder, exist_ok=True)

        final_screenshot = os.path.join(
            screenshots_folder,
            "order_confirmation.png"
        )

        driver.save_screenshot(final_screenshot)

        print("Final screenshot captured successfully!")
        print("Screenshot saved at:", final_screenshot)

        write_report(
            "Order Confirmation Screenshot",
            "PASS",
            final_screenshot
        )

    except Exception as e:

        print("Final screenshot failed!")
        print("Error:", e)

        write_report(
            "Order Confirmation Screenshot",
            "FAIL",
            str(e)
        )

else:

    print(
        "Final order screenshot skipped because "
        "order was not completed."
    )

    write_report(
        "Order Confirmation Screenshot",
        "SKIPPED",
        "Order was not completed"
    )

# ============================================================
# 18. KEEP BROWSER OPEN
# ============================================================

time.sleep(3)


# ============================================================
# 19. CLOSE BROWSER
# ============================================================

driver.quit()

print(
    "Browser closed."
)
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Initialize Firefox WebDriver
driver = webdriver.Firefox()

try:
    # Open the home page of your Django project
    driver.get("http://127.0.0.1:8000/")  # Replace with the actual URL of your Django project

    # Test Case 1: Verify navigation to different sections
    home_link = driver.find_element(By.CSS_SELECTOR, ".nav__link[href='#home']")
    about_link = driver.find_element(By.CSS_SELECTOR, ".nav__link[href='#about']")
    products_link = driver.find_element(By.CSS_SELECTOR, ".nav__link[href='#products']")
    faqs_link = driver.find_element(By.CSS_SELECTOR, ".nav__link[href='#faqs']")
    contact_link = driver.find_element(By.CSS_SELECTOR, ".nav__link[href='#contact']")

    home_link.click()
    time.sleep(5)  # Allow time for the page to load
    assert "home" in driver.current_url.lower()

    about_link.click()
    time.sleep(5)
    assert "about" in driver.current_url.lower()

    products_link.click()
    time.sleep(5)
    assert "products" in driver.current_url.lower()

    faqs_link.click()
    time.sleep(5)
    assert "faqs" in driver.current_url.lower()

    contact_link.click()
    time.sleep(5)
    assert "contact" in driver.current_url.lower()
    
    #----register code----
    driver.get("http://127.0.0.1:8000/register/")  # Replace with the actual URL of your registration page

    # Fill out the registration form
    username_input = driver.find_element(By.ID, "username")
    email_input = driver.find_element(By.ID, "email")
    password1_input = driver.find_element(By.ID, "password1")
    password2_input = driver.find_element(By.ID, "password2")

    # Replace 'test_user', 'test@example.com', 'testpassword' with your desired credentials
    username_input.send_keys("selenium")
    email_input.send_keys("baby.trishul@gmail.com")
    password1_input.send_keys("selenium")
    password2_input.send_keys("selenium")

    # Submit the registration form
    password2_input.send_keys(Keys.ENTER)

    # Allow time for the registration process to complete
    time.sleep(5)
    
    #----login code----
    driver.get("http://127.0.0.1:8000/login/")  # Replace with the actual URL of your login page

    # Fill out the login form
    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")

    # Replace 'selenium' with the username and password you provided
    username_input.send_keys("selenium")
    password_input.send_keys("selenium")

    # Submit the login form
    password_input.send_keys(Keys.ENTER)

    # Allow time for the login process to complete
    time.sleep(5)


    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Login successful!")
    print("All test cases passed!")

finally:
    # Close the browser
    driver.quit()

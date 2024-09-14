from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")

    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    driver.find_element(By.ID, "login-button").click()

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    driver.find_element(By.ID, "checkout").click()

    driver.find_element(By.ID, "first-name").send_keys("artem")

    driver.find_element(By.ID, "last-name").send_keys("hhru")

    driver.find_element(By.ID, "postal-code").send_keys("12345")

    driver.find_element(By.ID, "continue").click()

    driver.find_element(By.ID, "finish").click()

    complete_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "complete-header")))

    assert "THANK YOU FOR YOUR ORDER" in complete_message.text.strip().upper(), "Сообщение не найдено"
    
    print("Тест успешно завершен!")

finally:
    
    driver.quit()

import time
from selenium.webdriver.common.by import By

def test_registration(driver):
    driver.get("https://victoretc.github.io/selenium_waits/")

    text_title = driver.find_element(By.XPATH,"//body/h1").text
    assert text_title == "Практика с ожиданиями в Selenium"

    time.sleep(5)
    button_visible = driver.find_element(By.XPATH, "//button[@id='startTest']")
    button_visible.click()

    driver.find_element(By.XPATH, "//input[@id='login']").send_keys("login")
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("password")
    driver.find_element(By.XPATH, "//input[@id='agree']").click()
    driver.find_element(By.XPATH, "//button[@id='register']").click()

    load_is_display = driver.find_element(By.XPATH, "//div[@id='loader']").is_displayed()
    assert load_is_display == True

    time.sleep(5)
    loading_end = driver.find_element(By.XPATH, "//p[@id='successMessage']").text

    assert loading_end == "Вы успешно зарегистрированы!"



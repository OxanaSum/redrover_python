from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import conftest

def test_registration(driver, wait):
    driver.get("https://victoretc.github.io/selenium_waits/")

    text_title = driver.find_element(By.XPATH,"//body/h1").text
    assert text_title == "Практика с ожиданиями в Selenium"

    button_visible = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='startTest']")))
    button_visible.click()

    driver.find_element(By.XPATH, "//input[@id='login']").send_keys("login")
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("password")
    driver.find_element(By.XPATH, "//input[@id='agree']").click()
    driver.find_element(By.XPATH, "//button[@id='register']").click()

    load_is_display = driver.find_element(By.XPATH, "//div[@id='loader']").is_displayed()
    assert load_is_display == True

    text_after_loading = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[@id='successMessage']"))).text
    assert text_after_loading == "Вы успешно зарегистрированы!"



import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_registration(driver):
    driver.get("https://victoretc.github.io/selenium_waits/")

    text_title = driver.find_element(By.XPATH,"//body/h1").text
    assert text_title == "Практика с ожиданиями в Selenium"

    button_visible = driver.find_element(By.XPATH, "//button[@id='startTest']")
    button_visible.click()

    driver.find_element(By.XPATH, "//input[@id='login']").send_keys("login")
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("password")
    driver.find_element(By.XPATH, "//input[@id='agree']").click()
    driver.find_element(By.XPATH, "//button[@id='register']").click()

    load_is_display = driver.find_element(By.XPATH, "//div[@id='loader']").is_displayed()
    assert load_is_display == True

    loading_end = driver.find_element(By.XPATH, "//p[@id='successMessage']")
    while (loading_end.is_displayed() == False):
        pass

    assert loading_end.text == "Вы успешно зарегистрированы!"



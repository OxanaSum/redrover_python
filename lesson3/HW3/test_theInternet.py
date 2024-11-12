from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
import conftest


def test_add_element(driver):
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
    button_add = driver.find_element(By.XPATH, "//button")
    button_add.click()

    button_del = driver.find_element(By.XPATH, "//button[@class='added-manually']")

    assert button_del.is_displayed()

def test_del_element(driver):
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
    button_add = driver.find_element(By.XPATH, "//button")
    button_add.click()

    button_del = driver.find_element(By.XPATH, "//button[@class='added-manually']")
    button_del.click()

    try:
        button_del_check  = driver.find_element(By.XPATH, "//button[@class='added-manually']").is_displayed()
    except NoSuchElementException:
        button_del_check = False

    assert button_del_check == False

def test_authorisation(driver):
    login = "admin"
    passw = "admin"
    driver.get(f'https://{login}:{passw}@the-internet.herokuapp.com/basic_auth')

    message = driver.find_element(By.XPATH, "//p").text

    assert message == "Congratulations! You must have the proper credentials."











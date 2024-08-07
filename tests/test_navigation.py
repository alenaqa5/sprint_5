import locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def test_navigation_to_profile(login):
    driver = login
    driver.find_element(By.XPATH, locators.personal_account_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, locators.logout_button)))
    assert driver.find_element(By.XPATH, locators.logout_button)


def test_navigate_to_constructor_by_constructor_button(login):
    driver = login
    driver.find_element(By.XPATH, locators.personal_account_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, locators.logout_button)))
    driver.find_element(By.XPATH, locators.constructor).click()
    assert driver.find_element(By.XPATH, locators.collect_burger)


def test_navigate_to_constructor_by_logo(login):
    driver = login
    driver.find_element(By.XPATH, locators.personal_account_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, locators.logout_button)))
    driver.find_element(By.XPATH, locators.logo).click()
    assert driver.find_element(By.XPATH, locators.collect_burger)

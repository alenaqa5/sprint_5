import locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest


@pytest.mark.parametrize('setup', ['main_page'], indirect=True)
def test_logout_from_profile(login):
    driver = login
    driver.find_element(By.XPATH, locators.personal_account_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, locators.logout_button)))
    driver.find_element(By.XPATH, locators.logout_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, locators.login_button)))
    assert driver.find_element(By.XPATH, locators.login_button)


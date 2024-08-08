import locators
from selenium.webdriver.common.by import By
import pytest


@pytest.mark.parametrize('setup', ['main_page'], indirect=True)
def test_to_sauces_tab(setup):
    driver = setup
    driver.find_element(By.XPATH, locators.tab_sauces_not_selected).click()
    assert driver.find_element(By.XPATH, locators.tab_sauces_selected)


@pytest.mark.parametrize('setup', ['main_page'], indirect=True)
def test_to_buns_tab(setup):
    driver = setup
    driver.find_element(By.XPATH, locators.tab_sauces_not_selected).click()
    driver.find_element(By.XPATH, locators.tab_buns).click()
    assert driver.find_element(By.XPATH, locators.bun)


@pytest.mark.parametrize('setup', ['main_page'], indirect=True)
def test_to_toppings_tab(setup):
    driver = setup
    driver.find_element(By.XPATH, locators.tab_toppings).click()
    assert driver.find_element(By.XPATH, locators.header_toppings)

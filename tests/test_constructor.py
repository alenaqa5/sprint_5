import locators
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_to_sauces_tab():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, locators.tab_sauces).click()
    assert driver.find_element(By.XPATH, locators.sauce)
    driver.quit()


def test_to_buns_tab():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, locators.tab_sauces).click()
    driver.find_element(By.XPATH, locators.tab_buns).click()
    assert driver.find_element(By.XPATH, locators.bun)
    driver.quit()


def test_to_toppings_tab():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, locators.tab_toppings).click()
    assert driver.find_element(By.XPATH, locators.header_toppings)
    driver.quit()

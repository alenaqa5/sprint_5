import pytest
from selenium import webdriver
import random
from selenium.webdriver.common.by import By
import locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


@pytest.fixture
def create_email():
    return f'alena_podgornaia_12{random.randint(100, 300)}@yandex.ru'

@pytest.fixture
def create_correct_password():
    return f'{random.randint(100000, 200000)}'

@pytest.fixture
def create_incorrect_password():
    return f'{random.randint(1, 200)}'


@pytest.fixture
def create_username():
    names = 'этомногобуквычтобыдляименивыбратьоднуизбуквпоследовательности'
    return f'{random.choice(names)}'

@pytest.fixture
def login():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, locators.login_to_account_button).click()
    driver.find_element(By.XPATH, locators.email).send_keys('alena_podgornaia_1245@yandex.ru')
    driver.find_element(By.XPATH, locators.password).send_keys('123456')
    driver.find_element(By.XPATH, locators.login_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, locators.create_order)))
    yield driver
    driver.quit()


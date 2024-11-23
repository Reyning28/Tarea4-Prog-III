import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def setup():
    driver = webdriver.Chrome(executable_path="C:\\Users\\perdo\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login_success(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "username").send_keys("testuser")
    driver.find_element(By.ID, "password").send_keys("password123")
    driver.find_element(By.ID, "loginButton").click()

    assert "Bienvenido" in driver.page_source
    driver.save_screenshot("test_login_success.png")

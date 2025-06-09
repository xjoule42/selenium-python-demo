import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage

def test_valid_login():
    options = Options()
    options.add_argument("--headless")  # Ejecuta Chrome sin interfaz gráfica
    driver = webdriver.Chrome(options=options)
    login = LoginPage(driver)
    login.open()
    login.login("tomsmith", "SuperSecretPassword!")
    assert "You logged into a secure area!" in login.get_flash_message()
    driver.quit()

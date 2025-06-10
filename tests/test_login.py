import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from dotenv import load_dotenv
import os

load_dotenv()  # Carga las variables del archivo .env

def test_valid_login():
    options = Options()
    options.add_argument("--headless")  # Ejecuta Chrome sin interfaz gráfica
    driver = webdriver.Chrome(options=options)
    login = LoginPage(driver)
    login.open()
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    login.login(username, password)
    assert "You logged into a secure area!" in login.get_flash_message()
    driver.quit()

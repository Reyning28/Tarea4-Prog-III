from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Usar ChromeDriverManager para gestionar el chromedriver automáticamente
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Navegar a la página de inicio de sesión de Sauce Demo
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    # Esperar un poco para que la página cargue
    time.sleep(2)

    # Captura de pantalla de la página de inicio
    driver.save_screenshot("inicio_pagina_saucedemo.png")

    # Encuentra los campos y el botón de inicio de sesión
    username_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    # Ingresar los datos de inicio de sesión
    username_field.send_keys("standard_user")  
    password_field.send_keys("secret_sauce")  
    login_button.click()

    # Captura de pantalla después de hacer clic en el botón de login
    driver.save_screenshot("despues_de_login.png")

    # Esperar hasta que la URL cambie a la página de productos
    WebDriverWait(driver, 10).until(EC.url_contains("inventory.html"))

    # Captura de pantalla de la página de productos
    driver.save_screenshot("pagina_de_productos.png")

    print("Inicio de sesión exitoso")

    
    product = driver.find_element(By.CLASS_NAME, "inventory_item")
    product.click()

    # Captura de pantalla después de hacer clic en el primer producto
    driver.save_screenshot("producto_seleccionado.png")

finally:
    # Cerrar el navegador
    driver.quit()

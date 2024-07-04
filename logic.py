import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Función para verificar si la fecha está dentro de dos meses
def is_within_two_months(date_str):
    from datetime import datetime, timedelta
    date_format = "%d/%m/%Y"  # Ajustar el formato de fecha según sea necesario
    date = datetime.strptime(date_str, date_format)
    return date <= datetime.today() + timedelta(days=60)

def login_and_book_test(user_id, password, favorite_centre):
    #Configurar Opciones
    
    # Configuración del navegador
    driver = webdriver.Chrome()
    driver.maximize_window()
    # Navegar a la página inicial
    driver.get("https://www.gov.uk/book-pupil-driving-test")

    # Click en el botón "Start now"
    start_test_button = driver.find_element(By.LINK_TEXT, "Start now")
    start_test_button.click()

    # Esperar y navegar a la página de inicio de sesión
    WebDriverWait.until

    # Inicio de sesión
    user_id_field = driver.find_element(By.ID, "user-id")
    password_field = driver.find_element(By.ID, "password")

    user_id_field.send_keys(user_id)
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)

    # Esperar a que la página cargue
    WebDriverWait.until

    # Seleccionar centro favorito
    select_element = driver.find_element(By.ID, "testcentregroups")
    for option in select_element.find_elements(By.TAG_NAME, 'option'):
        if option.text == favorite_centre:
            option.click()
            break

    # Selección de 'No' en 'Special Needs'
    no_special_needs_radio = driver.find_element(By.ID, "specialNeedsChoice-noneeds")
    no_special_needs_radio.click()

    # Click en el botón "Book test"
    book_test_button = driver.find_element(By.ID, "submitSlotSearch")
    book_test_button.click()

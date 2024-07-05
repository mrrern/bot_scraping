import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tkinter import messagebox
from selenium.webdriver.support import expected_conditions as EC

# Función para verificar si la fecha está dentro de dos meses
def is_within_two_months(date_str):
    from datetime import datetime, timedelta
    date_format = "%d/%m/%Y"  # Ajustar el formato de fecha según sea necesario
    date = datetime.strptime(date_str, date_format)
    return date <= datetime.today() + timedelta(days=60)

def login_and_book_test(favorite_centre):
    # Configuración del navegador
    driver = webdriver.Safari()
    driver.maximize_window()

    # Navegar a la página inicial
    driver.get("https://www.gov.uk/book-pupil-driving-test")

    # Esperar a que la página cargue completamente la página inicial
    wait = WebDriverWait(driver, 200)
    current_utl =  driver.current_url

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'testcentre')))

    # Indicar al usuario que ingrese sus credenciales manualmente
    messagebox.showinfo(title="SIIIII", message="Ahora si entra.")

    # Esperar a que la URL cambie, lo que indica que el usuario ha iniciado sesión
    initial_url = driver.current_url
    while driver.current_url == initial_url:
        time.sleep(6)

    driver.close()

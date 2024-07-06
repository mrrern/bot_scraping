import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tkinter import messagebox
from selenium.webdriver.support import expected_conditions as EC

def is_within_two_months(date_str):
    from datetime import datetime, timedelta
    date_format = "%d/%m/%Y"  # Adjust the date format as needed
    date = datetime.strptime(date_str, date_format)
    return date <= datetime.today() + timedelta(days=60)

def login_and_book_test():
    # Configure Safari browser
    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')
    
    options.page_load_strategy = 'normal'  # Load the entire page before proceeding
    driver = webdriver.Chrome(options=options)

    driver.maximize_window()

    # Navigate to the homepage
    driver.get("https://www.gov.uk/book-pupil-driving-test")

    # Wait for the homepage to fully load
    wait = WebDriverWait(driver, 20)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'Book Test')))

    # Inform the user to manually enter their credentials
    messagebox.showinfo(title="SIIIII", message="Ahora si entra.")

    # Wait for the URL to change, indicating successful login
    current_url = driver.current_url
    initial_url = driver.current_url
    while driver.current_url == initial_url:
        time.sleep(6)

    # Close the Safari browser
    driver.quit()

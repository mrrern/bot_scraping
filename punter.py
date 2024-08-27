import pyautogui
import time
from tkinter import messagebox
import tkinter as tk

def click_button(image, timeout=60, confidence=0.8):
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            button_location = pyautogui.locateOnScreen(image, confidence=confidence)
            if button_location is not None:
                # Buscar la imagen y esperar 10 segundos
                time.sleep(10)
                # Click en el centro de la imagen
                pyautogui.moveTo(button_location.left + button_location.width / 2, button_location.top + button_location.height / 2)
                return True
        except pyautogui.ImageNotFoundException:
            print("Button not found")
            pass
        time.sleep(1)
    return False

def reserve_test():
    if click_button('images/view.png'):
        time.sleep(10)  # Esperar 10 segundos antes de continuar
        while click_button('images/reserve_test.png'):
            time.sleep(10)  # Esperar 10 segundos entre cada reserva
        return True
    return False

def activate_chrome():
    # Ajusta estos valores según la posición de la barra de título en tu pantalla
    pyautogui.moveTo(100, 10)
    pyautogui.click()
    time.sleep(10)  # Esperar 10 segundos antes de continuar

def main():
    reservations_needed = 10
    reservations_done = 0

    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal de Tkinter

    # Activar la ventana del navegador Chrome
    activate_chrome()

    while reservations_done < reservations_needed:
        if not reserve_test():
            if click_button('images/next_available.png'):
                time.sleep(10)  # Esperar 10 segundos antes de continuar
                pyautogui.scroll(-10000)  # Scroll to the bottom
                time.sleep(10)  # Esperar 10 segundos antes de continuar
                pyautogui.scroll(10000)  # Scroll to the top
                time.sleep(10)  # Esperar 10 segundos antes de continuar
                continue
            else:
                messagebox.showerror("No hay tests disponibles", "No hay tests disponibles")
                messagebox.showinfo("Proceso terminado", f"Reservas hechas: {reservations_done}")
                return

        while reservations_done < reservations_needed:
            if reserve_test():
                reservations_done += 1
                if reservations_done >= reservations_needed:
                    messagebox.showinfo("Programa completado", "Programa completado")
                    return
            else:
                time.sleep(10)  # Esperar 10 segundos antes de continuar
                if click_button('images/return_search.png'):
                    time.sleep(10)  # Esperar 10 segundos antes de continuar
                    break
                else:
                    messagebox.showinfo("Proceso terminado", f"Reservas hechas: {reservations_done}")
                    return

        time.sleep(10)  # Esperar 10 segundos antes de continuar

    messagebox.showinfo("Proceso terminado", f"Reservas hechas: {reservations_done}")
    print(f'Proceso terminado. Reservas hechas: {reservations_done}')

if __name__ == "__main__":
    main()
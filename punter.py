# import pyautogui
# import time
# from tkinter import messagebox
# from tkinter import ttk
# import tkinter as tk

# def click_button(image, confidence=0.8, timeout=30):
#     start_time = time.time()
#     while time.time() - start_time < timeout:
#         button_location = pyautogui.locateOnScreen(image, confidence=confidence)
#         if button_location is not None:
#             pyautogui.click(button_location)
#             return True
#         time.sleep(1)
#     return False

# def check_reservations():
#     # Replace this function with the actual check logic for reservations
#     # Here we just return False for the sake of demonstration
#     return False

# def reserve_test():
#     if click_button('images/view.png'):
#         time.sleep(2)
#         click_button('images/reserve_test.png')
#         return True
#     return False

# def main():
#     reservations_needed = 10
#     reservations_done = 0

#     while reservations_done < reservations_needed:
#         if not reserve_test():
#             click_button('images/next_available.png')
#             time.sleep(5)
#             pyautogui.scroll(-10000)  # Scroll to the bottom
#             time.sleep(2)
#             pyautogui.scroll(10000)  # Scroll to the top
#             time.sleep(2)
#             continue

#         if not click_button('view.png'):
#             tk.Tk().alert('No hay tests disponibles')
#             return
#         else:
#             pyautogui.alert('No hay tests disponibles')
#             return
        
#     while reservations_done < reservations_needed:
#             if reserve_test():
#                 reservations_done += 1
#                 if reservations_done >= reservations_needed:
#                     pyautogui.alert('Programa completado')
#                     return
#             else:
#                 time.sleep(5)
#                 if click_button('return_search.png'):
#                     time.sleep(5)
#                     break

#     time.sleep(5)  # Wait before looking for the next available slot

#     print(f'Proceso terminado. Reservas hechas: {reservations_done}')
    
# if __name__ == "__main__":
#     main()
import pyautogui
import time
from tkinter import messagebox
import tkinter as tk

def click_button(image, confidence=0.8, timeout=30):
    start_time = time.time()
    while time.time() - start_time < timeout:
        button_location = pyautogui.locateOnScreen(image, confidence=confidence)
        if button_location is not None:
            pyautogui.click(button_location)
            return True
        time.sleep(1)
    return False

def check_reservations():
    # Replace this function with the actual check logic for reservations
    # Here we just return False for the sake of demonstration
    return False

def reserve_test():
    if click_button('images/view.png'):
        time.sleep(2)
        while click_button('images/reserve_test.png'):
            time.sleep(1)
        return True
    return False

def main():
    reservations_needed = 10
    reservations_done = 0

    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal de Tkinter

    while reservations_done < reservations_needed:
        if not reserve_test():
            if click_button('images/next_available.png'):
                time.sleep(5)
                pyautogui.scroll(-10000)  # Scroll to the bottom
                time.sleep(2)
                pyautogui.scroll(10000)  # Scroll to the top
                time.sleep(2)
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
                time.sleep(5)
                if click_button('images/return_search.png'):
                    time.sleep(5)
                    break
                else:
                    messagebox.showinfo("Proceso terminado", f"Reservas hechas: {reservations_done}")
                    return

        time.sleep(5)  # Wait before looking for the next available slot

    messagebox.showinfo("Proceso terminado", f"Reservas hechas: {reservations_done}")
    print(f'Proceso terminado. Reservas hechas: {reservations_done}')

if __name__ == "__main__":
    main()

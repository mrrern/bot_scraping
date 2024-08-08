import pyautogui
import time

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
    if click_button('view_button.png'):
        time.sleep(1)
        click_button('reserve_test_button.png')
        return True
    return False

def main():
    reservations_needed = 10
    reservations_done = 0

    while reservations_done < reservations_needed:
        if not reserve_test():
            click_button('next_available_button.png')
            time.sleep(5)
            continue

        reservations_done += 1

        if check_reservations():
            break

        time.sleep(5)  # Wait before looking for the next available slot

    print(f'Proceso terminado. Reservas hechas: {reservations_done}')
    
if __name__ == "__main__":
    main()

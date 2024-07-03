from logic import login_and_book_test
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk


def submit_form():
    user_id = user_id_entry.get()
    password = password_entry.get()
    favorite_centre = favorite_centre_var.get()
    
    if not user_id or not password or favorite_centre == "Select favourite test centre group":
        messagebox.showerror(text="Error, Por favor, complete todos los campos.")
        return
    
    login_and_book_test(user_id, password, favorite_centre)

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Reservar Examen de Conducir")

tk.Label(root, text="User ID").grid(row=0, column=0)
user_id_entry = tk.Entry(root)
user_id_entry.grid(row=0, column=1)

tk.Label(root, text="Password").grid(row=1, column=0)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1)

tk.Label(root, text="Favorite Centre").grid(row=2, column=0)
favorite_centre_var = tk.StringVar()
favorite_centre_dropdown = ttk.Combobox(root, textvariable=favorite_centre_var)
favorite_centre_dropdown['values'] = ("Select favourite test centre group", "2nd Favorite", "3rd Favorite", "4th Favorite", "5th Favorite", "My Favorite")
favorite_centre_dropdown.grid(row=2, column=1)
favorite_centre_dropdown.current(0)

tk.Button(root, text="Submit", command=submit_form).grid(row=3, columnspan=2)

root.mainloop()
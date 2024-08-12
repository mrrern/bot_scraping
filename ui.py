from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
from punter import main as botin

def start_bot():
    botin() 

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Iniciar Bot")

# Create a clear and concise label to guide the user
label = tk.Label(root, text="Click the button to start the bot:")
label.pack(pady=20)

# Use a prominent button with "Iniciar Bot" (Start Bot) label
start_button = tk.Button(root, text="Iniciar Bot", command=start_bot, font=("Arial", 14, "bold"))
start_button.pack()

root.mainloop()

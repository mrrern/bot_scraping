from tkinter import messagebox
from tkinter import ttk
import tkinter as tk

def start_bot():
    # Replace this placeholder with your actual bot functionality,
    # potentially calling `login_and_book_test` if necessary.
    messagebox.showinfo(title="Bot Initiated", message="The bot is now running!")

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Iniciar Bot")  # Simplified title

# Create a clear and concise label to guide the user
label = tk.Label(root, text="Click the button to start the bot:")
label.pack(pady=20)  # Add some padding for better layout

# Use a prominent button with "Iniciar Bot" (Start Bot) label
start_button = tk.Button(root, text="Iniciar Bot", command=start_bot, font=("Arial", 14, "bold"))
start_button.pack()

root.mainloop()

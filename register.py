from database import register_user
import customtkinter as ctk
from tkinter import messagebox

def register_ui():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    root = ctk.CTk()
    root.title("Registro")
    window_width = 600
    window_height = 400
    root.resizable(False, False) # Impossibilitar maximizar janela
    root.iconbitmap("") # Icon do app

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width / 2) - (window_width / 2)
    y = (screen_height / 2) - (window_height / 2)

    root.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')

    title_label = ctk.CTkLabel(root, text="Registro", font=("Fixedsys", 24, "bold"))
    title_label.place(relx=0.5, rely=0.15, anchor='center')

    def register_user_inter():
        username = username_entry.get()
        password = password_entry.get()
        days_valid = int(days_entry.get())

        register_user(username, password, days_valid)
        messagebox.showinfo("Registro", "Usuário registrado com sucesso!")

    reg_frame = ctk.CTkFrame(root)
    reg_frame.place(relx=0.5, rely=0.5, anchor='center')

    ctk.CTkLabel(reg_frame, text="Usuário:").grid(row=0, column=0, padx=10, pady=5)
    username_entry = ctk.CTkEntry(reg_frame)
    username_entry.grid(row=0, column=1, padx=10, pady=5)

    ctk.CTkLabel(reg_frame, text="Senha:").grid(row=1, column=0, padx=10, pady=5)
    password_entry = ctk.CTkEntry(reg_frame, show='*')
    password_entry.grid(row=1, column=1, padx=10, pady=5)

    ctk.CTkLabel(reg_frame, text="Dias:").grid(row=2, column=0, padx=10, pady=5)
    days_entry = ctk.CTkEntry(reg_frame)
    days_entry.grid(row=2, column=1, padx=10, pady=5)

    register_button = ctk.CTkButton(reg_frame, text="Registrar", command=register_user_inter)
    register_button.grid(row=4, column=0, columnspan=2, pady=10)

    root.mainloop()

register_ui()

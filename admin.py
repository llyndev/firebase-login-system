# PAINEL DO ADMIN PARA ALTERAR A QUANTIDADE DE DIAS QUE O USUÁRIO TEM DE ACESSO AO SOFTWARE PRINCIPAL.
# INFORMANDO O USUÁRIO E A QUANTIDADE DE DIAS QUE ELE TERA ACESSO.

from database import register_user
import customtkinter as ctk

def create_register_ui():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    root = ctk.CTk()
    root.title("Registro de Usuário")
    window_width = 600
    window_height = 400
    root.resizable(False, False)
    root.iconbitmap("")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width / 2) - (window_width / 2)
    y = (screen_height / 2) - (window_height / 2)

    root.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')

    title_label = ctk.CTkLabel(root, text="Registro", font=("Fixedsys", 24, "bold"))
    title_label.place(relx=0.5, rely=0.15, anchor='center')

    def register_user_interface():
        username = username_entry.get()
        days_valid = int(days_entry.get())
        
        register_user(username, days_valid)

    reg_frame = ctk.CTkFrame(root)
    reg_frame.place(relx=0.5, rely=0.5, anchor='center')

    ctk.CTkLabel(reg_frame, text="Usuário:").grid(row=0, column=0, padx=10, pady=5)
    username_entry = ctk.CTkEntry(reg_frame)
    username_entry.grid(row=0, column=1, padx=10, pady=5)

    ctk.CTkLabel(reg_frame, text="Dias de Acesso:").grid(row=2, column=0, padx=10, pady=5)
    days_entry = ctk.CTkEntry(reg_frame)
    days_entry.grid(row=2, column=1, padx=10, pady=5)

    register_button = ctk.CTkButton(reg_frame, text="Registrar", command=register_user_interface)
    register_button.grid(row=4, column=0, columnspan=2, pady=10)

    root.mainloop()

create_register_ui()

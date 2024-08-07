# PAINEL DE REGISTRO

import customtkinter as ctk
from bdfire import load_database
from tkinter import messagebox
import bcrypt

# Configurações do Firebase
db = load_database()

# Função para abrir a interface de login
def open_login_ui():
    from login import main_ui
    main_ui()

# Função para retornar à tela principal
def back_to_main(root):
    from login import main_ui
    root.destroy()
    main_ui()

# Função para registrar um novo usuário
def register_user_interface(username, password, root):

    if not username or not password: # Verifica se nome de usuário ou senha estão vazios
        messagebox.showerror("Erro", "Nome de usuário e senha são obrigatórios.")
        return
    
    try:
        # Hash da senha usando bcrypt
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        user_data = db.child("users").child(username).get().val() # Verifica se o usuário já existe no banco de dados
        if user_data:
            messagebox.showerror("Erro", "Nome de usuário já existe.")
            return
        
        # Cria um dicionário com os dados do usuário
        user_data = {
            "password": hashed_password.decode('utf-8'), 
        }
        db.child("users").child(username).set(user_data) # Salva os dados do usuário no banco de dados

        messagebox.showinfo("Registro", "Usuário registrado com sucesso!")
        root.destroy()
        open_login_ui()
    
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível registrar o usuário: {e}")



# Função para criar a interface de registro de usuário
def register_ui():
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

    def on_register_click():
        username = username_entry.get()
        password = password_entry.get()
        register_user_interface(username, password, root)

    reg_frame = ctk.CTkFrame(root)
    reg_frame.place(relx=0.5, rely=0.5, anchor='center')

    ctk.CTkLabel(reg_frame, text="Usuário:").grid(row=0, column=0, padx=10, pady=5)
    username_entry = ctk.CTkEntry(reg_frame)
    username_entry.grid(row=0, column=1, padx=10, pady=5)

    ctk.CTkLabel(reg_frame, text="Senha:").grid(row=2, column=0, padx=10, pady=5)
    password_entry = ctk.CTkEntry(reg_frame, show='*')
    password_entry.grid(row=2, column=1, padx=10, pady=5)

    register_button = ctk.CTkButton(reg_frame, text="Registrar", command=on_register_click)
    register_button.grid(row=4, column=0, columnspan=2, pady=10)

    back_button = ctk.CTkButton(reg_frame, text="Voltar", command=lambda: back_to_main(root))
    back_button.grid(row=5, column=0, columnspan=2, pady=5)

    root.mainloop()

if __name__ == '__main__':
    register_ui()

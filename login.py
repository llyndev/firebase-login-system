from datetime import datetime
from dateutil import parser, tz
import customtkinter as ctk
import requests
from tkinter import messagebox
import pyrebase

firebase_config = {
    "apiKey": "YOUR_API_KEY",
    "authDomain": "YOUR_AUTH_DOMAIN",
    "databaseURL": "YOUR_DATABASE_URL",
    "projectId": "YOUR_ID",
    "storageBucket": "YOUR_STORAGE",
    "messagingSenderId": "YOUR_MESSAGING",
    "appId": "YOUR_APP_ID"
}

firebase = pyrebase.initialize_app(firebase_config)
db = firebase.database()

# Pegar o horario de uma API para evitar que o usuário burle
def get_current_time():
    try:
        response = requests.get("https://worldtimeapi.org/api/timezone/America/Sao_Paulo")
        response.raise_for_status()
        current_time = response.json()['datetime']
        return parser.isoparse(current_time).astimezone(tz.UTC)
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Erro", f"Não foi possível obter a hora atual: {e}")
        return None
    
def login_user(username, password):
    try:
        user_data = db.child("users").child(username).get().val()
        if user_data and user_data['password'] == password:
            current_time = get_current_time()
            if current_time is None:
                return
        
            expiration = datetime.strptime(user_data['expiration'], '%Y-%m-%d %H:%M:%S').replace(tzinfo=tz.UTC)
            if expiration >= current_time:
                messagebox.showinfo("Info", "Login bem-sucedido!")
                root.destroy()
            else:
                messagebox.showinfo("info", "Sua conta expirou!")
        else:
            messagebox.showerror("Error", "Usuário não encontrado ou senha incorreta!")
    except Exception as e:
        print("Erro ao fazer login", str(e))

if __name__ == '__main__':
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    root = ctk.CTk()
    root.title("Zenix")
    window_width = 600
    window_height = 400
    root.resizable(False, False)
    root.iconbitmap("")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width / 2) - (window_width / 2)
    y = (screen_height / 2) - (window_height / 2)

    root.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')

    title_label = ctk.CTkLabel(root, text="Login", font=("Fixedsys", 24, "bold"))
    title_label.place(relx=0.5, rely=0.2, anchor='center')

    login_frame = ctk.CTkFrame(root)
    login_frame.place(relx=0.5, rely=0.5, anchor='center')

    ctk.CTkLabel(login_frame, text="Usuário:").grid(row=0, column=0, padx=10, pady=5)
    user_entry = ctk.CTkEntry(login_frame)
    user_entry.grid(row=0, column=1, padx=10, pady=5)

    ctk.CTkLabel(login_frame, text="Senha:").grid(row=1, column=0, padx=10, pady=5)
    password_entry = ctk.CTkEntry(login_frame, show='*')
    password_entry.grid(row=1, column=1, padx=10, pady=5)

    login_button = ctk.CTkButton(login_frame, text="Login",
                                 command=lambda: login_user(user_entry.get(), password_entry.get()))
    login_button.grid(row=2, column=0, columnspan=2, pady=10)

    root.mainloop()

from datetime import datetime
from dateutil import parser, tz
import customtkinter as ctk
import requests
from tkinter import messagebox
import pyrebase

# Configurações do Firebase
firebase_config = {
    "apiKey": "YOUR_API_KEY",
    "authDomain": "YOUR_AUTH_DOMAIN",
    "databaseURL": "YOUR_DATABASE_URL",
    "projectId": "YOUR_ID",
    "storageBucket": "YOUR_STORAGE",
    "messagingSenderId": "YOUR_MESSAGING",
    "appId": "YOUR_APP_ID"
}

# Inicializa o aplicativo Firebase com a configuração fornecida
firebase = pyrebase.initialize_app(firebase_config)
db = firebase.database()

# Função para obter o horário atual de uma API para evitar manipulação de data
def get_current_time():
    try:
        # Faz uma requisição GET para a API de horário
        response = requests.get("https://worldtimeapi.org/api/timezone/America/Sao_Paulo")
        response.raise_for_status() # Levanta um erro para códigos de status HTTP ruins
        current_time = response.json()['datetime'] # Extrai o horário atual do JSON retornado
        return parser.isoparse(current_time).astimezone(tz.UTC) # Converte o horário para o fuso horário UTC
    except requests.exceptions.RequestException as e:
        # Exibe uma mensagem de erro se houver problemas com a requisição
        messagebox.showerror("Erro", f"Não foi possível obter a hora atual: {e}")
        return None
    
# Função para autenticar um usuário
def login_user(username, password):
    try:
        # Obtém os dados do usuário do Firebase
        user_data = db.child("users").child(username).get().val()
        if user_data and user_data['password'] == password: # Verifica se o usuário existe e a senha está correta
            current_time = get_current_time() # Obtém o horário atual
            if current_time is None:
                return # Se não conseguir obter o horário, encerra a função
        
            # Converte a data de expiração do usuário para o fuso horário UTC
            expiration = datetime.strptime(user_data['expiration'], '%Y-%m-%d %H:%M:%S').replace(tzinfo=tz.UTC)
            if expiration >= current_time: # Verifica se a conta ainda é válida
                messagebox.showinfo("Info", "Login bem-sucedido!")
                root.destroy() # Fecha a janela de login
                # AQUI DEVE CHAMAR A FUNÇÃO PARA ABRIR O PROGRAMA PRINCIPAL
            else:
                messagebox.showinfo("info", "Sua conta expirou!")
        else:
            messagebox.showerror("Error", "Usuário não encontrado ou senha incorreta!")
    except Exception as e:
        print("Erro ao fazer login", str(e))


# Código principal para configurar e iniciar a interface gráfica
if __name__ == '__main__':
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    root = ctk.CTk()
    root.title("Zenix")
    window_width = 600 # Largura da janela
    window_height = 400 # Altura da janela
    root.resizable(False, False) # Impede o redimensionamento da janela
    root.iconbitmap("") # Icon do app

    # Calcula as coordenadas para centralizar a janela na tela
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (window_width / 2)
    y = (screen_height / 2) - (window_height / 2)
    root.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}') # Define o tamanho e a posição da janela

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

from tkinter import messagebox
import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime, timedelta

# Carrega as credenciais do Firebase a partir de um arquivo JSON e inicializa a aplicação Firebase Admin
cred = credentials.Certificate("YOUR_CREDENTIALS")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'YOUR_CREDENTIALS' # URL do banco de dados em tempo real do Firebase
})

# Função para atualizar a data de expiração de um usuário
def days_user(username, days_valid):
    ref = db.reference('users') # Obtém a referência ao nó 'users' no banco de dados
    user_data = ref.child(username).get() # Obtém os dados do usuário a partir do banco de dados

    if user_data:
         # Calcula a nova data de expiração
        expiration_date = (datetime.now() + timedelta(days=days_valid)).strftime('%Y-%m-%d %H:%M:%S')

        # Atualiza a data de expiração do usuário no banco de dados
        ref.child(username).update({'expiration_date': expiration_date})
        messagebox.showinfo("Info", f"Data de expiração atualizada para o usuário: {username}")
    else:
        messagebox.showinfo("info", f"Usuário {username} não encontrado")
import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime, timedelta

# Carrega as credenciais do Firebase a partir de um arquivo JSON
cred = credentials.Certificate("YOUR_CREDENTIALS.JSON")

# Inicializa o aplicativo Firebase com as credenciais e a URL do banco de dados
firebase_admin.initialize_app(cred, {
    'databaseURL': 'YOUR_DATABASE_URL'
})

# Função para registrar um novo usuário
def register_user(username, password, days_valid):
    # Obtém uma referência ao nó 'users' no banco de dados Firebase
    ref = db.reference('users')

    # Calcula a data de expiração com base no número de dias válidos fornecidos
    expiration_date = (datetime.now() + timedelta(days=days_valid)).strftime('%Y-%m-%d %H:%M:%S')

    # Armazena os dados do usuário no banco de dados Firebase
    ref.child(username).set({
        'password': password, # Armazena a senha do usuário
        'expiration': expiration_date # Armazena a data de expiração da conta
    })
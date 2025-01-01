# login.py

# Usuário e senha armazenados para autenticação
USERS = {
    "admin": "123", # Exemplo de login e senha
    "user": "456" 
}

def verificar_login(username, password):
    """Função para verificar o login do usuário."""
    if USERS.get(username) == password:
        return True
    return False

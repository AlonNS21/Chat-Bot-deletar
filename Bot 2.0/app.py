# app.py
from flask import Flask, render_template, request, jsonify
from faq import obter_resposta
from login import verificar_login  # Importa a função de verificação de login

app = Flask(__name__)

# Rota principal para renderizar a página HTML
@app.route('/')
def index():
    return render_template('index.html')

# Rota para processar a pergunta e retornar a resposta
@app.route('/get_response', methods=['POST'])
def get_response():
    try:
        # Pega os dados de login
        username = request.json.get('username')
        password = request.json.get('password')
        
        # Verifica as credenciais de login
        if not verificar_login(username, password):
            return jsonify({"response": "Login ou senha inválidos."}), 403
        
        # Pega a mensagem do usuário
        user_message = request.json.get('message', '').strip().lower()
        user_name = username  # Nome do usuário para personalização da resposta
        
        if not user_message:
            return jsonify({"response": "Por favor, envie uma mensagem válida."}), 400

        # Obtém a resposta normalizada
        bot_response = obter_resposta(user_message, user_name)
        
        # Log básico no servidor
        print(f"[INFO] Mensagem de {user_name}: {user_message}")
        print(f"[INFO] Resposta do bot: {bot_response}")

        return jsonify({"response": bot_response})
    
    except Exception as e:
        print(f"[ERROR] Ocorreu um erro: {str(e)}")
        return jsonify({"response": "Desculpe, ocorreu um erro ao processar sua solicitação."}), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

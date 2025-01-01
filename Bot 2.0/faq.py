#faq.py

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from unidecode import unidecode  # Biblioteca para remover acentos
from loader import faq  # Lista de perguntas e respostas
from database import salvar_conversa  # Importa a função para salvar conversas

# Normaliza uma string (remove acentos e caracteres especiais)
def normalizar(texto):
    return unidecode(texto.lower())

# Vetoriza as perguntas normalizadas
perguntas = [normalizar(item[0]()) for item in faq]  # Executa as perguntas ao vetorizar
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(perguntas)  # Vetoriza as perguntas

def obter_resposta(pergunta_usuario, user_name):
    # Normaliza a pergunta do usuário
    pergunta_usuario_normalizada = normalizar(pergunta_usuario)
    
    # Transforma a pergunta do usuário em um vetor
    pergunta_usuario_vetor = vectorizer.transform([pergunta_usuario_normalizada])
    
    # Calcula a similaridade entre a pergunta do usuário e as perguntas armazenadas
    similaridades = cosine_similarity(pergunta_usuario_vetor, X)
    
    # Encontra o índice da pergunta mais semelhante
    indice_mais_semelhante = np.argmax(similaridades)
    
    # Verifica o valor da maior similaridade
    maior_similaridade = similaridades[0][indice_mais_semelhante]
    
    # Define um limiar de similaridade para garantir que a resposta seja relevante
    if maior_similaridade >= 0.5:  # Ajuste o valor do limiar conforme necessário
        # Chama a função de resposta associada
        resposta_func = faq[indice_mais_semelhante][1]
        resposta = resposta_func()  # Obtém a resposta
        
        # Salva a conversa no banco de dados (Excel)
        salvar_conversa(user_name, pergunta_usuario, resposta)
        
        return resposta
    else:
        resposta = "Desculpe, não entendi sua pergunta. Tente perguntar de outra forma."
        
        # Salva a conversa no banco de dados (Excel)
        salvar_conversa(user_name, pergunta_usuario, resposta)
        
        return resposta

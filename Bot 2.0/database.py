# database.py
import os
import pandas as pd
from datetime import datetime

# Função para criar a pasta 'conversas' se não existir
def criar_pasta_conversas():
    if not os.path.exists('conversas'):
        os.makedirs('conversas')

# Função para salvar a conversa no arquivo CSV
def salvar_conversa(usuario_nome, usuario_pergunta, bot_resposta):
    # Cria a pasta de conversas caso não exista
    criar_pasta_conversas()

    # Cria o nome do arquivo com base na data
    data_atual = datetime.now().strftime('%d-%m-%Y')
    nome_arquivo = f'conversas/conversas_{data_atual}.csv'

    # Verifica se o arquivo já existe
    if os.path.exists(nome_arquivo):
        # Se o arquivo existir, lê e adiciona a nova conversa
        df = pd.read_csv(nome_arquivo)
        nova_conversa = pd.DataFrame({
            'Usuário': [usuario_nome],  # Adiciona a coluna com o nome do usuário
            'Pergunta': [usuario_pergunta],
            'Resposta Bot': [bot_resposta]
        })
        df = pd.concat([df, nova_conversa], ignore_index=True)
    else:
        # Se não existir, cria um novo arquivo
        df = pd.DataFrame({
            'Usuário': [usuario_nome],  # Adiciona a coluna com o nome do usuário
            'Pergunta': [usuario_pergunta],
            'Resposta Bot': [bot_resposta]
        })

    # Salva o DataFrame no arquivo CSV
    df.to_csv(nome_arquivo, index=False, encoding='utf-8')

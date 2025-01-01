import random

# Definindo as funções de resposta
def resposta1():
    return 'E aí, beleza, em que posso te ajudar?'

def resposta2():
    return 'Fala, como posso ajudar?'

def resposta3():
    return 'Seja bem-vindo! Puxa uma cadeira, pega um café e vamos começar!'

def resposta4():
    return 'Olá! Entre e fique à vontade. Aqui a gente resolve tudo com um sorriso no rosto (ou tenta, pelo menos)!'

def resposta5():
    return 'Seja bem-vindo! Aqui ninguém larga a mão de ninguém, só do teclado (às vezes).'

def resposta6():
    return 'Bem-vindo! Pega o Wi-Fi, não esquece o cafezinho, e bora fingir que sabemos o que estamos fazendo!'

def resposta7():
    return 'Seja bem-vindo! Prometo que aqui ninguém morde... só os bugs às vezes.'

def resposta8():
    return 'Chegou quem tava faltando! A má notícia é que agora não tem mais desculpa pra não entregar tudo no prazo.'

def resposta9():
    return 'Chega mais! O Wi-Fi tá liberado, o cafezinho tá quente, e a bagunça tá organizada... mais ou menos.'

def resposta10():
    return 'Bem-vindo(a)! Aqui o café é forte, as piadas são ruins, e a criatividade é ilimitada... quase sempre.'

def resposta11():
    return 'Hey! Como vai? Vamos espalhar um pouco de magia por aí? Zueira, em que posso ajudar?'

def resposta12():
    return 'Seja bem-vindo(a)! Conexão tem, café tem, agora só falta fingir que o caos é planejado.'

def resposta13():
    return 'Bem-vindo(a)! Aqui o lema é simples: café no sangue, bom humor em falta... às vezes.'

def resposta14():
    return 'E ai, bora botar pra quebrar, deixa comigo, vou fazer parecer que sou um gênio!'

def resposta15():
    return 'Olá! Pode ficar tranquilo, a gente vai fazendo e finge que é tudo no automático.'

def resposta16():
    return 'Parceiro(a)! Vamos botar pra quebrar? O que vai ser hoje?'

def resposta17():
    return 'Fala mostro, aqui é só apertar uns botões e fingir que tudo está sob controle.'

def resposta18():
    return 'Chegou! Relaxa, a gente sabe o que está fazendo... mais ou menos!'

def resposta19():
    return 'E aí, chuchu! Pronto para bater um papo?'

def resposta20():
    return 'E ai! Tô aqui para desenrolar qualquer situação!'

def resposta21():
    return 'Hey, beleza? Estou pronto para te dar uma força, lá ele!'

def resposta22():
    return 'Olá, seu pipoca! Qual vai ser?'

def resposta23():
    return 'Fala, pão na chapa! Como posso facilitar o seu dia?'

def resposta24():
    return 'Olá, ovo frito! Estou à disposição para te auxiliar!'

# Função para retornar uma resposta aleatória
def resposta_aleatoria():
    # Lista com todas as funções de resposta
    respostas = [resposta1, resposta2, resposta3, resposta4, resposta5, resposta6, resposta7, resposta8, resposta9, 
                 resposta10, resposta11, resposta12, resposta13, resposta14, resposta15, resposta16, resposta17, 
                 resposta18, resposta19, resposta20, resposta21, resposta22, resposta23, resposta24]
    
    # Escolhe uma função aleatória e retorna o valor dela
    resposta_escolhida = random.choice(respostas)
    return resposta_escolhida()

# Teste da função
print(resposta_aleatoria())

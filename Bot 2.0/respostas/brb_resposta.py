# brb_resposta.py

def resposta_sabe_brb():
    resposta = (
        "O Banco de Brasília (BRB) é uma instituição financeira pública brasileira que tem como objetivo oferecer serviços bancários para pessoas físicas e jurídicas.<br><br>"
        "E as atividade que sei referente é:<br><br>"
        "1 - Passo a passo de rotina de processos BRB.<br>"
        "2 - Como enviar o e-mail para o BRB solicitando a Lei, data do extrato e valor atualizado.<br>"
        "3 - O que fazer caso o BRB não indentifique o Alvará.<br>"
        "4 - Como fazer boleto de deposito judical BRB.<br>"
        "5 - Como fazer um DAE Tributario para para pagamento do BRB"
        
    )
    return resposta




def resposta_deveolver_alvara():
    pdf_link = r"https://drive.google.com/file/d/1D2FR0Zh8tt4YhfDiqxOnExiz5Vkio5zw/view?usp=sharing"
    resposta = (
        "Caso o BRB não indentifique o Alvará basta devolver o processo para PGE/PROFIS.<br><br>"
        
        "Clique no link abaixo para ver um exemplo em PDF 👇.<br><br>"
        
        f'Link: "{pdf_link}".'
        
    )
    return resposta
    

def resposta_dae_brb():
    # Aqui você define a resposta específica para ativar o credor
    pdf_link = r"https://drive.google.com/file/d/11PY1R2z1L2EzdzuXTjqJD96TOT9KZLbH/view?usp=sharing"
    resposta = (
        
        "No caso do BRB o DAE é Tributario, isso significa que so a GEARC pode faze-lo."
        
        "Caso prceise fazer um DAE Tributario para para pagamento do BRB, basta emaninha o processo para a GEARC com o despacho informado o valor.\n\n"
        
        "Clique no link abaixo para ver um exemplo em PDF 👇.<br><br>"
        
        f'Link: "{pdf_link}".'
        
    )
    return resposta

def resposta_rotina_brb():
    # Aqui você define a resposta específica para ativar o credor
    pdf_link = r"https://drive.google.com/file/d/15JWqX7zKQadeTT_-nmmQxY1iMZ__rAn_/view?usp=sharing"
    pdf_link2 = r"https://drive.google.com/file/d/1awmRyOQZHijEfqkLfRPOezS9EiO7qn5B/view?usp=sharing"
    pdf_link3 = r"https://drive.google.com/file/d/14QKsVhtC95QQ9N_P7yJkGlcmBQpqhJ8A/view?usp=sharing"
    resposta = (
       
        "Passo a passo da rotina de processo do BRB, mostrando os principais topicos:<br><br>"
        
        "Anexar extrato do BRB, atentar a solicitação do processo, isso é verificar a Execução Fiscal e comparar com a da planiljas para ver se ja foi pago.(PAG. 01).<br><br>"
        "Encaminhar e-mail para o BRB para possiveis solicitações.(PAG. 01 A 02).<br><br>"
        "Encaminhar despacho para a GECRED, para uma possivel emição de DAE Tributario, lembrando que para cada quitação de DAE seja AI, PAF, DD vai conter dois DAE's.(PAG. 02)<br><br>"
        "Sobre processo de Honorários de Sucumbência.(PAG. 03)<br><br>"
        
        "E se possivel processo que ja foi pago, encaminhar processo de volta a PGE em um despacho.(PAG. 03).<br><br>"
        "Clique no link abaixo para ver um exemplo em PDF 👇.<br><br>"
        f"Link: ({pdf_link}.<br><br>"
        f"Obs.: Para identificar qual tipo de processo para encaminhar e-mail, solictando solicitando a Lei, data do extrato e valor atualizado, so procurar um dessse documentos clique em um dos links abaixo:<br><br>"
        f"So precisa da Lei ({pdf_link2})<br><br>"
        f"Precisa lei, data do extrato e valor atualizado ({pdf_link3})" 
    )
    return resposta
    
def resposta_email_brb():
    # Aqui você define a resposta específica para ativar o credor
    
    pdf_link2 = r"https://drive.google.com/file/d/17JJO0ugTGkRbBSOer3liBgFOxNOn0tQN/view?usp=sharing"
    pdf_link3 = r"https://drive.google.com/file/d/1saJSqiITzdPN570uyUBWaCV0jPuFG8XG/view?usp=sharing"
    
    pdf_link4 = r"https://drive.google.com/file/d/1awmRyOQZHijEfqkLfRPOezS9EiO7qn5B/view?usp=sharing"
    pdf_link5 = r"https://drive.google.com/file/d/14QKsVhtC95QQ9N_P7yJkGlcmBQpqhJ8A/view?usp=sharing"
    resposta = (
        
        "Para enviar o e-mail para o BRB solicitando a Lei, data do extrato e valor atualizado seram modelos de e-mails um pouco difrentes.<br><br>"
        
        "OBS.: Precisamos do pedido da lei para saber qual a lei que a conta esta vinculada.<br><br>"
        
        "1° Modelo - Solicitando a Lei:<br><br>"
        "Assunto:<br>" 
        "Identificação de valores creditados na conta corrente 344.253.143-0.<br><br>"
        "Mensagem:<br>"
        "Prezados bom dia/boa tarde.<br><br>"
        "Solicito, por gentileza, identificar a que lei estão vinculados os alvarás abaixo creditados na conta corrente 344.253.143-0.<br><br>"
        
        "OBS.: Sera enviado uma tabela com as informações necessarias como mostra o link abaixo 👇:<br><br>"
        
        f"Link: ({pdf_link2})<br><br>"
        
        "2° Modelo - Solicitando a Lei, data do extrato e valor atualizado:<br><br>"
        "Assunto:<br>" 
        "Identificação de valores creditados na conta corrente 344.253.143-0.<br><br>"
        "Mensagem:<br>"
        "Prezados bom dia/boa tarde<br>"
        "Solicito, por gentileza, identificar a que lei, a data do extrato e o valor atualizado que estão vinculados os alvarás abaixo creditados na conta corrente 344.253.143-0.<br><br>"
        
        "OBS.: Sera enviado uma tabela com as informações necessarias como mostra o link abaixo 👇:"
        
        f"Link: ({pdf_link2})<br><br>"
        
        "O e-mail sera encaminhado para os demais a baixo:<br><br>"
        
        "Para:<br><br>"
        "#Gerente de Equipe - GEDEB <equipegedeb@brb.com.br>;Natalia Duarte de Andrade <natalia.andrade@brb.com.br>;Gerente GEDEB <gedeb@brb.com.br>; #Gerente Geral PA FRB<ggfrb@brb.com.<br><br>"
        
        "Com copia para:<br><br>"
        "<sbotelho@sefaz.ba.gov.br> <csilva@sefaz.ba.gov.br> <mpfreitas@sefaz.ba.gov.<br><br>"
        
        f"Aqui esta como o BRB respondera o e-mail como mostra o link abaixo 👇:"
        
        f"Link: ({pdf_link3})<br><br>"
        
        f"Obs.: Para identificar qual tipo de processo para encaminhar e-mail, solictando solicitando a Lei, data do extrato e valor atualizado, so procurar um dessse documentos:<br><br>"
        f"So precisa da Lei ({pdf_link4})<br><br>"
        f"Precisa lei, data do extrato e valor atualizado ({pdf_link5})"
    )
    return resposta
   
   # Boleto BRB
def resposta_boleto_brb():
    pdf_link = "https://drive.google.com/file/d/103FRmhcU3sHDcsiOJMOGp4RkneuNwm36/view?usp=drive_link"
    resposta = (
        "Boleto de deposito judical BRB.<br><br>"
        
        "Clique no link abaixo para ver um exemplo em PDF de como fazer boleto de deposto judical do BRB 👇.<br><br>"

        f'Link: "{pdf_link}".'
        
        
    )
    return resposta 
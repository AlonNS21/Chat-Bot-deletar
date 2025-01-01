# receita_reposta.py
def resposta_receita_integrada():  
    resposta = (
        "Receita integrada.<br><br>"
        "Começa após o pagamento do DAE efetuado pelo contribuinte, o SIGAT recebe essas informações e as trata em seu banco de dados.<br><br>"
        "Em seguida passa por três processo Arrecadação, Repasse, classificada, e Regularização da RSS.<br><br>"

        "Arrecadação:<br><br>"
        "Durante a noite, o FIPLAN consome as informações dos DAE’s usando o banco de dados do SIGAT, gerando assim os DAE’s tributários e em seguida os DAE’s orçamentários que são divididos pela a receia, registrando assim a AVR (Aviso de credito).<br><br>"

        "OBS: A limitação é de: 45.000 unidades/dia em 3 lotes, 15.000 em cada lote.<br><br>"

        "Repasse:<br><br>" 
        "Depois de 2 dias o FIPLAN registra os DAC a partir dos repasses informado no SIGAT.<br><br>"

        "Classificada:<br><br>"
        "Gerou a RSS?<br><br>"
        "Se sim, irá registrar a RSS, por convênio, que será visualizada em dois dias (D+2), pois o DAC é processado na madrugada.<br>"
        "Se não, os documentos não casados ficam na Vala.<br><br>"
        "Os documentos na vala serão precisos fazer a Regularização da RSS manual, depois da regularização manual se o DAC for igual a AVR registrará a RSS, caso contrário voltará para a vala, esperando novos registro DAC (Repasses).<br><br>"

        "Regularização da RSS:<br><br>"
        "A RSS é regularizada automaticamente pelo FIPLAN, mas caso haja algum pendencia terá que fazer a regularização manualmente.<br><br>"
        "Regularizar a RSS manualmente no FIPLAN, depois emitir e analisar Relatório FIP 712A (Relatório Financeiro).<br><br>"
        
        "A análise do resultado do relatório FIP712A para não haver pendencias tem que está AVR=DAC=RSS, isto é, AVR-DAC e DAC-RSS zerados!<br><br>"
        "Analise do resultado do relatório FIP712A, RSS não gerada (AVR≠DAC), impacta na apuração diária do FUNCEP, pagamento de DAE por outro órgão."    
    )
    return resposta

def resposta_avr_maior_dac():
    resposta = (
        
    "AVR maior que DAC, com um valor positivo, significa que na coluna AVR-DAC exsite mais AVR do que DAC.<br><br>"
    
    "Caso a AVR esteja maior que o DAC isso geralmente tem a ver com o parcelamento.<br>"
    "OBS.: Pois o banco faz o repasse no último dia do mês, GEARC faz controle em planilha Excel e em seguida a GEARC envia a planilha de controle para DEPAT e para o BANCO.<br><br>"
    
    "A diferença devida ao parcelamento, processo de repasse das receitas em função do parcelamento, acompanhar durante o mês se o valor será repassado pelo banco no final do mês.<br>"
    "OBS 2.: O parcelamento é inicialmente enviado para uma conta especifica, com o controle da GEARC o banco faz as contas especificas de arrecadação.<br><br>"
    
    "Caso a diferença não é devido ao parcelamento, informar a GEARC para verificar o problema, em seguida só aguardar a GEARC resolver o problema.<br>"
    "OBS 3.: situações: Banco não enviar ou SIGAT não liberar repasse, problemas na integração, etc. O problema será resolvido.<br><br>"
    
     
         
    )
    return resposta

def reposta_avr_menor_dac():  
    resposta = (
    
    "AVR menor que o DAC, signfica que que na coluna AVR-DAC o valor estará negativo, tendo mais DAC que AVR.<br><br>"
    
   "Quando a AVR está menor que o DAC isso pode a ver inúmeros problemas, vou explicar;<br><br>"
   " 1 - DAEs não processados, o sistema não conseguiu processá-los por algum motivo, podendo assim forçar um processamento, no caso processá-los manualmente.<br>"
    "2 - Credor não cadastrado, os credores são as pessoas que pagaram o DAE, e assim terá que cadastra-los no banco de dados do FIPLAN, para assim o problema desaparecer, esse procedimento é feito pela COEFI.<br>"
    "3 - Natureza da Receita não cadastrada (NR), para solucionar, basta Solicitar a GERAC o cadastro da Natureza da Receita assim a GERAC aciona a SEPLAN para realizar o cadastro. Em caso de apenas parametrização da Natureza da Receita no FIPLAN, a GERAC resolve.<br>"
    "4 - Código de tributo não cadastrado, terá que solicitar a GERAC castro do código do tributo, a GERAC aciona a SAT/DARC para realizar o cadastro.<br>"
    "5 – Outros casos: Informar para GERAC verificar o problema, que pode ser pendencia de processamento de arrecadação no SIGAT ou na PRODEB, envio no arquivo pelo banco, etc.<br>"
    "Cadastro de credor realizado, Natureza da receita cadastrada ou apenas parametrizada, código do tributo cadastrada pela DARC ou pedir para GERAC verificar se a problema no processamento da arrecadação no SIGAT ou PRODEB.<br>"
    "Aguardar o sistema processar AVR/DAC na rotina automática.<br>"
    "6 - DAEs represados Solicitar a GDSAF carga extra de obtenção e processamento de DAE.<br><br>"
    "OBS.: Esse processo acontece durante o dia.<br><br>"
    
    "A SEFAZ/ DEPAT solicita abrir o ticket para a PRODEB realizar   processamento, caso processamento finalizado, informar a SAFAZ/ DEPAT.<br><br>" 
    "O processamento é finalizado após 17h aguardar o sistema processar AVR/DAC na rotina automática, processamento finalizado até início da tarde.<br><br>"
    "Depois é só processar o DAE manualmente, processar AVR manualmente e Processar Regularização de RSS manualmente.<br><br>" 
    "AVR processada?  RSS regularizada (até a data analisada).<br><br>"
    "AVR não processada? Aguardar o sistema processar AVR/DAC na rotina automática, no dia seguinte emitir o relatório FIP712A (Financeiro), verificar se AVR=DAC=RSS.<br><br>"
    "Caso a AVR esteja menor que o DAC, reportar problema para GERAC/GEARC/GDSAF e aguardar retorno dos setores responsáveis.<br><br>"
    "OBS: Problema na integração, doc de arrecadação não apropriado pelo SIGAT, receita sem código cadastrado.<br><br>"  
    "Problema resolvido!<br><br>"
    
    )
    return resposta


def resposta_fechamento_receita_integrada():
    resposta = (
    
    "Emitir relatório FIP712(contábil).<br><br>"
    
    "No final do mês conforme se o valor do parcelamento foi repassado, emitir relatório FIP712A (Financeiro) do mês. Para confirmar se AVR=DAC=RSS no mês, indicando que a RSS foi regularizada com sucesso e que não à pendencia no mês.<br><br>" 
    "Emitir relatório FIP712 (Contábil), caso a RSS não gerada dando indicio que a AVR está diferente do DAC (AVR≠DAC), é possível efetuar a correção dentro do mês.<br><br>" 
    "Emitir relatório FIP712(contábil).<br><br>"
    "AVR=DAC=RSS, RSS regularizada no automaticamente do mês pelo FIPLAN (Contábil)<br><br>"
    "-FIM!<br><br>"
    
    "RSS não gerada (AVR=DAC≠RSS), emitir relatório consulta AVR c/ indicativo de RSS – Não.<br><br>"
    "OBS: Verificar se há AVR/DAC sem RSS de mês anterior.<br><br>" 
    "Regularizar RSS nas datas de arrecadação correspondente às AVR do relatório.<br><br>"
    "Emitir novamente do FIP712A (contábil).<br><br>"
    "OBS: O mês pode ser fechado com diferença no relatório em caso de algum problema não resolvido.<br><br>" 
    "Mapear as diferenças encontradas para ajuste/correções no mês seguinte.<br><br>"
    "RSS regularizada no fechamento do mês no FIPLAN.<br><br>"
    "-FIM!" 
    )
    return resposta

def reposta_avr():    
    resposta = (
    
    "AVR é um aviso de Cerdito, faz parte da arrecadação.<br><br>"
    
    "Ainda sera incluido mais informações.<br><br>"
    )
    return resposta


def resposta_dac():
    resposta = (
    
    "DAC é o documento de aviso de credtito, faz parte dp repasse.<br><br>"
    
    "Ainda sera incluido mais informações.<br><br>"
    )
    return resposta

def resposta_rss():
    resposta = (
    
    "Sem informções ate o momento..."
    
    )
    return resposta

def resposta_avr_dac_rss():
    resposta = (
    
    "Se AVR-DAC e DAC-RSS estivem zeradas(0), significa que não a pendência para ser resolvidas."
    )
    return resposta


def resposta_dac_rss_negativa():
    resposta = (
    
    "Sempre vai ser um valor positivo indicando que a AVR-DAC esta com pendências, assim pendendo esse valor, ou zerado indicando que não tem pendências.<br><br>"
    
    "O DAC-RSS não deve acontecer nunca!<br>"
    "A RSS é o prduto do AVR e do DAC, se DAC-RSS é negativo, está dizendo que ele vai gerar a RSS sem ter DAC, um fato praticamente impossivel."
 
    )
    return resposta


def resposta_avr_zerada():    
    resposta = (
    
    "AVR zerada indica que não holve arrecadação.<br><br>"
    
    "Outro suposto indicativo:<br>"
    "Se for do convenio 0001 (ICMS) pode ser por causa do SIMPLES NACIONAL.<br>"
    "Aparentimente é normal, pois a informação so chega 2 dias depois."
    )
    return resposta


def resposta_dac_zerada():    
    resposta = (
    
    "Se o DAC estiver zerado, significa que Moreno não lançou o repasse, ou pode ser que o FIPLAN não conseguiu processar.<br><br>"
    "Dai tem que avaliar se seria algum problema na integração.<br><br>"
    
    "Assim como o DAC não ter AVR, também pode ser por problema de integração.<br><br>"
    
    "Tem que acompanhar e avaliar!"
    
    
    )
    return resposta

def resposta_rss_zerada():
    resposta = (
    
    "RSS zerada(0), significa que não holve o 'Casamento' da AVR e DAC ou DAC e AVR.<br><br>"
    
    "Outro suposto indicativo:<br>"
    "Se for do convenio 0001 (ICMS) pode ser por causa do SIMPLES NACIONAL.<br>"
    "Aparentimente é normal, pois a informação so chega 2 dias depois."
    
    )
    return resposta
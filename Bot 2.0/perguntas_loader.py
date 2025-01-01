#perguntas.py
def carregar_perguntas():
    """Retorna uma lista de perguntas associadas com suas funções de respostas"""
    from respostas.saldacoes_resposta import resposta_aleatoria
    from perguntas.saldacoes_pergunta import pergunta_saldacao
    # Receita
    from respostas.receita_reposta import resposta_receita_integrada, resposta_avr_maior_dac, reposta_avr_menor_dac, resposta_fechamento_receita_integrada, reposta_avr, resposta_dac, resposta_rss, resposta_avr_dac_rss, resposta_dac_rss_negativa, resposta_avr_zerada, resposta_dac_zerada, resposta_rss_zerada
    from perguntas.receita_perguntas import pergunta_receita_integrada, pergunta_avr_maior_dac, pergunta_avr_menor_dac, pergunta_fechamento_receita_integrada, pergunta_avr, pergunta_dac, pergunta_rss, pergunta_avr_dac_rss, pergunta_dac_rss_negativa, pergunta_avr_zerada, pergunta_dac_zerada, pergunta_rss_zerada
    # E-mail
    from respostas.email_resposta import resposta_ativar_credor, resposta_concluir_processo_aj, resposta_credor_pagamento_fatura, reposta_pagamento_nao_efetivado, resposta_inativar_conta_bancaria, resposta_fale_consco_rest, resposta_reset_senha_rede, resposta_cadastro_agencia_bancaria
    from perguntas.email_pergunta import pergunta_ativar_credor, pergunta_concluir_processo_aj, pergunta_credor_pagamento_fatura, pagamento_nao_efetivado, pergunta_inativar_conta_bancaria, pergunta_fale_consco_rest, pergunta_reset_senha_rede, pergunta_cadastro_agencia_bancaria
    # Comandos para bancos
    from respostas.coman_bancos_resposta import resposta_bb_pupanca, resposta_cef_pupanca, resposta_bancos
    from perguntas.coman_bancos_pergunta import pergunta_bb_pupanca, pergunta_cef_pupanca, pergunta_bancos
    # Passo a passo 
    from respostas.passos_resposta import resposta_pagamento_detran, resposta_rotina_deposito_judicial, resposta_incluir_nex
    from perguntas.passos_pergunta import pergunta_pagamento_detran, pergunta_rotina_deposito_judicial, pergunta_incluir_nex
    # Lista telefone / Ramal.
    from respostas.ramal_resposta import resposta_ramal_telefone
    from perguntas.ramal_pergunta import pergunta_ramal_telefone
    # BRB
    from respostas.brb_resposta import resposta_dae_brb, resposta_deveolver_alvara, resposta_email_brb, resposta_rotina_brb, resposta_boleto_brb, resposta_sabe_brb
    from perguntas.brb_pergunta import pergunta_dae_brb, pergunta_deveolver_alvara, pergunta_email_brb, pergunta_rotina_brb, pergunta_boleto_brb, pergunta_sabe_brb
    # Fiplan 
    from respostas.fiplan_resposta import resposta_credor, resposta_dr, resposta_nex, resposta_nob, resposta_noe, resposta_numero_credor, resposta_numero_documento, resposta_ped, resposta_sistema_fiplan, resposta_unidade_getora_executora
    from perguntas.fiplan_pergunta import pergunta_credor, pergunta_dr, pergunta_nex, pergunta_nob, pergunta_noe, pergunta_numero_credor, pergunta_numero_documento, pergunta_ped, pergunta_sistema_fiplan, pergunta_unidade_getora_executora
    #xingamentos
    from xingamentos.swearing_resposta import resposta_xingamento_idiota, resposta_xingamento_burro, resposta_xingamento_estupido, resposta_xingamento_merda, resposta_xingamento_palhaco, resposta_xingamento_imbecil, resposta_xingamento_otario, resposta_xingamento_besta, resposta_xingamento_corino, resposta_xingamento_analfabeto, resposta_xingamento_vagabundo, resposta_xingamento_ze_ruela, resposta_xingamento_feio, resposta_xingamento_burra, resposta_xingamento_lixo, resposta_xingamento_foca, resposta_xingamento_cavalo, resposta_xingamento_porco, resposta_xingamento_trouxa, resposta_xingamento_boco, resposta_xingamento_chato, resposta_xingamento_pateta, resposta_xingamento_cabeludo, resposta_xingamento_pato, resposta_xingamento_vaca, resposta_xingamento_cadela, resposta_xingamento_bicho, resposta_xingamento_aleijado, resposta_xingamento_baleia, resposta_xingamento_saco, resposta_xingamento_piranha, resposta_xingamento_esquisito, resposta_xingamento_galinha, resposta_xingamento_frouxo, resposta_xingamento_mermao, resposta_xingamento_bicho_papao, resposta_xingamento_pirralho, resposta_xingamento_cachorrinho, resposta_xingamento_lambedor, resposta_xingamento_safado, resposta_xingamento_vagabunda, resposta_xingamento_gordo, resposta_xingamento_viado, resposta_xingamento_lerdo, resposta_xingamento_imbecil, resposta_xingamento_panaca, resposta_xingamento_gamba, resposta_xingamento_ze_buceta, resposta_xingamento_liso, resposta_xingamento_tosco, resposta_xingamento_miseravel, resposta_xingamento_patife, resposta_xingamento_sacana, resposta_xingamento_vai_tomar_no_cu, resposta_xingamento_se_fode, resposta_xingamento_vai_se_ferrar, resposta_xingamento_vai_pra_puta_que_pariu, resposta_xingamento_vai_se_lascar, resposta_xingamento_vai_pro_inferno, resposta_xingamento_caralho, resposta_xingamento_puta_que_pariu, resposta_xingamento_filho_da_puta, resposta_xingamento_saco_de_merda, resposta_xingamento_vai_tomar_no_olho_do_cu, resposta_xingamento_merda_de_pessoa, resposta_xingamento_cala_a_boca, resposta_xingamento_vai_se_foder, resposta_xingamento_sua_puta, resposta_xingamento_vai_tomar_no_cuzinho, resposta_xingamento_vai_se_lascar_bem_longe, resposta_xingamento_vai_tomar_no_seu_cu_sujo, resposta_xingamento_porra, resposta_xingamento_vai_tomar_no_seu_cu_gordo, resposta_xingamento_vai_se_foder_bem_gostoso, resposta_xingamento_seu_imbecil, resposta_xingamento_vai_pra_puta_que_pariu_agora, resposta_xingamento_vai_se_fuder_mais_um_pouco, resposta_xingamento_sua_vaca, resposta_xingamento_puta_merda, resposta_xingamento_vai_se_fuder_pra_puta_que_pariu, resposta_xingamento_vai_se_ferrar_no_seu_cu, resposta_xingamento_vai_tomar_no_meio_do_cu, resposta_xingamento_seu_filho_da_puta, resposta_xingamento_vai_pro_inferno, resposta_xingamento_porra_nenhuma, resposta_xingamento_sua_puta, resposta_xingamento_cai_na_porra_do_poco, resposta_xingamento_vai_se_lascar_bem_fundo, resposta_xingamento_vai_se_foder_que_nem_um_animal, resposta_xingamento_caralho_que_merda, resposta_xingamento_voce_e_um_lixo
    from xingamentos.swearing_pergunta import pergunta_xingamento_idiota, pergunta_xingamento_burro, pergunta_xingamento_estupido, pergunta_xingamento_merda, pergunta_xingamento_palhaco, pergunta_xingamento_imbecil, pergunta_xingamento_otario, pergunta_xingamento_besta, pergunta_xingamento_corino, pergunta_xingamento_analfabeto, pergunta_xingamento_vagabundo, pergunta_xingamento_ze_ruela, pergunta_xingamento_feio, pergunta_xingamento_burra, pergunta_xingamento_lixo, pergunta_xingamento_foca, pergunta_xingamento_cavalo, pergunta_xingamento_porco, pergunta_xingamento_trouxa, pergunta_xingamento_boco, pergunta_xingamento_chato, pergunta_xingamento_pateta, pergunta_xingamento_cabeludo, pergunta_xingamento_pato, pergunta_xingamento_vaca, pergunta_xingamento_cadela, pergunta_xingamento_bicho, pergunta_xingamento_aleijado, pergunta_xingamento_baleia, pergunta_xingamento_saco, pergunta_xingamento_piranha, pergunta_xingamento_esquisito, pergunta_xingamento_galinha, pergunta_xingamento_frouxo, pergunta_xingamento_mermao, pergunta_xingamento_bicho_papao, pergunta_xingamento_pirralho, pergunta_xingamento_cachorrinho, pergunta_xingamento_lambedor, pergunta_xingamento_safado, pergunta_xingamento_vagabunda, pergunta_xingamento_gordo, pergunta_xingamento_viado, pergunta_xingamento_lerdo, pergunta_xingamento_imbecil, pergunta_xingamento_panaca, pergunta_xingamento_gamba, pergunta_xingamento_ze_buceta, pergunta_xingamento_liso, pergunta_xingamento_tosco, pergunta_xingamento_miseravel, pergunta_xingamento_patife, pergunta_xingamento_sacana, pergunta_xingamento_vai_tomar_no_cu, pergunta_xingamento_se_fode, pergunta_xingamento_vai_se_ferrar, pergunta_xingamento_vai_pra_puta_que_pariu, pergunta_xingamento_vai_se_lascar, pergunta_xingamento_vai_pro_inferno, pergunta_xingamento_caralho, pergunta_xingamento_puta_que_pariu, pergunta_xingamento_filho_da_puta, pergunta_xingamento_saco_de_merda, pergunta_xingamento_vai_tomar_no_olho_do_cu, pergunta_xingamento_merda_de_pessoa, pergunta_xingamento_cala_a_boca, pergunta_xingamento_vai_se_foder, pergunta_xingamento_sua_puta, pergunta_xingamento_vai_tomar_no_cuzinho, pergunta_xingamento_vai_se_lascar_bem_longe, pergunta_xingamento_vai_tomar_no_seu_cu_sujo, pergunta_xingamento_porra, pergunta_xingamento_vai_tomar_no_seu_cu_gordo, pergunta_xingamento_vai_se_foder_bem_gostoso, pergunta_xingamento_seu_imbecil, pergunta_xingamento_vai_pra_puta_que_pariu_agora, pergunta_xingamento_vai_se_fuder_mais_um_pouco, pergunta_xingamento_sua_vaca, pergunta_xingamento_puta_merda, pergunta_xingamento_vai_se_fuder_pra_puta_que_pariu, pergunta_xingamento_vai_se_ferrar_no_seu_cu, pergunta_xingamento_vai_tomar_no_meio_do_cu, pergunta_xingamento_seu_filho_da_puta, pergunta_xingamento_porra_nenhuma, pergunta_xingamento_cai_na_porra_do_poco, pergunta_xingamento_vai_se_lascar_bem_fundo, pergunta_xingamento_vai_se_foder_que_nem_um_animal, pergunta_xingamento_caralho_que_merda, pergunta_xingamento_voce_e_um_lixo


    




    
    
    return [
    (pergunta_saldacao, resposta_aleatoria),
    (pergunta_bancos, resposta_bancos),
    (pergunta_receita_integrada, resposta_receita_integrada),
    (pergunta_avr_maior_dac, resposta_avr_maior_dac),
    (pergunta_avr_menor_dac, reposta_avr_menor_dac),
    (pergunta_fechamento_receita_integrada, resposta_fechamento_receita_integrada),
    (pergunta_avr, reposta_avr),
    (pergunta_dac, resposta_dac),
    (pergunta_rss, resposta_rss),
    (pergunta_avr_dac_rss, resposta_avr_dac_rss),
    (pergunta_dac_rss_negativa, resposta_dac_rss_negativa),
    (pergunta_avr_zerada, resposta_avr_zerada),
    (pergunta_dac_zerada, resposta_dac_zerada),
    (pergunta_rss_zerada, resposta_rss_zerada),
    (pergunta_ativar_credor, resposta_ativar_credor),
    (pergunta_concluir_processo_aj, resposta_concluir_processo_aj),
    (pergunta_credor_pagamento_fatura, resposta_credor_pagamento_fatura),
    (pagamento_nao_efetivado, reposta_pagamento_nao_efetivado),
    (pergunta_inativar_conta_bancaria, resposta_inativar_conta_bancaria),
    (pergunta_fale_consco_rest, resposta_fale_consco_rest),
    (pergunta_reset_senha_rede, resposta_reset_senha_rede),
    (pergunta_cadastro_agencia_bancaria, resposta_cadastro_agencia_bancaria),
    (pergunta_bb_pupanca, resposta_bb_pupanca),
    (pergunta_cef_pupanca, resposta_cef_pupanca),
    (pergunta_boleto_brb, resposta_boleto_brb),
    (pergunta_pagamento_detran, resposta_pagamento_detran),
    (pergunta_rotina_deposito_judicial, resposta_rotina_deposito_judicial),
    (pergunta_incluir_nex, resposta_incluir_nex),
    (pergunta_ramal_telefone, resposta_ramal_telefone),
    (pergunta_deveolver_alvara, resposta_deveolver_alvara),
    (pergunta_sabe_brb,resposta_sabe_brb),
    (pergunta_dae_brb, resposta_dae_brb),
    (pergunta_rotina_brb, resposta_rotina_brb),
    (pergunta_email_brb, resposta_email_brb),
    (pergunta_credor, resposta_credor),
    (pergunta_dr, resposta_dr),
    (pergunta_nex, resposta_nex),
    (pergunta_nob, resposta_nob),
    (pergunta_noe, resposta_noe),
    (pergunta_numero_documento, resposta_numero_documento),
    (pergunta_ped, resposta_ped),
    (pergunta_sistema_fiplan, resposta_sistema_fiplan),
    (pergunta_unidade_getora_executora, resposta_unidade_getora_executora),
    (pergunta_numero_credor, resposta_numero_credor),
    #Xingamentos!
    (pergunta_xingamento_idiota, resposta_xingamento_idiota),
    (pergunta_xingamento_burro, resposta_xingamento_burro),
    (pergunta_xingamento_estupido, resposta_xingamento_estupido),
    (pergunta_xingamento_merda, resposta_xingamento_merda),
    (pergunta_xingamento_palhaco, resposta_xingamento_palhaco),
    (pergunta_xingamento_imbecil, resposta_xingamento_imbecil),
    (pergunta_xingamento_otario, resposta_xingamento_otario),
    (pergunta_xingamento_besta, resposta_xingamento_besta),
    (pergunta_xingamento_corino, resposta_xingamento_corino),
    (pergunta_xingamento_analfabeto, resposta_xingamento_analfabeto),
    (pergunta_xingamento_vagabundo, resposta_xingamento_vagabundo),
    (pergunta_xingamento_ze_ruela, resposta_xingamento_ze_ruela),
    (pergunta_xingamento_feio, resposta_xingamento_feio),
    (pergunta_xingamento_burra, resposta_xingamento_burra),
    (pergunta_xingamento_lixo, resposta_xingamento_lixo),
    (pergunta_xingamento_foca, resposta_xingamento_foca),
    (pergunta_xingamento_cavalo, resposta_xingamento_cavalo),
    (pergunta_xingamento_porco, resposta_xingamento_porco),
    (pergunta_xingamento_trouxa, resposta_xingamento_trouxa),
    (pergunta_xingamento_boco, resposta_xingamento_boco),
    (pergunta_xingamento_chato, resposta_xingamento_chato),
    (pergunta_xingamento_pateta, resposta_xingamento_pateta),
    (pergunta_xingamento_cabeludo, resposta_xingamento_cabeludo),
    (pergunta_xingamento_pato, resposta_xingamento_pato),
    (pergunta_xingamento_vaca, resposta_xingamento_vaca),
    (pergunta_xingamento_cadela, resposta_xingamento_cadela),
    (pergunta_xingamento_bicho, resposta_xingamento_bicho),
    (pergunta_xingamento_aleijado, resposta_xingamento_aleijado),
    (pergunta_xingamento_baleia, resposta_xingamento_baleia),
    (pergunta_xingamento_saco, resposta_xingamento_saco),
    (pergunta_xingamento_piranha, resposta_xingamento_piranha),
    (pergunta_xingamento_esquisito, resposta_xingamento_esquisito),
    (pergunta_xingamento_galinha, resposta_xingamento_galinha),
    (pergunta_xingamento_frouxo, resposta_xingamento_frouxo),
    (pergunta_xingamento_mermao, resposta_xingamento_mermao),
    (pergunta_xingamento_bicho_papao, resposta_xingamento_bicho_papao),
    (pergunta_xingamento_pirralho, resposta_xingamento_pirralho),
    (pergunta_xingamento_cachorrinho, resposta_xingamento_cachorrinho),
    (pergunta_xingamento_lambedor, resposta_xingamento_lambedor),
    (pergunta_xingamento_safado, resposta_xingamento_safado),
    (pergunta_xingamento_vagabunda, resposta_xingamento_vagabunda),
    (pergunta_xingamento_gordo, resposta_xingamento_gordo),
    (pergunta_xingamento_viado, resposta_xingamento_viado),
    (pergunta_xingamento_lerdo, resposta_xingamento_lerdo),
    (pergunta_xingamento_imbecil, resposta_xingamento_imbecil),
    (pergunta_xingamento_panaca, resposta_xingamento_panaca),
    (pergunta_xingamento_gamba, resposta_xingamento_gamba),
    (pergunta_xingamento_ze_buceta, resposta_xingamento_ze_buceta),
    (pergunta_xingamento_liso, resposta_xingamento_liso),
    (pergunta_xingamento_tosco, resposta_xingamento_tosco),
    (pergunta_xingamento_miseravel, resposta_xingamento_miseravel),
    (pergunta_xingamento_patife, resposta_xingamento_patife),
    (pergunta_xingamento_sacana, resposta_xingamento_sacana),
    (pergunta_xingamento_vai_tomar_no_cu,resposta_xingamento_vai_tomar_no_cu),
    (pergunta_xingamento_se_fode,resposta_xingamento_se_fode),
    (pergunta_xingamento_vai_se_ferrar,resposta_xingamento_vai_se_ferrar),
    (pergunta_xingamento_vai_pra_puta_que_pariu,resposta_xingamento_vai_pra_puta_que_pariu),
    (pergunta_xingamento_vai_se_lascar,resposta_xingamento_vai_se_lascar),
    (pergunta_xingamento_vai_pro_inferno,resposta_xingamento_vai_pro_inferno),
    (pergunta_xingamento_caralho,resposta_xingamento_caralho),
    (pergunta_xingamento_puta_que_pariu,resposta_xingamento_puta_que_pariu),
    (pergunta_xingamento_filho_da_puta,resposta_xingamento_filho_da_puta),
    (pergunta_xingamento_saco_de_merda,resposta_xingamento_saco_de_merda),
    (pergunta_xingamento_vai_tomar_no_olho_do_cu,resposta_xingamento_vai_tomar_no_olho_do_cu),
    (pergunta_xingamento_merda_de_pessoa,resposta_xingamento_merda_de_pessoa),
    (pergunta_xingamento_cala_a_boca,resposta_xingamento_cala_a_boca),
    (pergunta_xingamento_vai_se_foder,resposta_xingamento_vai_se_foder),
    (pergunta_xingamento_sua_puta,resposta_xingamento_sua_puta),
    (pergunta_xingamento_vai_tomar_no_cuzinho,resposta_xingamento_vai_tomar_no_cuzinho),
    (pergunta_xingamento_vai_se_lascar_bem_longe,resposta_xingamento_vai_se_lascar_bem_longe),
    (pergunta_xingamento_vai_tomar_no_seu_cu_sujo,resposta_xingamento_vai_tomar_no_seu_cu_sujo),
    (pergunta_xingamento_porra,resposta_xingamento_porra),
    (pergunta_xingamento_vai_tomar_no_seu_cu_gordo,resposta_xingamento_vai_tomar_no_seu_cu_gordo),
    (pergunta_xingamento_vai_se_foder_bem_gostoso,resposta_xingamento_vai_se_foder_bem_gostoso),
    (pergunta_xingamento_seu_imbecil,resposta_xingamento_seu_imbecil),
    (pergunta_xingamento_vai_pra_puta_que_pariu_agora,resposta_xingamento_vai_pra_puta_que_pariu_agora),
    (pergunta_xingamento_vai_se_fuder_mais_um_pouco,resposta_xingamento_vai_se_fuder_mais_um_pouco),
    (pergunta_xingamento_sua_vaca,resposta_xingamento_sua_vaca),
    (pergunta_xingamento_puta_merda,resposta_xingamento_puta_merda),
    (pergunta_xingamento_vai_se_fuder_pra_puta_que_pariu,resposta_xingamento_vai_se_fuder_pra_puta_que_pariu),
    (pergunta_xingamento_vai_se_ferrar_no_seu_cu,resposta_xingamento_vai_se_ferrar_no_seu_cu),
    (pergunta_xingamento_vai_tomar_no_meio_do_cu,resposta_xingamento_vai_tomar_no_meio_do_cu),
    (pergunta_xingamento_seu_filho_da_puta,resposta_xingamento_seu_filho_da_puta),
    (pergunta_xingamento_porra_nenhuma,resposta_xingamento_porra_nenhuma),
    (pergunta_xingamento_cai_na_porra_do_poco,resposta_xingamento_cai_na_porra_do_poco),
    (pergunta_xingamento_vai_se_lascar_bem_fundo,resposta_xingamento_vai_se_lascar_bem_fundo),
    (pergunta_xingamento_vai_se_foder_que_nem_um_animal,resposta_xingamento_vai_se_foder_que_nem_um_animal),
    (pergunta_xingamento_caralho_que_merda,resposta_xingamento_caralho_que_merda),
    (pergunta_xingamento_voce_e_um_lixo,resposta_xingamento_voce_e_um_lixo)

]

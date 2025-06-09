print("Políticas de privacidade:\nO banco monedas coleta seus dados de maneira segura e eficaz, com a finalidade de melhorar a experiência dos seus clientes, seguindo as recomendações e restrições da LGPD (Lei geral de proteção de dados).\nVocê concorda com as políticas acima?")
resposta = input("Sua resposta:")
if resposta == "sim":
    print("Meus parabéns, o Monedas te agradeçe.")
elif resposta == "não":
    print("Concorde com a política de privacidade para prosseguir.")
else: 
    print("Digite uma resposta válida: 'sim' ou 'não'.")
    resposta = input("Sua resposta:")
    if resposta == "sim":
        print("Meus parabéns, o Monedas te agradeçe.")
    elif resposta == "não":
        print("Concorde com a política de privacidade para prosseguir.")

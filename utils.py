def exibir_cabecalho(*textos, caractere='-'):
    largura = 50
    print(caractere * largura)
    for texto in textos:
        print(texto.center(largura))
    print(caractere * largura)
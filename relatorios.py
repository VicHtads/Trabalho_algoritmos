# Arquivo: relatorios.py
# Este arquivo deverá receber todas e quaisquer fuções e métodos relacionados aos relatórios direcionados ao adiministrador do sistema.
from utils import exibir_cabecalho

def relatorio_temas_populares(lista_e):
    """
    Calcula e exibe os temas de eventos mais populares com base no número
    total de incrições em cada tema.
    """
    exibir_cabecalho("Relatório: Temas Mais Populares")

    if not lista_e:
        print("Não há eventos para gerar estatísticas.")
        return
    # Dicionário para contar as inscrições por tema
    contagem_temas = {}
    for evento in lista_e:
        tema = evento.get('tema')
        if tema:# Garante que só processamos eventos que têm um tema
            num_inscritos = len(evento['inscritos'])
            # .get(tema, 0) pega o valor atual ou 0 se o tema for novo
            contagem_temas[tema] = contagem_temas.get(tema, 0) + num_inscritos
    
    if not contagem_temas:
        print("Nenhum tema com incrições para analisar.")
        return
    
    # Ordenando o dicionário pelo número de inscrições (o valor), em ordem decrescente
    temas_ordenados = sorted(contagem_temas.items(), key=lambda item: item[1], reverse=True)

    print(f"{'Tema':<25} | {'Total de Inscrições'}")
    print("-" * 50)
    for tema, total in temas_ordenados:
        print(f"{tema:<25} | {total}")
    print("-" * 50)
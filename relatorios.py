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


def relatorio_participantes_ativos(lista_e, lista_p):
    """
    Calcula e exibe um ranking dos participantes mais ativos com base 
    no número de eventos em que estão inscritos
    """
    exibir_cabecalho("Relatório: Participantes Mais Ativos")

    if not lista_e or not lista_p:
        print("Dados insuficientes para gerar o relatório.")
        return
    
    # Conta a frequência de cada ID de participante nos eventos
    contagem_ids = {}
    for evento in lista_e:
        for participante_id in evento['inscritos']:
            contagem_ids[participante_id] = contagem_ids.get(participante_id, 0) + 1
    
    if not contagem_ids:
        print("Nenhum participante inscrito em eventos.")
        return
    
    # Cria um dicionário de busca para acesso rápido aos nomes
    participantes_por_id = {p['id']: p for p in lista_p}

    # Monta a lista final com nome e contagem
    resultado_final = []
    for pid, contagem in contagem_ids.items():
        # Acessa o nome instantaneamente usando o dicionário de busca
        nome_participante = participantes_por_id.get(pid, {}).get('nome', f'ID Desconhecido{pid}')
        resultado_final.append({'nome': nome_participante, 'eventos': contagem})

    # Ordena o resultado final pela contagem de eventos
    ranking = sorted(resultado_final, key=lambda item: item['eventos'], reverse=True)

    # Exibe o ranking
    print(f"{'Posição':<10} | {'Nome do Participante':<25} | {'Eventos Inscritos'}")
    print("-" * 65)

    for i, item in enumerate(ranking):
        posicao = f"{i + 1}º"
        print(f"{posicao:<10} | {item['nome']:<25} | {item['eventos']}")
    print("-" * 65)


def relatorio_baixa_adesao(lista_e):
    """
    Identifica e lista eventos com um número de particoantes abaixo de um limite mínimo,
    sugerindo-os para revisão ou cancelamento.
    """
    exibir_cabecalho("Relatório: Eventos com Baixa Adesão")

    # Define o limite aqui para ser fácil de alterar no futuro
    limite_minimo = 2

    # Filtra os eventos que atendem à condição
    eventos_criticos = [e for e in lista_e if len(e.get('inscritos', [])) < limite_minimo]

    if not eventos_criticos:
        print("\n[SUCESSO] Nenhum evento com baixa adesão encontrado.")
        return
    
    print(f"\n[AVISO] Os seguintes eventos têm menos de {limite_minimo} participantes e podem ser candidatos a cancelamento\n")

    # Exibe os eventos encontrados
    for evento in eventos_criticos:
        nome = evento.get('nome', 'Evento sem nome')
        num_inscritos = len(evento.get('inscritos', []))
        print(f"- {nome} (Inscritos: {num_inscritos})")

    print("\n" + "-" * 60)
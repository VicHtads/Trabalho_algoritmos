# Arquivo: eventos.py
# Este arquivo será o contâiner para todas as funcionalidades envolvendo 'eventos'
from utils import exibir_cabecalho

def listar_todos_eventos(lista_e):# Exibe no terminal a lista de todos eventos cadastrados.

    exibir_cabecalho("Lista de Eventos Cadastrados")

    if not lista_e:
        print("Nenhum evento cadastrado no sistema")
        return
    for e in lista_e:# Acesso dos valores do dicionário evento por suas chaves
        nome = e["nome"]
        data = e["data"]
        tema = e["tema"]
        num_inscritos = len(e["inscritos"])

        print(f"- {nome} ({tema})")
        print(f" Data: {data} | Inscritos: {num_inscritos}")
        print("-" * 20)


def listar_participante_evento_especifico(eventos, participantes):
    '''
    Lista os participantes de um evento específico escollhido pelo usuário.
    '''
    exibir_cabecalho("Listar Participantes por Eventos Cadastrados")

    if not eventos:
        print("Nenhum evento cadastrado para consultar")
        return
    
    # Lista todos os eventos para o usuário escolher
    for i, evento in enumerate(eventos):
        print(f"{i + 1}. {evento['nome']}")
    
    try:
        escolha = int(input("\nDigite o número do evento que deseja consultar: "))
        # Converte a escolha para um índice de lista (ex: 1 -> 0, 2 -> 1)
        indice_evento = escolha - 1

        # Converte a escolha para um índice de lista (ex: 1 -> 0, 2 -> 1)
        if 0 <= indice_evento < len(eventos):
            evento_escolhido = eventos[indice_evento]
        else:
            print("[ERRO] Número de eventos inválido.")
            return
        
    except ValueError:
        print("[ERRO] Entrada inválida. Por favor digite um número.")
        return
    # Encontrar os IDs dos inscritos no evento escolhido
    print(f"\n--- Participantes Inscritos em: {evento_escolhido['nome']} ---")
    ids_dos_inscritos = evento_escolhido['inscritos']

    if not ids_dos_inscritos:
        print("Este evento não possui participantes inscritos.")
        return
    
    # Buscar os detalhes dos participantes correspondentes
    participantes_encontrados = [p for p in participantes if p['id'] in ids_dos_inscritos]
    
    # Exibir os detalhes
    print(f"{'ID':<5} | {'Nome':<25} | {'E-mail'}")
    print("-" * 50)
    for p in participantes_encontrados:
        print(f"{p['id']:<5} | {p['nome']:<25} | {p['email']}")
    print("-" * 50)
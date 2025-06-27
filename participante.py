# Arquivo: participante.py 
# Este arquivo receberá todas e quaisquer funcionalidades com relação ao indivíduo 'participante'.
from utils import exibir_cabecalho
import eventos as evt

def cadastro_participante(lista_p, lista_e):
    '''
    Solicita os dados de um novo participante, com suas preferências temáticas, sugere eventos e libera uma inscrição imediata caso o participante queira.
    '''
    exibir_cabecalho("Cadastrar Novo Participante")

# --- Bloco: Coleta de Dados Básicos ---
    while True:
    #  Solicita dados ao usuário
    # Uso do .strip() para remover espaços extras que o usuário possa digitar
        nome = input("Digite o nome completo do participante: ").strip()
        if len(nome) > 2: # Uma validação simples: o nome deve conter maus de 2 caracteres.
            break
        else:
            print("[ERRO] Nome inválido. por favor, digite um nome com mais de 2 caracteres")

    while True:
        email = input(f"Digite o e-mail de {nome}: ").strip()
        # Validação de formato: Checa se tem o '@' e se tem '.' depois do '@'
        if "@" in email and "." in email.split("@")[1]:
            break
        else:
            print("[ERRO] Formato de e-mail inválido. O e-mail deve conter '@' e um '.' após.")

# --- Bloco: Coletar Preferências Temáticas ---
    print("\nSelecione seus temas de interesse:")
    temas_disponiveis = evt.obter_temas_unicos(lista_e)
    for i, tema in enumerate(temas_disponiveis):
        print(f"{i + 1}. {tema}")

    preferencias_escolhidas = []
    try:
        escolhas = input("Digite os números dos temas (separados por vírgulas, ex: 1,3): ").split(',')
        for escolha in escolhas:
            indice = int(escolha.strip()) - 1
            if 0 <= indice < len(temas_disponiveis):
                preferencias_escolhidas.append(temas_disponiveis[indice])
    except (ValueError, IndexError):
        print("[AVISO] Seleção de temas inválidas. O participante será cadastrado sem preferências.")

# --- Bloco: Criar e Salvar Participante ---
    novo_id = gerar_novo_id_participante(lista_p)
    novo_participante = {
        'id': novo_id,
        'nome': nome,
        'email': email,
        'preferencias_tematicas': preferencias_escolhidas
    }
    lista_p.append(novo_participante)
    print(f"\n[SUCESSO] Participante '{nome}' (ID: {novo_id}) cadastrado!")

# --- Bloco: Sugerir e Inscrever em Evento ---
    if not preferencias_escolhidas:
        return # Se não foram especificadas preferências temáticas, encerra a função aqui.
    
    eventos_sugeridos = [e for e in lista_e if e['tema'] in preferencias_escolhidas]

    if not eventos_sugeridos:
        print("Nenhum evento encontrado com base em suas preferências")
        return
    
    exibir_cabecalho("Eventos Sugeridos para Você")
    for i, evento in enumerate(eventos_sugeridos):
        print(f"{i + 1}. {evento['nome']} ({evento['tema']}) - Data {evento['data']}")
    
    try:
        inscricao = input("\nDeseja se increver em um dos eventos sugeridos? Digite o número do evento ou 'N' para não: "). strip()
        if inscricao.upper() == 'N':
            print("Entendido! Pulando incrição em evento.")
            return
        
        indice_evento = int(inscricao) - 1
        if 0 <= indice_evento < len(eventos_sugeridos):
            evento_para_inscrever = eventos_sugeridos[indice_evento]
            # Adiciona o ID do participante na lista de inscritos do evento
            evento_para_inscrever['inscritos'].append(novo_id)
            print(f"[SUCESO] Inscrição realizada no evento: {evento_para_inscrever['nome']}!")
        else:
            print("[AVISO] Escolha de evento inválida. Inscrição não realizada.")
    except ValueError:
        print("[AVISO] Entrada inválida. inscrição não realizada.")


# - Geração de ID's únicos de 1 à ... 
def gerar_novo_id_participante(lista_p):
    '''
    Gera um ID único para um participante.
    A lógica é encontrar o maior ID existente e incrementar + 1
    '''
    if not lista_p:
        # Se a lista está vazia, o primeiro ID será 1.
        return 1
    else:
        return max(p['id'] for p in lista_p) + 1


def listar_todos_participantes(lista_p):
    '''
    Exibe no terminal a lista de todos os participantes cadastrados.
    '''
    exibir_cabecalho("Lista de Participantes Cadastrados")

    if not lista_p:
        print("Nenhum participante Cadastrado no sistema.")
        return
    
    print(f"{'ID':<5} | {'Nome':<25} | {'E-mail'}")
    print("-" * 50)

    for p in lista_p:
        # Acesso dos valores do dicionário 'p' por suas chaves
        uid = p['id']
        nome = p['nome']
        email = p['email']

        # Uso da formatação em f-string para alinhar os dados em colunas
        # :<5 significa "Alinhar à esquerda com 5 caracteres de espaço"***** Lembrar *****
        print(f"{uid:<5} | {nome:<25} | {email}")
    print("-" * 50)

def buscar_participante_por_id(lista_p):
    '''
    Solicita o ID de um participante e exibe seus detalhes caso seja encontrado. Solicitar -> Validar -> Buscar -> Exibir
    '''
    exibir_cabecalho("Buscar Participante por ID")

    try:
        id_buscado = int(input("Digite o ID do participante a ser buscado: "))
    except ValueError:
        print("\n[ERRO] ID inválido. Por favor, digite apenas números.")
        return

    for p in lista_p:
        if p['id'] == id_buscado:
            print("\n[SUCESSO] Participante encontrado.")
            print("-" * 30)
            print(f"ID: {p['id']}")
            print(f"Nome: {p['nome']}")
            print(f"E-mail: {p['email']}")
            print(f"Preferências: {', '.join(p['preferencias_tematicas']) if p['preferencias_tematicas'] else 'Nenhuma'}")
            print("-" * 30)
            return # Caso o participante seja encontrado e seus dados exibidos, encerra a função
    print(f"\n[AVISO] Nenhum participante encontrado com o ID {id_buscado}.")

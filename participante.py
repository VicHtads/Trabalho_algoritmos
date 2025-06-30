# Arquivo: participante.py 
# Este arquivo receberá todas e quaisquer funcionalidades com relação ao indivíduo 'participante'.
from utils import exibir_cabecalho
import eventos as evt

def cadastro_participante(lista_p, lista_e):
    '''
    Solicita os dados de um novo participante, com suas preferências temáticas, sugere eventos e libera uma inscrição imediata caso o participante queira.
    '''
    exibir_cabecalho("Cadastrar Novo Participante")

# Coleta de dados básicos
    while True:
    #  Solicita dados ao usuário
    # Uso do .strip() para remover espaços extras que o usuário possa digitar
        nome = input("Digite o nome completo do participante: ").strip()
        if len(nome) > 2: # Validação simples - o nome deve conter mais de 2 caracteres.
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

# Coleta preferências temáticas
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

# Criar e Salvar Participante
    novo_id = gerar_novo_id_participante(lista_p)
    novo_participante = {
        'id': novo_id,
        'nome': nome,
        'email': email,
        'preferencias_tematicas': preferencias_escolhidas
    }
    lista_p.append(novo_participante)
    print(f"\n[SUCESSO] Participante '{nome}' (ID: {novo_id}) cadastrado!")

# Sugere e Inscreve em Evento 
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


# Geração de ID's únicos de 1 à ... 
def gerar_novo_id_participante(lista_p):
    '''
    Gera um ID único para um participante.
    A lógica é encontrar o maior ID existente e incrementar + 1
    '''
    if not lista_p:
        # Se a lista estiver vazia, o primeiro ID será 1.
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
        # :<5 significa "Alinhar à esquerda com 5 caracteres de espaço"***** Lembrar de reutilizar *****
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


def remover_participante(lista_p, lista_e):
    """
    Remove um participante da lista principal e também de todas as listas de inscrição de eventos.
    """
    exibir_cabecalho("Remover Participante")

    if not lista_p:
        print("Nenhum participante para remover.")
        return

    for i, p in enumerate(lista_p): # Lista todos os participantes encontrados na lista_p(lista_participantes)
        print(f"{i + 1}. {p['nome']} (ID: {p['id']})")

    try:
        escolha = int(input("\nDigite o número do particpante que deseja remover: "))
        indice = escolha - 1

        if not (0 <= indice < len(lista_p)):
            print("[ERRO] Número de participante inválido.")
            return

        particpante_a_remover = lista_p[indice]

    except ValueError:
        print("[ERRO] Entrada inválida. Por favor, digite um número.")

    # Confirmação de segurança
    # .upper() converte a resposta para maiúscula, aceitando 's' ou 'S'
    confirmacao = input(f"Tem certeza que deseja remover '{particpante_a_remover['nome']}'? Esta ação não poderá ser desfeita. [S/N]: ").strip().upper()

    if confirmacao != 'S':
        print("Operação cancelada.")
        return

    # Executa a remoção
    id_a_remover = particpante_a_remover['id']

    # Remove o ID das listas de inscritos dos eventos
    for evento in lista_e:
        if id_a_remover in evento['inscritos']:
            evento['inscritos'].remove(id_a_remover)
    
    # Remove o participante da lista principal
    lista_p.remove(particpante_a_remover)
    print(f"\n[SUCESSO] Participante '{particpante_a_remover['nome']}' removido do sistema.")


def atualizar_participante(lista_p):
    """
    Permite atualização dos dados de um participante escolhido pelo usuário.
    """
    exibir_cabecalho("Atualizar Dadods de Participante")

    if not lista_p:
        print("Nenhum participante para atualizar.")
        return
    
    # Lista e seleciona o participante
    for i, p in enumerate(lista_p):
        print(f"{i + 1}. {p['nome']}")
    
    try:
        escolha = int(input("\nDigite o número do particpante que deseja atualizar: "))
        indice = escolha - 1

        if not (0 <= indice < len(lista_p)):
            print("[ERRO] Número de participante inválido.")
            return

        particpante_a_atualizar = lista_p[indice]

    except ValueError:
        print("[ERRO] Entrada inválida. Por favor, digite um número.")

    while True:
        exibir_cabecalho(f"Editando: {particpante_a_atualizar['nome']}")
        print(f"1. Nome: {particpante_a_atualizar['nome']}")
        print(f"2. email: {particpante_a_atualizar['email']}")
        print(f"0. Voltar ao menu principal")

        campo_escolhido = input("\nQual campo deseja atualizar? ").strip()

        if campo_escolhido == '1':
            # Lógica para alterar o nome
            while True:
                novo_nome = input("Digite o novo nome: ").strip()
                if len(novo_nome) > 2: # Validação que verifica se o nome em digitado tem ou não mais que 2 caractéres
                    particpante_a_atualizar['nome'] = novo_nome
                    print("[SUCESSO] Nome atualizado.")
                    break
                else:
                    print("[ERRO] Nome inválido.")

        elif campo_escolhido == '2':
            # Lógica para alterar o e-mail
            while True:
                novo_email = input("Digite o novo e-mail: ").strip()
                if "@" in novo_email and "." in novo_email.split('@')[1]:# Mesma lógica usada no cadastro de participante
                    particpante_a_atualizar['email'] = novo_email
                    print("[SUCESSO] E-mail atualizado.")
                    break
                else:
                    print("[ERRO] Formato de e-mail inválido.")

        elif campo_escolhido == '0':
            print("Retornando ao menu principal...")
            break

        else:
            print("[ERRO] Opção de campo inválida.")
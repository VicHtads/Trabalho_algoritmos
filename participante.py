from dados import lista_participantes

def cadastro_participante():
    '''
    Solicita os dados de um novo participante, com validação interativa, e o adiciona à lista.
    '''
    print("\n--- Cadastrar Novo Participante ---")

    while True:
    # 1. Solicita dados ao usuário
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

# --- Geração do ID e Criação do Dicionário ---
    novo_id = gerar_novo_id_participante()

    novo_participante = {
        "id": novo_id,
        "nome": nome,
        "email": email,
        "preferencias_tematicas": []
    }

    lista_participantes.append(novo_participante)

    print(f"\n[SUCESSO] Participante '{nome}' adicionado com o ID {novo_id}!")


# - Geração de ID's únicos para 
def gerar_novo_id_participante():
    '''
    Gera um ID único para um participante.
    A lógica é encontrar o maior ID existente e incrementar + 1
    '''
    if not lista_participantes:
        # Se a lista está vazia, o primeiro ID será 1.
        return 1
    else:
        # 1. Cria uma lista vazia para guardar os IDs
        ids_existentes = []

        # 2. Usa um for loop para percorrer cada dicionário de participante
        for participantes in lista_participantes:

            # 3. De cada participante, pega o valor da chave 'id' e adiciona à lista
            ids_existentes.append(participantes["id"])

        # 4. Usa a função max() para encontrar o maior número nessa lista
        maior_id = max(ids_existentes)

        # 5. O novo ID será o maior ID + 1
        novo_id = maior_id + 1
        return novo_id


def listar_todos_participantes():
    """
    Exibe no terminal a lista de todos os participantes cadastrados.
    """
    # --- DEBUG CHECKPOINT 3 ---
    print(f"--- DEBUG: No início de listar_participantes, a lista tem {len(lista_participantes)} itens.")
    print("\n--- Lista de Participantes Cadastrados ---")

    if not lista_participantes:
        print("Nenhum participante Cadastrado no sistema.")
        return
    
    print(f"{'ID':<5} | {'Nome':<25} | {'E-mail'}")
    print("-" * 50)

    for p in lista_participantes:
        # Acesso dos valores do dicionário 'p' por suas chaves
        uid = p['id']
        nome = p['nome']
        email = p['email']

        # Uso da formatação em f-string para alinhar os dados em colunas
        # :<5 significa "Alinhar à esquerda com 5 caracteres de espaço"
        print(f"{uid:<5} | {nome:<25} | {email}")
    print("-" * 50)

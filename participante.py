# Arquivo: participante.py 
# Este arquivo receberá todas e quaisquer funcionalidades com relação ao indivíduo 'participante'.

def cadastro_participante(lista_p):
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
    novo_id = gerar_novo_id_participante(lista_p)

    novo_participante = {
        "id": novo_id,
        "nome": nome,
        "email": email,
        "preferencias_tematicas": []
    }

    lista_p.append(novo_participante)
    print(f"\n[SUCESSO] Participante '{nome}' adicionado com o ID {novo_id}!")


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
        ids_existentes = [p['id'] for p in lista_p]
        return max(ids_existentes) + 1


def listar_todos_participantes(lista_p):
    """
    Exibe no terminal a lista de todos os participantes cadastrados.
    """
    print("\n--- Lista de Participantes Cadastrados ---")
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
        # :<5 significa "Alinhar à esquerda com 5 caracteres de espaço"
        print(f"{uid:<5} | {nome:<25} | {email}")
    print("-" * 50)

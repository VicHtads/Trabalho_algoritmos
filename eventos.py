# Arquivo: eventos.py
# Este arquivo será o contâiner para todas as funcionalidades envolvendo 'eventos'.
import datetime
from utils import exibir_cabecalho

def listar_todos_eventos(lista_e):
    """
    Exibe no terminal a lista de todos eventos cadastrados.
    """
    exibir_cabecalho("Lista de Eventos Cadastrados")

    if not lista_e:
        print("Nenhum evento cadastrado no sistema")
        return
    for e in lista_e: # Acesso dos valores do dicionário evento por suas chaves
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
    # Encontra os IDs dos inscritos no evento escolhido
    print(f"\n--- Participantes Inscritos em: {evento_escolhido['nome']} ---")
    ids_dos_inscritos = evento_escolhido['inscritos']

    if not ids_dos_inscritos:
        print("Este evento não possui participantes inscritos.")
        return
    
    # Busca os detalhes dos participantes correspondentes
    participantes_encontrados = [p for p in participantes if p['id'] in ids_dos_inscritos]
    
    # Exibe os detalhes
    print(f"{'ID':<5} | {'Nome':<25} | {'E-mail'}")
    print("-" * 50)
    for p in participantes_encontrados:
        print(f"{p['id']:<5} | {p['nome']:<25} | {p['email']}")
    print("-" * 50)

def obter_temas_unicos(eventos):
    '''
    A lógica é procurar na lista de eventos e retornar uma lista de temas únicos
    '''
    if not eventos:
        return []

    temas_brutos = {e.get('tema') for e in eventos}
    temas_unicos = {tema for tema in temas_brutos if tema is not None}

    temas = sorted(list(temas_unicos))
    return temas


def adicionar_novo_evento(lista_e, lista_p_speakers):
    """
    Cadastra um novo evento com validação de nome único, formato de data, e
    permite a associação de palestrantes existentes.
    """
    exibir_cabecalho("Adicionar Novo Evento")

    # Coleta nome e validar unicidade
    while True:
        nome = input("Digite o nome do evento: ").strip()
        # Checa se o nome já existe
        if any(evento['nome'].lower() == nome.lower() for evento in lista_e):
            print("[ERRO] Já existe um evento com esse nome. Tente outro.")
        elif len(nome) < 3:
            print("[ERRO] O nome do evento deve ter pelo ao menos 3 caracteres.")
        else:
            break

    while True:
        data_str = input("Digite a data do evento (formato AAAA-MM-DD):").strip()
        try:
            # Tenta converter a str para um objeto de data(estrutura de dados que representa uma data específica). Se der certo, o formato é válido.
            datetime.datetime.strptime(data_str, '%Y-%m-%d')
            break
        except ValueError:
            print("[ERRO] Formato de data inválido. Use AAAA-MM-DD.")

    # Coletar tema
    tema = input("Digite o tema central do evento: ").strip()

    # Seleciona palestrantes
    ids_palestrantes_selecionados = []

    if not lista_p_speakers:
        print("[AVISO] Nenhum palestrante cadastrado para associar a este evento.")
    else:
        print("\nSelecione os palestrantes para este evento: ")
        for i, palestrante in enumerate(lista_p_speakers):
            print(f"{i + 1}. {palestrante['nome']}")
        
        try:
            escolhas = input("Digite os números dos palestrantes (separados por vírgula ou deixe em branco para nenhum): ").split(',')
            for escolha in escolhas:
                if escolha.strip(): # Garante que não processamos escolhas vazias
                    indice = int(escolha.strip()) - 1
                    if 0 <= indice < len(lista_p_speakers):
                        ids_palestrantes_selecionados.append(lista_p_speakers[indice]['id'])
        except (ValueError, IndexError):
            print("[AVISO] Seleção de palestrantes inválida. O evento será criado sem palestrantes.")

    # Cria o dicionário do novo evento e adicionar à lista
    novo_evento = {
        "nome": nome,
        "data": data_str,
        "tema": tema,
        "inscritos": [], # Um novo evento começa sem inscritos
        "palestrantes": ids_palestrantes_selecionados
    }

    lista_e.append(novo_evento)
    print(f"\n[SUCESSO] Evento '{nome}' cadastrado.")


def remover_evento(lista_e):
    """
    Remove um evento selecionado do sistema após a confirmação do usuário.
    """
    exibir_cabecalho("Remover Evento")

    if not lista_e:
        print("Nenhum evento para remover.")
        return
    
    # Lista eventos para seleção
    for i, evento in enumerate(lista_e):
        print(f"{i + 1}. {evento['nome']}")

    try:
        escolha = int(input("\nDigite o número do evento que deseja remover: "))
        indice =escolha - 1

        if not (0 <= indice < len(lista_e)):
            print("[ERRO] Número de evento inválido.")
            return
        
        evento_a_remover = lista_e[indice]

    except ValueError:
        print("[ERRO] Entrada inválida. Por favor, digite um número.")
        return

    # Confirmação de segurança
    confirmacao = input(f"Tem certeza que deseja remover o evento '{evento_a_remover['nome']}'? [S/N]: ").strip().upper()

    if confirmacao != 'S':
        print("Operação cancelada.")
        return

    # Remove o evento da lista principal
    lista_e.remove(evento_a_remover)

    print(f"\n[SUCESSO] Evento '{evento_a_remover['nome']}' removido do sistema.")


def atualizar_evento(lista_e, lista_p_speakers):
    """
    Permite a atualização dos dados de um evento existente.
    """
    exibir_cabecalho("Atualizar Evento")

    if not lista_e:
        print("Nenhum evento para atualizar.")
        return

    # Selecionar o evento a ser atualizado
    for i, evento in enumerate(lista_e):
        print(f"{i + 1}. {evento['nome']}")
    try:
        escolha = int(input("\nDigite o número do evento que deseja atualizar: "))
        indice = escolha - 1
        if not (0 <= indice < len(lista_e)):
            print("[ERRO] Número de evento inválido.")
            return
        evento_a_atualizar = lista_e[indice]
    except ValueError:
        print("[ERRO] Entrada inválida.")
        return

    # Loop de edição com sub-menu
    while True:
        exibir_cabecalho(f"Editando Evento: {evento_a_atualizar['nome']}")
        print(f"1. Nome: {evento_a_atualizar['nome']}")
        print(f"2. Data: {evento_a_atualizar['data']}")
        print(f"3. Tema: {evento_a_atualizar['tema']}")
        print(f"4. Palestrantes (Atualmente: {len(evento_a_atualizar['palestrantes'])})")
        print("0. Concluir Edição")

        campo_escolhido = input("\nQual campo deseja alterar? ").strip()

        if campo_escolhido == '1':
            novo_nome = input("Digite o novo nome: ").strip()
            if any(e['nome'].lower() == novo_nome.lower() and e is not evento_a_atualizar for e in lista_e):
                print("[ERRO] Outro evento já possui este nome.")
            elif len(novo_nome) > 2:
                evento_a_atualizar['nome'] = novo_nome
                print("[SUCESSO] Nome atualizado!")
            else:
                print("[ERRO] Nome inválido.")
        
        elif campo_escolhido == '2':
            nova_data = input("Digite a nova data (AAAA-MM-DD): ").strip()
            try:
                datetime.datetime.strptime(nova_data, '%Y-%m-%d')
                evento_a_atualizar['data'] = nova_data
                print("[SUCESSO] Data atualizada!")
            except ValueError:
                print("[ERRO] Formato de data inválido.")

        elif campo_escolhido == '3':
            evento_a_atualizar['tema'] = input("Digite o novo tema: ").strip()
            print("[SUCESSO] Tema atualizado!")

        elif campo_escolhido == '4':
            # Lógica para re-selecionar palestrantes
            ids_palestrantes_selecionados = []
            if lista_p_speakers:
                print("\nSelecione os novos palestrantes:")
                for i, p in enumerate(lista_p_speakers):
                    print(f"{i + 1}. {p['nome']}")

                try:
                    escolhas = input("Digite os números (separados por vírgula): ").split(',')
                    for esc in escolhas:
                        if esc.strip():
                            idx = int(esc.strip()) - 1
                            if 0 <= idx < len(lista_p_speakers):
                                ids_palestrantes_selecionados.append(lista_p_speakers[idx]['id'])
                    evento_a_atualizar['palestrantes'] = ids_palestrantes_selecionados
                    print("[SUCESSO] Lista de palestrantes atualizada!")
                except (ValueError, IndexError):
                    print("[AVISO] Seleção inválida. Palestrantes não foram alterados.")

            else:
                print("Nenhum palestrante cadastrado para selecionar.")

        elif campo_escolhido == '0':
            print(f"Atualizações do evento '{evento_a_atualizar['nome']}' concluídas.")
            break
        else:
            print("[ERRO] Opção de campo inválida.")


def buscar_eventos_por_tema(lista_e):
    """
    Permite ao usuáriio escolher um tema e lista todos eventos correspondentes
    àquele tema.
    """
    exibir_cabecalho("Buscar Eventos por Tema")

    # Reutiliza função para obter e listar os temas
    temas_disponiveis =obter_temas_unicos(lista_e)
    if not temas_disponiveis:
        print("Não há temas disponíveis para busca.")
        return
    
    print("Selecione um tema para ver os eventos associados:")
    for i, tema in enumerate(temas_disponiveis):
        print(f"{i + 1}. {tema}")

    # Obtém e valida a escolha do usuário
    try:
        escolha = int(input("\nDigite o número do tema: "))
        indice = escolha - 1
        if not (0 <= indice < len(temas_disponiveis)):
            print("[ERRO] Número de tema inválido.")
            return
        tema_escolhido = temas_disponiveis[indice]
    except ValueError:
        print("[ERRO] Entrada inválida. Por favor digite um número.")
        return
    
    # Filtra os eventos
    eventos_encontrados = [e for e in lista_e if e.get('tema') == tema_escolhido]

    # Exibi os resultados
    exibir_cabecalho(f"Eventos sobre o Tema: {tema_escolhido}")

    if not eventos_encontrados:
        print("Nenhum evento encontrado para este tema.")
    else:
        # Reutilizando a mesma formatação da função de listar todos
        for evento in eventos_encontrados:
            nome = evento['nome']
            data = evento['data']
            num_inscritos = len(evento['inscritos'])
            
            print(f"- {nome}")
            print(f"  Data: {data} | Inscritos: {num_inscritos}")
            print("-" * 20)
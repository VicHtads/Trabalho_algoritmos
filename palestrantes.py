# Arquivo: palestrante.py
# Este arquivo receberá todas e quaisquer funcionalidades e métodos relacionados a entidade 'palestrante'.
from utils import exibir_cabecalho

def gerar_id_palestrante(lista_palestrante):
    """
    Gera um ID customizado para um plaestrante no formato PXXX (ex: P001, P002).
    """
    maior_numero = 0 # Encontra o maior número usado nos IDs de palestrante
    for palestrante in lista_palestrante:
        id_existente = str(palestrante.get('id', ''))

        try:
            # Pega a parte numérica depois do 'P'
            numero = int(id_existente[1:])
            if numero > maior_numero:
                maior_numero = numero
        except (ValueError, IndexError):
            continue # Ignora qualquer ID que não seja no formato PXXX
    
    novo_numero = maior_numero + 1
    # Formata o novo ID com zeros à esquerda para ter 3 dígitos com a f-string com :03d.
    novo_id = f"P{novo_numero:03d}" 
    return novo_id

def adicionar_novo_palestrante(lista_palestrantes):
    """
    Solicita os dados de um novo palestrante e o adiciona a lista.
    """
    exibir_cabecalho("Adicionar Novo Palestrante")

    # Coleta de dados
    nome = input("Digite o nome completo do palestrante: ").strip()
    bio= input(f"Digite a bio de {nome}: ").strip()
    area = input(f"Digite a área de expertise de {nome}: ").strip()

    if not nome or not bio or not area:
        print("\n[ERRO] Todos os ccampos (nome, bio, área) são obrigatórios. O cancelada.")
        return

    # Gerar o novo ID customizado
    novo_id = gerar_id_palestrante(lista_palestrantes)

    novo_palestrante = {
        'id': novo_id,
        'nome': nome,
        'bio': bio,
        'area_expertise': area
    }

    lista_palestrantes.append(novo_palestrante)
    print(f"\n[SUCESSO] Palestrante '{nome}' cadastrado com sucesso co ID: {novo_id}!")


def listar_todos_palestrantes(lista_p):
    """
    Exibe no terminal uma lista formatada de todos os palestrantes cadastrados.
    """
    exibir_cabecalho("Lista de Palestrantes Cadastrados")

    if not lista_p:
        print("Nenhum palestrante cadastrado no sistema.")
        return
    
    print(f"{'ID':<10} | {'Nome':<25} | {'Área de Expertise'}")
    print("-" * 60)

    # Iteração sobre a lista para exibir os dados achados de cada palestrante
    for palestrante in lista_p:
        pid = palestrante.get('id', 'N/A')
        nome = palestrante.get('nome', 'N/A')
        area = palestrante.get('area_expertise', 'N/A')

        print(f"{str(pid):<10} | {nome:<25} | {area}")
    print("-" * 60)


def ver_detalhes_palestrante(lista_p, lista_e):
    """
    Exibe os detalhes completos de um palestrante específico, incluindo os eventos
    em que ele está escalado para palestrar.
    """

    exibir_cabecalho("Ver Detalhes de um Palestrante")

    if not lista_p:
        print("Nenhum palestrante cadastrado.")
        return
    
    # Lista palestrantes para seleção
    for i, palestrante in enumerate(lista_p):
        print(f"{i + 1}. {palestrante['nome']}")

    try:
        escolha = int(input("\nDigite o número do palestrante que desja ver: "))
        indice = escolha - 1

        if not (0 <= indice < len(lista_p)):
            print("[ERRO] Número de palestrante inválido.")
            return
        palestrante_escolhido = lista_p[indice]
    
    except ValueError:
        print("[ERRO] Entrada inválida. Por favor, digite um número.")
        return
    
    # Exibe os detalhes básicos do palestrante
    exibir_cabecalho(f"Detalhes de: {palestrante_escolhido['nome']}")
    print(f"ID: {palestrante_escolhido['id']}")
    print(f"Bio: {palestrante_escolhido['bio']}")
    print(f"Área de Expertise: {palestrante_escolhido['area_expertise']}")

    # Encontra e lista os eventos associados
    print("\nEventos Associados:")
    id_palestrante = palestrante_escolhido['id']
    eventos_encontrados = [evento for evento in lista_e if id_palestrante in evento['palestrantes']]

    if not eventos_encontrados:
        print("Nenhum evento associado a este palestrante.")
    else:
        for evento in eventos_encontrados:
            print(f"  - {evento['nome']} (Tema: {evento['tema']}) - Data: {evento['data']}")

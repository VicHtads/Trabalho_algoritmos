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
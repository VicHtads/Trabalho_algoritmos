# Arquivo: palestrante.py
# Este arquivo receberá todas e quaisquer funcionalidades e métodos relacionados a entidade 'palestrante'.

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
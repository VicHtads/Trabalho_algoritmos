# Arquivo: eventos.py
# Este arquivo será o contâiner para todas as funcionalidades envolvendo 'eventos'

def listar_todos_eventos(lista_e):# Exibe no terminal a lista de todos eventos cadastrados.
    print("\n--- Lista de Eventos Cadastrados ---")

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
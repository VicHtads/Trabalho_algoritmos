from dados import lista_eventos

def listar_todos_eventos():# Exibe no terminal a lista de todos eventos cadastrados.
    print("\n--- Lista de Eventos Cadastrados ---")

    if not lista_eventos:
        print("Nenhum evento cadastrado no sistema")
        return
    for evento in lista_eventos:# Acesso dos valores do dicionário evento por suas chaves
        nome = evento["nome"]
        data = evento["data"]
        tema = evento["tema"]
        num_inscritos = len(evento["inscritos"])

        print(f"- {nome} ({tema})")
        print(f" Data: {data} | Inscritos: {num_inscritos}")
        print("-" * 20)
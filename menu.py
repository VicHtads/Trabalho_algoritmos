import main as m

def exibir_menu():
    print("\n--- Sistema de Gerenciamento de Eventos Tech ---")
    print("1. Listar todos os eventos")
    print("2. Cadastrar novo participante")
    #print("3. Listar todos os participantes")
    # Futuras opções aqui
    print("0. Sair")
    print("--------------------------------------------------")

def listar_todos_eventos():# Exibe no terminal a lista de todos eventos cadastrados.
    print("\n--- Lista de Eventos Cadastrados ---")

    if not m.lista_eventos:
        print("Nenhum evento cadastrado no sistema")
        return
    for evento in m.lista_eventos:# Acesso dos valores do dicionário evento por suas chaves
        nome = evento["nome"]
        data = evento["data"]
        tema = evento["tema"]
        num_inscritos = len(evento["inscritos"])

        print(f"- {nome} ({tema})")
        print(f" Data: {data} | Inscritos: {num_inscritos}")
        print("-" * 20)

def sair_do_sistema():
    print("Saindo do sistema. Até logo!")
    return "SAIR"
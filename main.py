from dados import PARTICIPANTES_DADOS, EVENTOS_DADOS 
import participante as p
import menu
# Listas globais
lista_participantes = []
lista_eventos = []


def carrgar_dados():# Função para carregar e ler os dados importados de forma reutilizavel
    global lista_participantes, lista_eventos
# copy() está sendo usado para evitar mudanças inesperadas na lista original.
    lista_participantes = PARTICIPANTES_DADOS.copy()
    lista_eventos = EVENTOS_DADOS.copy()
    print(">>> Dados carregados com sucesso!")


# --- Ponto de Entrada do Sistema ---
if __name__ == "__main__":
    carrgar_dados()

    opcoes_menu = {
        "1": menu.listar_todos_eventos,
        "0": menu.sair_do_sistema,
        "2": p.cadastro_participante,
        #"3": p.listar_todos_participantes,
    }

    # Loop principal do programa
    while True:
        menu.exibir_menu()
        opcao = input("Escolha uma opção: ").strip()# .strip() Serve para reduzir os erros do usuário utilizando somente o que é conveniênte
        funcao_a_executar = opcoes_menu.get(opcao)# .get() ajuda a lidar com opções inválidas, visto que ele não gera erros caso não encontre o que foi pedido

        if funcao_a_executar:
            # Se o .get() encontrar a função, o programa a executa
            resultado = funcao_a_executar()
            if resultado == "SAIR":
                break # Executa a chamada da função e sai do sistema
        else:
            # Se a função não foi encontrada no dicionário, então:
            print("Opção inválida! Por favor, tente novamente.")

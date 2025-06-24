# Arquivo: main.py
# Este arquivo será o motor do sistem. Onde todo o sistema será executado

from dados import PARTICIPANTES_DADOS, EVENTOS_DADOS
import participante
import menu
import eventos

lista_participantes = []
lista_eventos = []

def carrgar_dados():
    global lista_participantes, lista_eventos
    # copy() está sendo usado para evitar mudanças inesperadas na lista original.
    lista_participantes.extend(PARTICIPANTES_DADOS)
    lista_eventos.extend(EVENTOS_DADOS)
    print(">>> Dados carregados com sucesso!")

# --- Ponto de Entrada do Sistema ---
if __name__ == "__main__":
    carrgar_dados()

    opcoes_menu = {
        "1": lambda: eventos.listar_todos_eventos(lista_eventos),
        "2": lambda: participante.cadastro_participante(lista_participantes),
        "3": lambda: participante.listar_todos_participantes(lista_participantes),
        "0": lambda: menu.sair_do_sistema(),
    }

    # Loop principal do programa
    while True:
        menu.exibir_menu()
        opcao = input("Escolha uma das opções apresentadas: ").strip()# .strip() Serve para reduzir os erros do usuário utilizando somente o que é conveniênte
        funcao_a_executar = opcoes_menu.get(opcao)# .get() ajuda a lidar com opções inválidas, visto que ele não gera erros caso não encontre o que foi pedido

        if funcao_a_executar:
            # Se o .get() encontrar a função, o programa a executa
            resultado = funcao_a_executar()
            if resultado == "SAIR":
                break # Executa a chamada da função e sai do sistema
        else:
            # Se a função não foi encontrada no dicionário, então:
            print("Opção inválida! Por favor, tente novamente.")

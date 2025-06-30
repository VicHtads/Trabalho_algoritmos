# Arquivo: main.py
# Este arquivo será o motor do sistem. Onde todo o sistema será executado

from dados import PARTICIPANTES_DADOS, EVENTOS_DADOS, PALESTRANTE_DADOS
import participante
import menu
import eventos
import relatorios
import palestrantes

lista_palestrantes = []
lista_participantes = []
lista_eventos = []

def carregar_dados():
    lista_participantes.extend(PARTICIPANTES_DADOS)
    lista_eventos.extend(EVENTOS_DADOS)
    lista_palestrantes.extend(PALESTRANTE_DADOS)
    print(">>> Dados carregados com sucesso!")

# --- Funções de Sub-Menu ---

def gerenciar_eventos_sub_menu():
    """
    Gerencia todas as operações relacionadas a eventos.
    """

    opcoes = {
        '1': lambda: eventos.listar_todos_eventos(lista_eventos),
        '2': lambda: eventos.adicionar_novo_evento(lista_eventos, lista_palestrantes),
        '3': lambda: eventos.atualizar_evento(lista_eventos, lista_palestrantes),
        '4': lambda: eventos.remover_evento(lista_eventos),
        '5': lambda: eventos.buscar_eventos_por_tema(lista_eventos),
        '6': lambda: eventos.listar_participante_evento_especifico(lista_eventos, lista_participantes),
    }

    while True:
        menu.exibir_menu_eventos()
        opcao = input("Escolha uma opção para Eventos: ").strip()
        if opcao == '0': break
        funcao = opcoes.get(opcao)
        if funcao: funcao()
        else: print("[ERRO] Opção inválida.")

def gerenciar_participantes_sub_menu():
    """
    Gerencia todas as operações relacionadas a participantes.
    """

    opcoes = {
        '1': lambda: participante.listar_todos_participantes(lista_participantes),
        '2': lambda: participante.cadastro_participante(lista_participantes, lista_eventos),
        '3': lambda: participante.atualizar_participante(lista_participantes),
        '4': lambda: participante.remover_participante(lista_participantes, lista_eventos),
        '5': lambda: participante.buscar_participante_por_id(lista_participantes),
    }

    while True:
        menu.exibir_menu_participantes()
        opcao = input("Escolha uma opção para Participantes: ").strip()
        if opcao == '0': break
        funcao = opcoes.get(opcao)
        if funcao: funcao()
        else: print("[ERRO] Opção inválida.")

def gerenciar_palestrantes_sub_menu():
    """
    Gerencia todas as operações relacionadas a palestrantes.
    """

    opcoes = {
        '1': lambda: palestrantes.listar_todos_palestrantes(lista_palestrantes),
        '2': lambda: palestrantes.adicionar_novo_palestrante(lista_palestrantes),
        '3': lambda: palestrantes.ver_detalhes_palestrante(lista_palestrantes, lista_eventos),
    }

    while True:
        menu.exibir_menu_palestrantes()
        opcao = input("Escolha uma opção para Palestrantes: ").strip()
        if opcao == '0': break
        funcao = opcoes.get(opcao)
        if funcao: funcao()
        else: print("[ERRO] Opção inválida.")

def relatorios_sub_menu():
    """
    Gerencia a exibição de todos os relatórios.
    """

    opcoes = {
        '1': lambda: relatorios.relatorio_temas_populares(lista_eventos),
        '2': lambda: relatorios.relatorio_participantes_ativos(lista_eventos, lista_participantes),
        '3': lambda: relatorios.relatorio_baixa_adesao(lista_eventos),
    }

    while True:
        menu.exibir_menu_relatorios()
        opcao = input("Escolha uma opção para Relatórios: ").strip()
        if opcao == '0':
            break
        funcao = opcoes.get(opcao)
        if funcao: funcao()
        else: print("[ERRO] Opção inválida.")

# --- Ponto de Entrada Principal ---
if __name__ == "__main__":
    carregar_dados()

    while True:
        menu.exibir_menu_principal()
        opcao_main = input("Digite o número da área que deseje gerenciar: ").strip()

        if opcao_main == '1': gerenciar_eventos_sub_menu()
        elif opcao_main == '2': gerenciar_participantes_sub_menu()
        elif opcao_main == '3': gerenciar_palestrantes_sub_menu()
        elif opcao_main == '4': relatorios_sub_menu()
        elif opcao_main == '0':
            menu.sair_do_sistema()
            break
        else:
            print("[ERRO] Opção principal inválida.")

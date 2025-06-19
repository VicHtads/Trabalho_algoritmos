from dados import carrgar_dados, lista_eventos, lista_participantes
import participante
import menu
import eventos

# --- Ponto de Entrada do Sistema ---
if __name__ == "__main__":
    carrgar_dados()
    # --- DEBUG CHECKPOINT 2 ---
    print(f"--- DEBUG: Após a chamada de carregar_dados, a lista global de participantes tem {len(lista_participantes)} itens.")

    opcoes_menu = {
        "1": eventos.listar_todos_eventos,
        "0": menu.sair_do_sistema,
        "2": participante.cadastro_participante,
        "3": participante.listar_todos_participantes,
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

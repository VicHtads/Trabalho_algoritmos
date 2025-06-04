from dados import PARTICIPANTES_DADOS, EVENTOS_DADOS 

# Listas globais
lista_participantes = []
lista_eventos = []


def carrgar_dados():# Função para carregar e ler os dados importados de forma reutilizavel
    global lista_participantes, lista_eventos
# copy() está sendo usado para evitar mudanças inesperadas na lista original.
    lista_participantes = PARTICIPANTES_DADOS.copy()
    lista_eventos = EVENTOS_DADOS.copy()
    print('>>> Dados carregados com sucesso!')

def exibir_menu():
    print('\n--- Sistema de Gerenciamento de Eventos Tech ---')
    print('1. Listar todos os eventos')
    # Futuras opções aqui
    print('0. Sair')
    print('--------------------------------------------------')

def listar_todos_eventos():# Exibe no terminal a lista de todos eventos cadastrados.
    print('\n--- Lista de Eventos Cadastrados ---')

    if not lista_eventos:
        print('Nenhum evento cadastrado no sistema')
        return
    for evento in lista_eventos:# Acesso dos valores do dicionário evento por suas chaves
        nome = evento['nome']
        data = evento['data']
        tema = evento['tema']
        num_inscritos = len(evento['inscritos'])

        print(f'- {nome} ({tema})')
        print(f' Data: {data} | Inscritos: {num_inscritos}')
        print('-' * 20)

def sair_do_sistema():
    print('Saindo do sistema. Até logo!')
    return 'SAIR'

# --- Ponto de Entrada do Sistema ---
if __name__ == '__main__':
    carrgar_dados()

    opcoes_menu = {
        '1': listar_todos_eventos,
        '0': sair_do_sistema,
    }

    # Loop principal do programa
    while True:
        exibir_menu()
        opcao = input('Escolha uma opção: ').strip()# .strip() Serve para reduzir os erros do usuário utilizando somente o que é conveniênte
        funcao_a_executar = opcoes_menu.get(opcao)# .get() ajuda a lidar com opções inválidas, visto que ele não gera erros caso não encontre o que foi pedido

        if funcao_a_executar:
            # Se o .get() encontrar a função, o programa a executa
            resultado = funcao_a_executar()
            if resultado == 'SAIR':
                break # Executa a chamada da função e sai do sistema
        else:
            # Se a função não foi encontrada no dicionário, então:
            print('Opção inválida! Por favor, tente novamente.')

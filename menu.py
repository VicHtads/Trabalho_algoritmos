# Arquivo: menu.py
# Este arquivo terá toda a 'interface' do sistema, com suas respectivas opções de mostragem.
from utils import exibir_cabecalho

def exibir_menu():
    exibir_cabecalho("Sistema de Gerenciamento de Eventos Tech")
    print("1. Listar todos os eventos")
    print("2. Cadastrar novo participante")
    print("3. Listar todos os participantes")
    print("4. Listar participantes de evento especifico")
    print("5. Buscar participante por ID")
    # Futuras opções aqui
    print("0. Sair")
    print("--------------------------------------------------")

def sair_do_sistema():
    print("Saindo do sistema. Até logo!")
    return "SAIR"
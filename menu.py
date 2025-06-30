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
    print("6. Gerar relatório de temas populares")
    print("7. Adicionar novo palestrante")
    print("8. Listar todos os palestrantes")
    print("9. Ver detalhes de um palestrante")
    print("10. Remover participante")
    print("11. Atualizar dados de participante")
    print("12. Adicionar novo evento")
    print("13. Remover evento")
    print("14. Atualizar dados de eventos")
    # Futuras opções aqui
    print("0. Sair")
    print("--------------------------------------------------")

def sair_do_sistema():
    print("Saindo do sistema. Até logo!")
    return "SAIR"
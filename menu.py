# Arquivo: menu.py
# Este arquivo terá toda a 'interface' do sistema, com suas respectivas opções de mostragem.
from utils import exibir_cabecalho

def exibir_menu_principal():
    exibir_cabecalho("Sistema de Gerenciamento de Eventos - Menu Principal")
    print("1. Gerenciar Eventos")
    print("2. Gerenciar Participantes")
    print("3. Gerenciar Palestrantes")
    print("4. Relatórios e Ferramentas")
    print("\n0. Sair do Sistema")
    print("-" * 60)


def exibir_menu_eventos():
    exibir_cabecalho("Gerenciar Eventos")
    print("1. Listar todos os eventos")
    print("2. Adicionar novo evento")
    print("3. Atualizar evento")
    print("4. Remover evento")
    print("5. Buscar eventos por tema")
    print("6. Listar participantes de um evento")
    print("\n0. Voltar ao menu principal")
    print("-" * 60)


def exibir_menu_participante():
    exibir_cabecalho("Gerenciar Participantes")
    print("1. Listar todos os participantes")
    print("2. Adicionar novo participante")
    print("3. Atualizar dados de participante")
    print("4. Remover participante")
    print("5. Buscar participante por ID")
    print("\n0. Voltar ao menu principal")
    print("-" * 60)


def exibir_menu_palestrante():
    exibir_cabecalho("Gerenciar Palestrantes")
    print("1. Listar todos os palestrantes")
    print("2. Adicionar novo palestrante")
    print("3. Ver detalhes de um palestrante")
    print("\n0. Voltar ao menu principal")
    print("-" * 60)


def exibir_menu_relatorios():
    exibir_cabecalho("Relatórios e Ferramentas")
    print("1. Relatório de temas mais populares")
    print("2. Relatório de participantes mais ativos")
    print("3. Alerta de eventos com baixa adesão")
    print("\n0. Voltar ao menu principal")
    print("-" * 60)


def sair_do_sistema():
    print("Saindo do sistema. Até logo!")
    return "SAIR"
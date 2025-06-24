# Arquivo: dados.py
# Este arquivo simula os dados prontos que o sistema deve importar.

PARTICIPANTES_DADOS = [
    {"id": 1, "nome": "Carlos Silva", "email": "carlos.silva@email.com", "preferencias_tematicas": ["Inteligência Artificial", "Segurança"]},
    {"id": 2, "nome": "Beatriz Santos", "email": "beatriz.santos@email.com", "preferencias_tematicas": ["Web", "Inteligência Artificial"]},
    {"id": 3, "nome": "Lucas Oliveira", "email": "lucas.oliveira@email.com", "preferencias_tematicas": ["Segurança", "Dados"]},
    {"id": 4, "nome": "Juliana Pereira", "email": "juliana.pereira@email.com", "preferencias_tematicas": ["Web"]},
    {"id": 5, "nome": "Fernando Costa", "email": "fernando.costa@email.com", "preferencias_tematicas": ["Inteligência Artificial", "Dados"]},
]

EVENTOS_DADOS = [
    {"nome": "Workshop de IA", "data": "2025-08-15", "tema": "Inteligência Artificial", "inscritos": [1, 2, 5]},
    {"nome": "Segurança em Foco", "data": "2025-09-02", "tema": "Segurança", "inscritos": [1, 3]},
    {"nome": "Desenvolvimento Web Moderno", "data": "2025-09-20", "tema": "Web", "inscritos": [2, 4]},
    {"nome": "Hackathon de Dados", "data": "2025-10-10", "tema": "Dados", "inscritos": [3, 5]},
    {"nome": "Palestra sobre Carreira Tech", "data": "2025-11-05", "tema": "Carreira", "inscritos": [1, 2, 3, 4, 5]},
    {"nome": "Minicurso de Git", "data": "2025-11-25", "tema": "Ferramentas", "inscritos": []} # Evento sem inscritos ainda | Utilizado para testes de novos registros
]
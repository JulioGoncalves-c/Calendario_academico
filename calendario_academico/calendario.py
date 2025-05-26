import json
import os
from eventos import Evento

class Calendario:
    def __init__(self, usuario=None):
        # Cria um arquivo de eventos único para cada usuário
        self.arquivo = f'eventos_{usuario}.json' if usuario else 'eventos.json'
        self.eventos = []
        self.carregar_eventos()

    def carregar_eventos(self):
        # Lê o arquivo JSON correspondente ao usuário
        if os.path.exists(self.arquivo):
            with open(self.arquivo, 'r', encoding='utf-8') as f:
                dados = json.load(f)
                self.eventos = [Evento.from_dict(e) for e in dados]

    def salvar_eventos(self):
        # Salva os eventos do usuário no seu arquivo próprio
        with open(self.arquivo, 'w', encoding='utf-8') as f:
            json.dump([e.to_dict() for e in self.eventos], f, ensure_ascii=False, indent=4)

    def adicionar_evento(self, evento):
        self.eventos.append(evento)
        self.salvar_eventos()

    def listar_eventos(self):
        return self.eventos

    def limpar_eventos(self):
        self.eventos = []
        self.salvar_eventos()
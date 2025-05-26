# calendario.py - responsável por gerenciar e armazenar os eventos

import json  # Módulo para leitura e escrita de arquivos JSON
import os    # Módulo para interagir com o sistema de arquivos
from eventos import Evento  # Importa a classe Evento usada para representar cada evento individual

class Calendario:
    def __init__(self):
        # Caminho do arquivo onde os eventos serão salvos
        self.arquivo = 'eventos.json'
        # Lista que armazenará os objetos do tipo Evento
        self.eventos = []
        # Tenta carregar os eventos do arquivo logo ao iniciar
        self.carregar_eventos()

    def carregar_eventos(self):
        # Verifica se o arquivo existe antes de tentar ler
        if os.path.exists(self.arquivo):
            with open(self.arquivo, 'r', encoding='utf-8') as f:
                dados = json.load(f)  # Carrega os dados do JSON como uma lista de dicionários
                self.eventos = [Evento.from_dict(e) for e in dados]  # Converte cada dicionário para objeto Evento

    def salvar_eventos(self):
        # Converte a lista de objetos Evento em uma lista de dicionários e salva em JSON
        with open(self.arquivo, 'w', encoding='utf-8') as f:
            json.dump([e.to_dict() for e in self.eventos], f, ensure_ascii=False, indent=4)

    def adicionar_evento(self, evento):
        # Adiciona um novo evento na lista e salva
        self.eventos.append(evento)
        self.salvar_eventos()

    def listar_eventos(self):
        # Retorna a lista de eventos
        return self.eventos

    def limpar_eventos(self):
        # Limpa todos os eventos e atualiza o arquivo
        self.eventos = []
        self.salvar_eventos()
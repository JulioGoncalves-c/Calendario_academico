# eventos.py - define a classe Evento, responsável por representar os dados de cada evento no sistema

class Evento:
    def __init__(self, titulo, data, tipo, prioridade='media', realizado=False):
        # Construtor da classe. Inicializa os atributos com os valores passados na criação do objeto.
        self.titulo = titulo            # Nome do evento (ex: Prova de Matemática)
        self.data = data                # Data do evento no formato 'dd/mm/aaaa'
        self.tipo = tipo                # Tipo do evento (aula, prova, reforco, feriado...)
        self.prioridade = prioridade    # Prioridade: baixa, média ou alta
        self.realizado = realizado      # Status: True se já aconteceu, False se ainda está por vir

    def __str__(self):
        # Representação textual simples do evento quando ele for impresso
        return f"{self.data} - {self.tipo.upper()}: {self.titulo}"

    def to_dict(self):
        # Converte o objeto Evento em um dicionário (para salvar no JSON)
        return {
            "titulo": self.titulo,
            "data": self.data,
            "tipo": self.tipo,
            "prioridade": self.prioridade,
            "realizado": self.realizado
        }

    @staticmethod
    def from_dict(d):
        # Método estático que cria um objeto Evento a partir de um dicionário (carregado do JSON)
        return Evento(
            d.get("titulo"),
            d.get("data"),
            d.get("tipo"),
            d.get("prioridade", "media"),
            d.get("realizado", False)
        )

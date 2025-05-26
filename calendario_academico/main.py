# main.py - versão comentada com ordenação, status, remoção por número

from eventos import Evento           # Importa a classe que representa um evento
from calendario import Calendario   # Importa a classe que gerencia os eventos cadastrados
from datetime import datetime       # Importa datetime para lidar com datas

calendario = Calendario()  # Cria um objeto do calendário com os eventos carregados do JSON

# Função principal com menu de opções do sistema

def menu():
    while True:
        print("\nMenu:")
        print("1. Adicionar novo evento")
        print("2. Listar todos os eventos")
        print("3. Listar eventos por tipo")
        print("4. Remover evento por número")
        print("5. Alterar data de um evento")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            # Entrada dos dados para criar um novo evento
            titulo = input("Título do evento: ")
            data = input("Data (DD/MM/AAAA): ")
            tipo = input("Tipo (aula, reforco, prova, feriado): ").lower()
            prioridade = input("Prioridade (baixa, media, alta): ").lower()
            realizado = input("O evento foi realizado? (s/n): ").lower() == "s"

            # Criação e adição do evento
            evento = Evento(titulo, data, tipo, prioridade, realizado)
            calendario.adicionar_evento(evento)
            print("Evento adicionado com sucesso!")

        elif opcao == "2":
            # Exibe todos os eventos ordenados por data
            if not calendario.eventos:
                print("Nenhum evento cadastrado.")
            else:
                print("\nEventos cadastrados:")
                eventos_ordenados = sorted(calendario.eventos, key=lambda e: datetime.strptime(e.data, "%d/%m/%Y"))
                hoje = datetime.today()
                for i, ev in enumerate(eventos_ordenados):
                    data_evento = datetime.strptime(ev.data, "%d/%m/%Y")
                    status = "Realizado" if ev.realizado else ("Pendente" if data_evento >= hoje else "Atrasado")
                    print(f"[{i}] {ev.data} - {ev.tipo.upper()} - {ev.titulo} ({ev.prioridade.upper()} - {status})")

        elif opcao == "3":
            # Filtro por tipo de evento
            tipo = input("Digite o tipo de evento para filtrar (aula, reforco, prova, feriado): ").lower()
            encontrados = [e for e in calendario.eventos if e.tipo == tipo]
            if encontrados:
                for e in encontrados:
                    print(f"{e.data} - {e.titulo} ({e.prioridade})")
            else:
                print("Nenhum evento encontrado para esse tipo.")

        elif opcao == "4":
            # Remoção de evento por número/index na lista
            if not calendario.eventos:
                print("Nenhum evento para remover.")
            else:
                eventos_ordenados = sorted(calendario.eventos, key=lambda e: datetime.strptime(e.data, "%d/%m/%Y"))
                for i, ev in enumerate(eventos_ordenados):
                    print(f"[{i}] {ev.data} - {ev.tipo.upper()} - {ev.titulo}")
                try:
                    indice = int(input("Digite o número do evento que deseja remover: "))
                    if 0 <= indice < len(eventos_ordenados):
                        evento = eventos_ordenados[indice]
                        calendario.eventos.remove(evento)
                        calendario.salvar_eventos()
                        print(f"Evento '{evento.titulo}' removido com sucesso!")
                    else:
                        print("Índice inválido.")
                except ValueError:
                    print("Entrada inválida. Digite um número.")

        elif opcao == "5":
            # Alterar data de um evento específico
            titulo = input("Título do evento a editar: ")
            data_antiga = input("Data atual do evento (DD/MM/AAAA): ")
            nova_data = input("Nova data (DD/MM/AAAA): ")
            for evento in calendario.eventos:
                if evento.titulo == titulo and evento.data == data_antiga:
                    evento.data = nova_data
                    calendario.salvar_eventos()
                    print("Data do evento atualizada com sucesso!")
                    break
            else:
                print("Evento não encontrado.")

        elif opcao == "6":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Inicia o menu interativo quando o programa é executado diretamente
if __name__ == '__main__':
    menu()
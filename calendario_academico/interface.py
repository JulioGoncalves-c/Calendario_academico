from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import Calendar
from eventos import Evento
from calendario import Calendario
from datetime import datetime

class AgendaTI:
    def __init__(self, root):
        self.root = root
        self.root.title("agendaTI - Calendário Acadêmico")
        self.root.geometry("1100x700")
        self.calendario = Calendario()

        self.root.configure(bg="#f0f4ff")

        Label(self.root, text="CALENDÁRIO ACADÊMICO - agendaTI", font=("Arial", 16, "bold"), bg="#003366", fg="white", pady=10).pack(fill=X)

        main_frame = Frame(self.root, bg="#f0f4ff")
        main_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

        left_frame = Frame(main_frame, bg="#f0f4ff")
        left_frame.pack(side=LEFT, padx=10, pady=10)

        Label(left_frame, text="Selecione a data", bg="#f0f4ff", font=("Arial", 10)).pack()
        self.cal = Calendar(left_frame, date_pattern='dd/mm/yyyy')
        self.cal.pack(pady=5)

        Button(left_frame, text="Adicionar Evento", command=self.adicionar_evento, bg="#003366", fg="white").pack(pady=5)
        Button(left_frame, text="Remover Evento", command=self.remover_evento, bg="#aa3333", fg="white").pack(pady=5)

        Label(left_frame, text="Título:", bg="#f0f4ff").pack(anchor="w")
        self.entry_titulo = Entry(left_frame, width=30)
        self.entry_titulo.pack()

        Label(left_frame, text="Tipo:", bg="#f0f4ff").pack(anchor="w")
        self.entry_tipo = Entry(left_frame, width=30)
        self.entry_tipo.pack()

        Label(left_frame, text="Prioridade:", bg="#f0f4ff").pack(anchor="w")
        self.prioridade = StringVar(value="media")
        OptionMenu(left_frame, self.prioridade, "baixa", "media", "alta").pack()

        Label(left_frame, text="Status:", bg="#f0f4ff").pack(anchor="w")
        self.status_var = StringVar(value="Pendente")
        OptionMenu(left_frame, self.status_var, "Pendente", "Concluído", "Atrasado").pack()

        right_frame = Frame(main_frame, bg="#ffffff", bd=2, relief=GROOVE)
        right_frame.pack(side=RIGHT, fill=BOTH, expand=True, padx=10, pady=10)

        Label(right_frame, text="Eventos do Mês", font=("Arial", 12, "bold"), bg="#ffffff").pack()

        filtro_frame = Frame(right_frame, bg="#ffffff")
        filtro_frame.pack(pady=5)

        Label(filtro_frame, text="Filtrar por status:", bg="#ffffff").pack(side=LEFT)
        self.filtro_status = StringVar(value="Todos")
        OptionMenu(filtro_frame, self.filtro_status, "Todos", "Pendente", "Concluído", "Atrasado").pack(side=LEFT, padx=5)
        Button(filtro_frame, text="Filtrar", command=self.aplicar_filtro).pack(side=LEFT, padx=5)
        Button(filtro_frame, text="Limpar filtro", command=self.atualizar_tabela).pack(side=LEFT)

        columns = ("Data", "Título", "Tipo", "Prioridade", "Status")
        self.tree = ttk.Treeview(right_frame, columns=columns, show='headings', height=20)
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")
        self.tree.pack(fill=BOTH, expand=True, padx=10, pady=10)

        self.tree.tag_configure("atrasado", background="#ffe5e5")
        self.tree.tag_configure("realizado", background="#e0ffe0")
        self.tree.tag_configure("pendente", background="#fffce0")

        self.atualizar_tabela()

    def adicionar_evento(self):
        titulo = self.entry_titulo.get()
        tipo = self.entry_tipo.get().lower()
        prioridade = self.prioridade.get()
        status_escolhido = self.status_var.get()
        realizado = True if status_escolhido == "Concluído" else False
        data = self.cal.get_date()

        if not titulo or not tipo:
            messagebox.showwarning("Campos obrigatórios", "Preencha todos os campos.")
            return

        if tipo not in ["aula", "reforco", "prova", "feriado"]:
            messagebox.showerror("Erro", "Tipo inválido. Use: aula, reforco, prova ou feriado.")
            return

        evento = Evento(titulo, data, tipo, prioridade, realizado)
        self.calendario.adicionar_evento(evento)
        self.calendario.salvar_eventos()
        self.atualizar_tabela()
        messagebox.showinfo("Sucesso", "Evento adicionado com sucesso!")

        self.entry_titulo.delete(0, END)
        self.entry_tipo.delete(0, END)
        self.status_var.set("Pendente")
        self.prioridade.set("media")

    def remover_evento(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Nenhum selecionado", "Selecione um evento na tabela para remover.")
            return

        item = self.tree.item(selected[0])
        valores = item['values']
        data, titulo = valores[0], valores[1]

        for evento in self.calendario.eventos:
            if evento.data == data and evento.titulo == titulo:
                self.calendario.eventos.remove(evento)
                break

        self.calendario.salvar_eventos()
        self.atualizar_tabela()
        messagebox.showinfo("Removido", "Evento removido com sucesso!")

    def atualizar_tabela(self, eventos_filtrados=None):
        for row in self.tree.get_children():
            self.tree.delete(row)

        eventos = eventos_filtrados if eventos_filtrados is not None else self.calendario.eventos
        eventos_ordenados = sorted(eventos, key=lambda e: datetime.strptime(e.data, "%d/%m/%Y"))

        for e in eventos_ordenados:
            status = "Concluído" if e.realizado else "Pendente"
            data_evento = datetime.strptime(e.data, "%d/%m/%Y")
            hoje = datetime.today()
            if not e.realizado and data_evento < hoje:
                status = "Atrasado"

            cor = "realizado" if status == "Concluído" else ("atrasado" if status == "Atrasado" else "pendente")

            self.tree.insert("", END, values=(e.data, e.titulo, e.tipo, e.prioridade, status), tags=(cor,))

    def aplicar_filtro(self):
        status_desejado = self.filtro_status.get()
        if status_desejado == "Todos":
            self.atualizar_tabela()
            return

        eventos_filtrados = []
        for e in self.calendario.eventos:
            status = "Concluído" if e.realizado else "Pendente"
            data_evento = datetime.strptime(e.data, "%d/%m/%Y")
            hoje = datetime.today()
            if not e.realizado and data_evento < hoje:
                status = "Atrasado"
            if status == status_desejado:
                eventos_filtrados.append(e)

        self.atualizar_tabela(eventos_filtrados)

if __name__ == '__main__':
    root = Tk()
    app = AgendaTI(root)
    root.mainloop()

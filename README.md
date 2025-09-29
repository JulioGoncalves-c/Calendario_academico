Calendário Acadêmico - agendaTI

Um sistema de calendário acadêmico desenvolvido em **Python**, com versões em **linha de comando (CLI)** e **interface gráfica (GUI)**.  
Permite organizar aulas, provas e eventos acadêmicos, com suporte a **multiusuário**, **status de eventos** e integração com **feriados nacionais**.

---
Funcionalidades
- Login multiusuário com autenticação via arquivo `usuarios.txt`
- Cadastro, edição e remoção de eventos
- Persistência em arquivos JSON separados por usuário (ex: `eventos.json`, `eventos_Andrea.json`)
- Classificação por prioridade (baixa, média, alta)
- Status dos eventos: **Pendente, Concluído, Atrasado**
- Filtro por status
- Integração com feriados nacionais (biblioteca `holidays`)
- Interface gráfica amigável feita em **Tkinter + tkcalendar**
- Destaque visual de eventos (cores diferentes para status)

---

Tecnologias Utilizadas
- **Python 3**
- **Tkinter** + **tkcalendar** (interface gráfica)
- **JSON** (persistência de dados)
- **holidays** (feriados nacionais do Brasil)
- **Pillow** (tratamento de imagens na interface)

---

Como Executar

### 1. Clone o repositório
```bash
git clone https://github.com/SEU_USUARIO/calendario-academico.git
cd calendario-academico

pip install tkcalendar holidays pillow
python main.py
python interface.py

Estrutura do Projeto

eventos.py → classe Evento (representa cada atividade)

calendario.py → classe Calendario (gerencia eventos e persistência em JSON)

main.py → versão CLI com menu interativo

interface.py → versão GUI com Tkinter

usuarios.txt → credenciais de usuários

eventos.json / eventos_<usuario>.json → eventos cadastrados

# 🧠 TDD - Gerenciador de Itens

Este projeto é um exemplo prático de **Desenvolvimento Orientado a Testes (TDD)** em Python.  
O sistema consiste em um **gerenciador de itens/tarefas**, com funcionalidades básicas de adicionar, listar, concluir e remover itens, desenvolvido passo a passo com **pytest**.

---

## 🚀 Funcionalidades

- ✅ Adicionar novo item (com título e detalhes)
- 🗂️ Listar todos os itens
- 🏁 Marcar item como concluído
- ❌ Remover item existente
- ⚠️ Validação para evitar títulos vazios ou duplicados

---

## 🧩 Estrutura do Projeto

```
TDD-Julliana-Rodrigues/
│
├── item.py                 # Classe Item (representa uma tarefa)
├── controlador.py          # Classe ControladorDeItens (gerencia a lista de itens)
├── test_controlador.py     # Testes automatizados com pytest
└── README.md               # Documentação do projeto
```

---

## 🧠 Conceito: TDD (Test Driven Development)

O ciclo **TDD** é seguido em três etapas principais:

1. 🔴 **RED** — Escreva um teste que falha.
2. 🟢 **GREEN** — Implemente o código mínimo para o teste passar.
3. ♻️ **REFACTOR** — Melhore o código, mantendo os testes verdes.

> Cada commit do projeto reflete uma dessas etapas.

---

## 🧪 Executando os Testes

### 1️⃣ Instalar as dependências

Certifique-se de ter o Python instalado.  
No terminal, execute:

```bash
pip install pytest
```

### 2️⃣ Executar os testes

Rode todos os testes automatizados com:

```bash
pytest -v
```

O `-v` (verbose) mostra os detalhes de cada teste executado.

---

## 💻 Exemplo de Uso

```python
from controlador import ControladorDeItens

c = ControladorDeItens()

c.adicionar_item("Estudar Python", "Praticar TDD com pytest")
c.adicionar_item("Fazer exercícios", "Resolver desafios no VS Code")

print(c.listar_itens())

c.finalizar_item("Estudar Python")
print(c.listar_itens())

c.remover_item("Fazer exercícios")
print(c.listar_itens())
```

Saída esperada:
```python
[
  {'titulo': 'Estudar Python', 'detalhes': 'Praticar TDD com pytest', 'estado': 'pendente'},
  {'titulo': 'Fazer exercícios', 'detalhes': 'Resolver desafios no VS Code', 'estado': 'pendente'}
]
[
  {'titulo': 'Estudar Python', 'detalhes': 'Praticar TDD com pytest', 'estado': 'concluído'},
  {'titulo': 'Fazer exercícios', 'detalhes': 'Resolver desafios no VS Code', 'estado': 'pendente'}
]
[
  {'titulo': 'Estudar Python', 'detalhes': 'Praticar TDD com pytest', 'estado': 'concluído'}
]
```

---

## 🧱 Tecnologias Utilizadas

- 🐍 **Python 3.10+**
- 🧪 **pytest** (para testes automatizados)
- 💡 **Git & GitHub** (para versionamento e histórico TDD)

---

## 🧭 Histórico de Commits

| Etapa | Commit | Descrição |
|-------|---------|------------|
| 🔴 RED | `error - TDD-RED` | Criação inicial dos testes que falham |
| 🟢 GREEN | `TDD - Green` | Implementação mínima para os testes passarem |
| ♻️ REFACTOR | `TDD-REFACTOR` | Melhorias no código mantendo testes verdes |

---

## 🧩 Próximos Passos (para prática de TDD)

- Implementar persistência de dados (salvar tarefas em arquivo JSON)
- Adicionar filtros (`listar_itens(status="pendente")`)
- Criar método de atualização de item (`editar_item`)
- Criar interface de linha de comando (CLI)

---

## 👩‍💻 Autora

**Julliana F. Rodrigues**  
💼 Projeto de estudo sobre TDD em Python  
🔗 [GitHub - JullianaF](https://github.com/JullianaF)

---

## 🪄 Licença

Este projeto é de uso livre para fins de estudo e aprendizado.  
Sinta-se à vontade para clonar, modificar e praticar o fluxo TDD.

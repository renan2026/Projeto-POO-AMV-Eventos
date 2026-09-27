# Amv Eventos

![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white)
![Paradigma](https://img.shields.io/badge/Paradigma-POO-1F3A5F)
![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-2E8B57)

Sistema em Python, desenvolvido com **Programação Orientada a Objetos**, para organizar a logística de entrega de materiais de cozinha em eventos: motoristas, veículos, materiais, itens de entrega e o andamento de cada evento.

> Projeto acadêmico da disciplina de Programação Orientada a Objetos.

---

## Sumário

- [Sobre o projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Diagrama de classes](#diagrama-de-classes)
- [Estrutura do repositório](#estrutura-do-repositório)
- [Como executar](#como-executar)
- [Exemplo de uso](#exemplo-de-uso)
- [Tecnologias](#tecnologias)
- [Equipe](#equipe)
- [Documentação](#documentação)

---

## Sobre o projeto

Eventos que dependem de estrutura de cozinha precisam que panelas, utensílios e equipamentos cheguem ao local certo, na quantidade certa e no dia combinado. Quando esse controle é feito à mão, é fácil perder informações como qual motorista ficou responsável, qual veículo foi usado e o que foi enviado.

O **Amv Eventos** modela essa logística em cinco classes. Cada evento registra data, destino, motorista, veículo e a lista de itens transportados, além de um status que acompanha o seu andamento.

## Funcionalidades

| Classe | O que faz |
|---|---|
| `Motorista` | Cadastra e atualiza nome, CPF e CNH. Na atualização, só os campos informados são alterados. |
| `Veiculo` | Cadastra e atualiza placa, modelo e capacidade. Recusa capacidade zero ou negativa. |
| `MaterialCozinha` | Cadastra e atualiza nome, tipo e descrição dos materiais transportados. |
| `ItemEntrega` | Associa um material a uma quantidade; permite adicionar e remover unidades, com validação. |
| `Evento` | Reúne data, destino, motorista, veículo e itens; controla o status do evento. |

### Ciclo de vida do evento

```
Pendente ──criar()──► Criado ──finalizar()──► Finalizado
                         │
                         └────cancelar()────► Cancelado
```

## Diagrama de classes

![Diagrama de classes](docs/diagrama_de_classes.png)

| Relação | Multiplicidade | Significado |
|---|---|---|
| Motorista e Evento | 1 para 0..* | Um motorista pode conduzir vários eventos. |
| Veiculo e Evento | 1 para 0..* | Um veículo pode ser usado em vários eventos. |
| Evento e ItemEntrega (agregação) | 1 para 0..* | Um evento reúne vários itens de entrega. |
| ItemEntrega e MaterialCozinha | 0..* para 1 | Cada item se refere a um material. |

## Estrutura do repositório

```
Projeto-POO-AMV-Eventos/
├── src/
│   └── amv_eventos.py                        # Código-fonte com as classes e o teste
├── docs/
│   ├── diagrama_de_classes.png               # Diagrama exportado (imagem)
│   ├── diagrama_de_classes.drawio            # Arquivo editável do draw.io
│   └── Relatorio_Projeto_POO_Amv_Eventos.pdf # Relatório do projeto
├── .gitignore
└── README.md
```

## Como executar

**Pré-requisito:** Python 3 instalado. O projeto não usa bibliotecas externas, então não há nada para instalar.

```bash
# 1. Clone o repositório
git clone https://github.com/renan2026/Projeto-POO-AMV-Eventos.git

# 2. Entre na pasta
cd Projeto-POO-AMV-Eventos

# 3. Execute
python src/amv_eventos.py
```

> No Linux e no macOS, use `python3` no lugar de `python`.

## Exemplo de uso

```python
m1 = Motorista(1, "Carlos Silva", "123.456.789-00", "ABC12345")
v1 = Veiculo(1, "ABC-1234", "Kombi", 1200.0)

mat1 = MaterialCozinha(1, "Panela Industrial", "Inox", "Panela 50L")
item1 = ItemEntrega(101, 5, mat1)
item1.adicionar(10)

ev1 = Evento(1, "2026-10-15", "Cozinha Comunitária Centro", m1, v1)
ev1.adicionar_item(item1)
ev1.criar()
ev1.finalizar()
```

Saída:

```
Adicionados 10 itens. Total atual: 15
Evento 1 para Cozinha Comunitária Centro foi criado.
Status atual do evento: Criado
Evento 1 finalizado.
Status atual do evento: Finalizado
```

## Conceitos de POO aplicados

- **Classes e objetos:** cada entidade do problema é uma classe.
- **Associação:** `Evento` referencia `Motorista` e `Veiculo`; `ItemEntrega` referencia `MaterialCozinha`.
- **Agregação:** `Evento` mantém uma lista de `ItemEntrega`.
- **Encapsulamento de regras:** cada classe valida os próprios dados.
- **Tratamento de exceções:** entradas inválidas geram `ValueError`.
- **Controle de estado:** o `status` acompanha o ciclo de vida do evento.

## Tecnologias

| Tecnologia | Uso |
|---|---|
| Python 3 | Implementação do sistema |
| UML | Modelagem das classes |
| draw.io | Desenho do diagrama de classes |
| Git e GitHub | Versionamento e colaboração |

## Equipe

| Integrante | Responsabilidade |
|---|---|
| **João** | Desenvolvimento do código (revisado por toda a equipe) |
| **David** | Diagrama de classes (revisado por toda a equipe) |
| **Renan** | Relatório e documentação do repositório |

O repositório foi construído em conjunto pelos três integrantes.

## Documentação

- [Relatório do projeto (PDF)](docs/Relatorio_Projeto_POO_Amv_Eventos.pdf)
- [Diagrama de classes](docs/diagrama_de_classes.png)

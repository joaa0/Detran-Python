```md
# 🎮 Detran-Python

## 📌 Sobre o projeto
O **Detran-Python** é um jogo simples em Python, executado no terminal, desenvolvido para simular os passos lógicos de uma prova prática de autoescola.

O jogador deve seguir corretamente a sequência de ações exigidas durante a prova. A cada erro, perde pontos. O jogo termina quando os pontos chegam a **0**.

---

## 🎯 Objetivo
Criar um jogo funcional e didático, focado em:
- Lógica de programação
- Uso de estruturas básicas do Python
- Trabalho em equipe
- Organização de código simples

---

## 🕹️ Como funciona
- O jogador começa com uma quantidade de pontos (ex: 100)
- O jogo apresenta etapas da prova
- Para cada etapa, o jogador responde uma pergunta
- Se errar:
  - perde pontos
- Se acertar:
  - continua normalmente
- O jogo termina quando:
  - os pontos chegam a 0 (Game Over)
  - ou todas as etapas são concluídas

---

## 💻 Tecnologias utilizadas
- Python 3
- Execução via terminal (CLI)

---

## 📂 Estrutura básica do projeto

```

detran-python/
│
├── main.py              # Arquivo principal
├── etapas.py            # Etapas da prova
├── perguntas.py         # Perguntas e respostas
├── validacao.py         # Validação de respostas
├── pontuacao.py         # Sistema de pontos
├── feedback.py          # Mensagens do jogo
└── README.md

````

---

## 🚀 Como executar o projeto

### 1. Clonar ou baixar o projeto
```bash
git clone <url-do-repositorio>
cd detran-python
````

### 2. Executar o jogo

```bash
python main.py
```

---

## 🧩 Organização do desenvolvimento

O projeto foi dividido em **8 tarefas**, cada integrante do grupo é responsável por uma parte:

* Estrutura base do jogo
* Etapas da prova
* Sistema de perguntas
* Fluxo principal
* Validação de respostas
* Sistema de pontuação
* Feedback do jogo
* Integração final

---

## ⚠️ Regras de desenvolvimento

* Código simples (nível iniciante)
* Evitar complexidade desnecessária
* Funções pequenas e claras
* Testar sempre no terminal
* Manter organização do código

---

## ✅ Exemplo de execução

```
Você ajustou o banco?
> sim

✅ Correto!

Você colocou o cinto?
> não

❌ Errado! -10 pontos

Pontos: 90
```

---

## 👨‍💻 Equipe

Projeto desenvolvido por estudantes de TI (1º semestre), com foco em aprendizado prático de Python.

---

## 📌 Observações finais

Este projeto é apenas a primeira versão (Milestone 1), focada no funcionamento no terminal.

Possíveis evoluções futuras:

* Interface gráfica (pygame)
* Sons e animações
* Sistema mais complexo de pontuação
* Melhor experiência do usuário

```
```

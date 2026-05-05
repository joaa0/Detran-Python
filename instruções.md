# 🎮 Detran-Python — Distribuição de Tasks (Milestone 1)

## 📌 Objetivo
Criar um jogo **100% funcional no terminal**, simulando uma prova prática de autoescola.

O jogador começa com pontos e perde ao cometer erros nas ações. O jogo termina quando os pontos chegam a 0.

---

## ⚙️ Regras do Projeto

- Código **simples (nível iniciante)**
- Sem uso de conceitos avançados (classes, arquitetura complexa, etc.)
- Cada pessoa faz **uma parte isolada**
- Tudo será integrado em tempo real, com uso de git
- Linguagem: **Python puro (terminal)**

---

## 👥 Distribuição das Tasks

---

### 🧩 1. Estrutura base do jogo (PYT-5) -> CÉSAR
**Responsável:** Pessoa 1  

**Objetivo:** Criar o ponto inicial do jogo

**O que fazer:**
- Criar `main.py`
- Criar função `iniciar_jogo()`
- Criar loop principal (`while`)
- Exibir mensagem inicial

---

### 🧩 2. Etapas da prova (PYT-7) -> LEANDRO
**Responsável:** Pessoa 2  

**Objetivo:** Definir a sequência da prova

**O que fazer:**
- Criar lista ou dicionário com etapas

**Exemplo:**
```python
etapas = [
    "Ajustar banco",
    "Colocar cinto",
    "Dar partida",
    "Engatar marcha"
]
````

---

### 🧩 3. Sistema de perguntas (PYT-8) -> JOÃO

**Responsável:** Pessoa 3

**Objetivo:** Criar perguntas para cada etapa

**O que fazer:**

* Criar dicionário de perguntas
* Criar função que mostra pergunta e recebe input

**Exemplo:**

```python
perguntas = {
    "Ajustar banco": "O que você faz primeiro?"
}
```

---

### 🧩 4. Fluxo principal (PYT-9) -> MARCUS

**Responsável:** Pessoa 4

**Objetivo:** Controlar a ordem do jogo

**O que fazer:**

* Percorrer as etapas com loop
* Chamar as perguntas

---

### 🧩 5. Validação de respostas (PYT-10) ->

**Responsável:** Pessoa 5

**Objetivo:** Verificar acertos e erros

**O que fazer:**

* Criar função de validação

**Exemplo:**

```python
def validar(resposta_usuario, resposta_correta):
    return resposta_usuario.lower() == resposta_correta.lower()
```

---

### 🧩 6. Sistema de pontuação (PYT-6) ->

**Responsável:** Pessoa 6

**Objetivo:** Controlar os pontos do jogador

**O que fazer:**

* Criar variável `pontos = 100`
* Diminuir pontos ao errar
* Encerrar jogo quando pontos = 0

---

### 🧩 7. Feedback do jogo (PYT-11) ->

**Responsável:** Pessoa 7

**Objetivo:** Melhorar interação com o jogador

**O que fazer:**

* Mensagens de:

  * Acerto ✅
  * Erro ❌
  * Game Over
* Melhorar prints no terminal

---

### 🧩 8. Integração final (PYT-12) ->

**Responsável:** Pessoa 8

**Objetivo:** Juntar tudo

**O que fazer:**

* Integrar todas as partes
* Testar jogo completo
* Corrigir erros simples

---

## 🔗 Como o sistema se conecta

```
main.py
 ├── etapas
 ├── perguntas
 ├── fluxo
 │    ├── validação
 │    ├── pontuação
 │    └── feedback
 └── integração final
```

---

## ⚠️ Boas práticas obrigatórias

* Usar nomes simples e claros
* Evitar código complexo
* Criar funções pequenas
* Testar no terminal sempre
* Não mudar código dos outros sem avisar

---

## ✅ Resultado esperado

Exemplo de execução:

```
Você ajustou o banco?
> sim

✅ Correto!

Você colocou o cinto?
> não

❌ Errado! -10 pontos

Pontos: 90

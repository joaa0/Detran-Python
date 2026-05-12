# Detran-Python

Simulador simples de prova prática de autoescola feito em Python, para rodar no terminal. O projeto foi mantido propositalmente beginner-friendly, com lógica direta e sem dependências externas.

## Sobre o projeto

O usuário acessa um menu inicial, pode iniciar a prova, ler instruções, ver créditos ou sair. Durante a prova, cada etapa apresenta uma situação com alternativas, valida a resposta digitada e aplica a pontuação conforme o tipo de falta cometida.

Ao final, o sistema mostra:

- o resultado da prova;
- a pontuação final;
- o total de erros;
- o resumo das faltas cometidas.

## Funcionalidades atuais

- menu principal em loop com `while`;
- validação da opção digitada no menu;
- cadastro simples do condutor antes da prova;
- perguntas por etapa com opções numeradas;
- validação da resposta informada pelo usuário;
- pontuação diferente para cada tipo de falta;
- feedback visual mais claro para acerto, erro e resultado final;
- resumo final com os erros cometidos.

## Como executar

1. Abra um terminal na pasta do projeto.
2. Execute:

```bash
python main.py
```

Se o seu ambiente usar `python3`, execute:

```bash
python3 main.py
```

## Estrutura do projeto

O projeto está concentrado principalmente em um arquivo:

```text
main.py
```

Esse arquivo contém:

- o cadastro do condutor;
- as etapas da prova prática;
- a validação das respostas;
- o cálculo da pontuação;
- o feedback exibido ao usuário;
- o menu principal do sistema.

## Regras do jogo

- o usuário começa com 100 pontos;
- cada erro desconta pontos conforme a gravidade da falta;
- se a pontuação chegar a zero, a prova é encerrada;
- se concluir as etapas com pontos acima de zero, o usuário é aprovado.

## Tecnologias

- Python 3
- Interface de texto no terminal

## Observações

- O projeto foi pensado para estudo e prática de lógica.
- O código segue uma estrutura simples para facilitar leitura e manutenção.
- Não há banco de dados, interface gráfica ou dependências externas.

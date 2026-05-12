def validar_sistema():
    print("--- CADASTRO DE CONDUTOR ---")
    
    # Validação de Nome
    nome = input("Nome completo: ").strip()
    while len(nome) < 3:
        print("Nome muito curto!")
        nome = input("Nome completo: ").strip()

    # Validação de Idade (Número)
    while True:
        try:
            idade = int(input("Idade: "))
            if 18 <= idade <= 100:
                break
            print("Apenas condutores entre 18 e 100 anos.")
        except ValueError:
            print("Por favor, digite um número.")

    # Validação de Categoria (Lista)
    while True:
        cat = input("Categoria CNH [A/B/AB]: ").upper()
        if cat in ['A', 'B', 'AB']:
            break
        print("Categoria inválida!")

    print(f"\n✅ Cadastro realizado: {nome}, {idade} anos, Categoria {cat}")


def mostrar_titulo(texto):
    linha = "=" * 50
    print("\n" + linha)
    print(texto.center(50))
    print(linha)


def mostrar_bloco(texto):
    print(f"\n{text}")

print("=" * 70)

#DICIONARIO
# Lista com as etapas da prova prática
prova_pratica = [
    {
        "nome": "Ajustar banco e espelhos",
        "descricao": "Antes de ligar o carro, ajuste o banco e os espelhos.",
        "opcoes": ["Ajustar tudo corretamente", "Ignorar ajustes", "Ajustar só o banco"],
        "resposta_correta": "Ajustar tudo corretamente",
        "penalidade": "Falta leve"
    },
    {
        "nome": "Colocar cinto de segurança",
        "descricao": "Você deve colocar o cinto antes de iniciar.",
        "opcoes": ["Colocar o cinto", "Não colocar", "Colocar depois de sair"],
        "resposta_correta": "Colocar o cinto",
        "penalidade": "Falta grave"
    },
    {
        "nome": "Ligar o carro",
        "descricao": "Ligue o carro corretamente.",
        "opcoes": ["Dar partida com tudo certo", "Dar partida sem freio", "Errar a partida"],
        "resposta_correta": "Dar partida com tudo certo",
        "penalidade": "Falta média"
    },
    {
        "nome": "Sair com o veículo",
        "descricao": "Inicie o movimento do carro com segurança.",
        "opcoes": ["Sair devagar e sinalizar", "Sair rápido", "Não sinalizar"],
        "resposta_correta": "Sair devagar e sinalizar",
        "penalidade": "Falta média"
    },
    {
        "nome": "Parada obrigatória",
        "descricao": "Você encontra uma placa de pare.",
        "opcoes": ["Parar totalmente", "Reduzir sem parar", "Ignorar a placa"],
        "resposta_correta": "Parar totalmente",
        "penalidade": "Falta gravíssima"
    },
    {
        "nome": "Estacionar o veículo",
        "descricao": "Realize a baliza corretamente.",
        "opcoes": ["Estacionar correto", "Subir na calçada", "Bater no cone"],
        "resposta_correta": "Estacionar correto",
        "penalidade": "Eliminação"
    }
]

def fazer_pergunta(etapa):
    """
    Exibe a pergunta, captura o input e retorna a resposta do usuário.
    """
    mostrar_titulo(f"ETAPA: {etapa['nome']}")
    print(f"Situação: {etapa['descricao']}")
    print("Escolha uma das opções abaixo:")
    for i, opcao in enumerate(etapa['opcoes'], 1):
        print(f"[{i}] {opcao}")

    resposta = input("Sua resposta: ").strip()
    return resposta


def validar_resposta(resposta_usuario, etapa):
    """
    Verifica se a escolha do usuário bate com a resposta correta.
    """
    try:
        indice = int(resposta_usuario) - 1
        escolha = etapa['opcoes'][indice]
        return escolha == etapa['resposta_correta']
    except (ValueError, IndexError):
        return False


def obter_pontos_da_falta(tipo_falta):
    """
    Retorna a quantidade de pontos perdidos de acordo com o tipo da falta.
    """
    pontos_por_falta = {
        "Falta leve": 5,
        "Falta média": 10,
        "Falta grave": 15,
        "Falta gravíssima": 20,
        "Eliminação": 50
    }
    return pontos_por_falta.get(tipo_falta, 0)


def mostrar_feedback_correto(pontos_atual):
    print("\n┌──────────────────────────────────────────┐")
    print("│              RESPOSTA CERTA              │")
    print("├──────────────────────────────────────────┤")
    print("│ Você executou a etapa corretamente.      │")
    print(f"│ Pontuação atual: {pontos_atual:<22}│")
    print("└──────────────────────────────────────────┘")


def mostrar_feedback_erro(etapa, pontos_perdidos, pontos_restantes):
    print("\n┌──────────────────────────────────────────┐")
    print("│                ATENÇÃO                   │")
    print("├──────────────────────────────────────────┤")
    print(f"│ Falta cometida: {etapa['penalidade']:<20}│")
    print(f"│ Resposta certa: {etapa['resposta_correta'][:20]:<20}│")
    print(f"│ Perda de pontos: -{pontos_perdidos:<18}│")
    print(f"│ Pontuação atual: {pontos_restantes:<22}│")
    print("│ Dica: confira a ação correta e tente      │")
    print("│ manter a calma na próxima etapa.          │")
    print("└──────────────────────────────────────────┘")


def mostrar_resumo_final(pontos, erros):
    mostrar_titulo("RESUMO FINAL")
    print(f"Pontuação final: {max(pontos, 0)}")
    print(f"Total de erros: {len(erros)}")

    if erros:
        print("\nErros cometidos:")
        for erro in erros:
            print(f"- {erro['etapa']}: {erro['falta']} (-{erro['pontos_perdidos']} pontos)")
    else:
        print("\nVocê não cometeu erros.")


# Fluxo da prova

def iniciar_prova_fluxo(etapas):
    """
    Controla o loop principal da prova, passando por todas as etapas.
    """
    pontos = 100
    erros = []
    
    mostrar_titulo("INÍCIO DA PROVA PRÁTICA")
    print("Você verá uma situação por vez.")
    print("Responda com atenção ao número correto.\n")
    
    # Percorrer todas as etapas em sequência
    for etapa in etapas:
        # Condição de Game Over se os pontos zerarem
        if pontos <= 0:
            print("\n❌ GAME OVER! Você perdeu todos os seus pontos.")
            break
            
        print(f"\n[Pontuação atual: {pontos}]")
        
        # Executar a etapa usando a função de perguntas
        resposta = fazer_pergunta(etapa)
        
        # Validação e Feedback
        acertou = validar_resposta(resposta, etapa)
        
        if acertou:
            mostrar_feedback_correto(pontos)
        else:
            pontos_perdidos = obter_pontos_da_falta(etapa['penalidade'])
            pontos -= pontos_perdidos
            mostrar_feedback_erro(etapa, pontos_perdidos, max(pontos, 0))
            erros.append({
                "etapa": etapa["nome"],
                "falta": etapa["penalidade"],
                "pontos_perdidos": pontos_perdidos
            })
            
        input("\nPressione ENTER para seguir para a próxima etapa...")

    # Critério de conclusão: Mostrar aprovação ao concluir a prova
    mostrar_titulo("RESULTADO DA PROVA")
    if pontos > 0:
        print(f"🎉 APROVADO! Você terminou a prova com {pontos} pontos.")
    else:
        print("❌ REPROVADO. Você zerou a pontuação da prova.")

    mostrar_resumo_final(pontos, erros)

print("""

██████╗ ███████╗████████╗██████╗  █████╗ ███╗   ██╗
██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔══██╗████╗  ██║
██║  ██║█████╗     ██║   ██████╔╝███████║██╔██╗ ██║
██║  ██║██╔══╝     ██║   ██╔══██╗██╔══██║██║╚██╗██║
██████╔╝███████╗   ██║   ██║  ██║██║  ██║██║ ╚████║
╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝

""")

print("=" * 70)
print("      SIMULADOR DE PROVA PRÁTICA DE AUTOESCOLA")
print("=" * 70)
print("Treine situações comuns da prova e acompanhe seu desempenho.")

while True:
    mostrar_titulo("MENU PRINCIPAL")
    print("[1] Iniciar prova")
    print("[2] Instruções")
    print("[3] Créditos")
    print("[4] Sair")

    print("\n" + "-" * 70)

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        print("\nPreparando a prova...\n")
        validar_sistema()
        iniciar_prova_fluxo(prova_pratica)

    elif opcao == "2":
        mostrar_titulo("INSTRUÇÕES")
        print("1. Digite apenas o número da opção desejada.")
        print("2. Leia cada situação com calma.")
        print("3. Cada erro desconta pontos conforme a gravidade.")

    elif opcao == "3":
        mostrar_titulo("CRÉDITOS")
        print("Projeto simples criado em Python.")
        print("Foco em aprendizado e prática.")

    elif opcao == "4":
        print("\nSaindo do sistema...")
        break

    else:
        print("\n⚠️  Opção inválida. Digite apenas um número entre 1 e 4.")

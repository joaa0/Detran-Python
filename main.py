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

print("=" * 70)

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

# MENU
print("\n[1] INICIAR PROVA")
print("[2] INSTRUÇÕES")
print("[3] CRÉDITOS")
print("[4] SAIR")

print("\n" + "-" * 70)

# ESCOLHA
opcao = input("Escolha uma opção: ")

# OPÇÕES
if opcao == "1":

    print("\nIniciando prova...\n")
    validar_sistema()

elif opcao == "2":

    print("\nINSTRUÇÕES:")
    print("Digite o número da opção desejada.")
    print("Responda as perguntas corretamente.")

elif opcao == "3":

    print("\nCRÉDITOS:")
    print("Projeto simples criado em Python.")

elif opcao == "4":

    print("\nSaindo do sistema...")

else:

    print("\nOpção inválida!")

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

# Exemplo de uso
for etapa in prova_pratica:
    print(etapa["nome"])


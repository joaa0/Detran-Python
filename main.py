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




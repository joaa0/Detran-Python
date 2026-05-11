# ============================================
#      SIMULADOR DETRAN - TERMINAL PYTHON
# ============================================

# TÍTULO
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

    pergunta = input("Qual a cor do semáforo que indica PARE? ")

    if pergunta.lower() == "vermelho":
        print("\nResposta correta!")
    else:
        print("\nResposta incorreta!")

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

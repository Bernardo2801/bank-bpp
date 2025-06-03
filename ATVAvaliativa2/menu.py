from banco import Banco, criar_banco_e_tabelas
from operacoes import BancoOperacoes

def menu():
    nome_banco = 'simulador_banco_BPP'

    banco = Banco(database=None)
    criar_banco_e_tabelas(banco, nome_banco)
    banco.fechar_conexao()

    banco = Banco(database=nome_banco)
    operacoes = BancoOperacoes(banco)

# 📋 Menu interativo
    while True:
        banco.cursor.execute("SELECT COUNT(*) FROM cliente")
        clientes = banco.cursor.fetchone()[0]

        banco.cursor.execute("SELECT COUNT(*) FROM conta")
        contas = banco.cursor.fetchone()[0]

        print("\n--- MENU SIMULADOR DE BANCO ---")
        print("1 - Cadastrar Cliente")
        print("2 - Cadastrar Conta")

# 🧠 Verificação de pré-condições
        if clientes > 0 and contas > 0:
            print("3 - Depositar")
            print("4 - Sacar")
            print("5 - Ver Extrato")
        else:
            print("3 - Depositar (desabilitado - cadastre cliente e conta primeiro)")
            print("4 - Sacar (desabilitado - cadastre cliente e conta primeiro)")
            print("5 - Ver Extrato (desabilitado - cadastre cliente e conta primeiro)")
# Função: Evita operações inválidas antes de cadastrar clientes e contas.

        print("6 - Deletar Conta")
        print("7 - Deletar Cliente")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do cliente: ")
            cpf = input("CPF (somente números): ")
            operacoes.cadastrar_cliente(nome, cpf)

        elif opcao == '2':
            clientes_list = operacoes.listar_clientes()
            if not clientes_list:
                print("❌ Cadastre clientes antes de criar contas.")
                continue
            print("Clientes cadastrados:")
            for c in clientes_list:
                print(f"{c[0]} - {c[1]} (CPF: {c[2]})")

            id_cliente = int(input("Escolha o ID do cliente para a conta: "))
            tipo_conta = input("Tipo da conta (corrente/poupanca): ").lower()
            if tipo_conta == 'corrente':
                limite = float(input("Limite da conta corrente: "))
                operacoes.cadastrar_conta(id_cliente, tipo_conta, limite=limite)
            elif tipo_conta == 'poupanca':
                dia_rendimento = int(input("Dia do rendimento (1-28): "))
                operacoes.cadastrar_conta(id_cliente, tipo_conta, dia_rendimento=dia_rendimento)
            else:
                print("Tipo de conta inválido.")

        elif opcao == '3' and clientes > 0 and contas > 0:
            contas_list = operacoes.listar_contas()
            print("Contas cadastradas:")
            for c in contas_list:
                print(f"{c[0]} - Cliente: {c[1]}, Tipo: {c[2]}, Saldo: R${c[3]:.2f}")
            id_conta = int(input("Escolha o ID da conta para depósito: "))
            valor = float(input("Valor para depósito: "))
            operacoes.depositar(id_conta, valor)

        elif opcao == '4' and clientes > 0 and contas > 0:
            contas_list = operacoes.listar_contas()
            print("Contas cadastradas:")
            for c in contas_list:
                print(f"{c[0]} - Cliente: {c[1]}, Tipo: {c[2]}, Saldo: R${c[3]:.2f}")
            id_conta = int(input("Escolha o ID da conta para saque: "))
            valor = float(input("Valor para saque: "))
            operacoes.sacar(id_conta, valor)

        elif opcao == '5' and clientes > 0 and contas > 0:
            contas_list = operacoes.listar_contas()
            print("Contas cadastradas:")
            for c in contas_list:
                print(f"{c[0]} - Cliente: {c[1]}, Tipo: {c[2]}, Saldo: R${c[3]:.2f}")
            id_conta = int(input("Escolha o ID da conta para ver extrato: "))
            operacoes.ver_extrato(id_conta)

        elif opcao == '6':
            contas_list = operacoes.listar_contas()
            if not contas_list:
                print("❌ Nenhuma conta para deletar.")
                continue
            print("Contas cadastradas:")
            for c in contas_list:
                print(f"{c[0]} - Cliente: {c[1]}, Tipo: {c[2]}, Saldo: R${c[3]:.2f}")
            id_conta = int(input("Escolha o ID da conta para deletar: "))
            operacoes.deletar_conta(id_conta)

        elif opcao == '7':
            clientes_list = operacoes.listar_clientes()
            if not clientes_list:
                print("❌ Nenhum cliente para deletar.")
                continue
            print("Clientes cadastrados:")
            for c in clientes_list:
                print(f"{c[0]} - Nome: {c[1]}, CPF: {c[2]}")
            id_cliente = int(input("Escolha o ID do cliente para deletar: "))
            operacoes.deletar_cliente(id_cliente)

        elif opcao == '0':
            print("Saindo...")
            banco.fechar_conexao()
            break

        else:
            print("Opção inválida ou desabilitada.")

#Função: Interface de linha de comando para interagir com o sistema. Permite cadastrar, consultar e deletar dados.

if __name__ == "__main__":
    menu()

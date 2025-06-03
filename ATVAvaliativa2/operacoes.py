import decimal
from mysql.connector import Error

class BancoOperacoes:
    def __init__(self, banco):
        self.banco = banco
        self.cursor = banco.cursor
        self.conexao = banco.conexao

# 👤 Cadastro de cliente C(reate)RUD
    def cadastrar_cliente(self, nome, cpf):
        try:
            self.cursor.execute("INSERT INTO cliente (nome, cpf) VALUES (%s, %s)", (nome, cpf))
            self.conexao.commit()
            print(f"✅ Cliente '{nome}' cadastrado com sucesso.")
        except Error as e:
            print(f"❌ Erro ao cadastrar cliente: {e}")
#Função: Insere um novo cliente no banco de dados.

    def listar_clientes(self):
        self.cursor.execute("SELECT * FROM cliente")
        return self.cursor.fetchall()

# 💳 Cadastro de conta C(reate)RUD
    def cadastrar_conta(self, id_cliente, tipo_conta, limite=None, dia_rendimento=None):
        try:
            self.cursor.execute("""
                INSERT INTO conta (id_cliente, tipo_conta, limite, dia_rendimento)
                VALUES (%s, %s, %s, %s)
            """, (id_cliente, tipo_conta, limite, dia_rendimento))
            self.conexao.commit()
            print(f"✅ Conta '{tipo_conta}' cadastrada com sucesso para o cliente ID {id_cliente}.")
        except Error as e:
            print(f"❌ Erro ao cadastrar conta: {e}")
#Função: Cria uma conta corrente ou poupança associada a um cliente.

    def listar_contas(self):
        self.cursor.execute("""
            SELECT conta.id_conta, cliente.nome, conta.tipo_conta, conta.saldo 
            FROM conta 
            JOIN cliente ON conta.id_cliente = cliente.id_cliente
        """)
        return self.cursor.fetchall()

# ➕ Depósito CRU(pdate)D
    def depositar(self, id_conta, valor):
        try:
            self.cursor.execute("SELECT saldo FROM conta WHERE id_conta = %s", (id_conta,))
            saldo_atual = self.cursor.fetchone()
            if saldo_atual is None:
                print("Conta não encontrada.")
                return

            saldo_atual_decimal = saldo_atual[0]
            valor_decimal = decimal.Decimal(str(valor))

            novo_saldo = saldo_atual_decimal + valor_decimal
            self.cursor.execute("UPDATE conta SET saldo = %s WHERE id_conta = %s", (novo_saldo, id_conta))
            self.cursor.execute(
                "INSERT INTO transacao (id_conta, tipo, valor) VALUES (%s, %s, %s)",
                (id_conta, 'deposito', valor_decimal)
            )
            self.conexao.commit()
            print(f"✅ Depósito de R${valor_decimal:.2f} realizado com sucesso.")
        except Error as e:
            print(f"❌ Erro ao realizar depósito: {e}")
# Atualiza o saldo da conta e registra a transação.

# ➖ Saque com verificação de saldo e limite CRU(pdate)D
    def sacar(self, id_conta, valor):
        try:
            self.cursor.execute("SELECT saldo, limite FROM conta WHERE id_conta = %s", (id_conta,))
            dados = self.cursor.fetchone()
            if dados is None:
                print("Conta não encontrada.")
                return

            saldo_atual, limite = dados
            saldo_atual_decimal = saldo_atual
            limite_decimal = limite if limite is not None else decimal.Decimal('0.00')
            valor_decimal = decimal.Decimal(str(valor))

            if saldo_atual_decimal + limite_decimal < valor_decimal:
                print(f"❌ Saldo insuficiente. Saldo disponível: R${(saldo_atual_decimal + limite_decimal):.2f}")
                return

            novo_saldo = saldo_atual_decimal - valor_decimal
            self.cursor.execute("UPDATE conta SET saldo = %s WHERE id_conta = %s", (novo_saldo, id_conta))
            self.cursor.execute(
                "INSERT INTO transacao (id_conta, tipo, valor) VALUES (%s, %s, %s)",
                (id_conta, 'saque', valor_decimal)
            )
            self.conexao.commit()
            print(f"✅ Saque de R${valor_decimal:.2f} realizado com sucesso.")
        except Error as e:
            print(f"❌ Erro ao realizar saque: {e}")
#Função: Permite saque apenas se o valor não exceder o saldo + limite.

# 📄 Ver extrato CR(ead)UD
    def ver_extrato(self, id_conta):
        try:
            self.cursor.execute("SELECT * FROM conta WHERE id_conta = %s", (id_conta,))
            conta = self.cursor.fetchone()
            if conta is None:
                print("Conta não encontrada.")
                return

            self.cursor.execute("""
                SELECT tipo, valor, data FROM transacao 
                WHERE id_conta = %s ORDER BY data DESC
            """, (id_conta,))
            transacoes = self.cursor.fetchall()

            print(f"\n--- Extrato da Conta {id_conta} ---")
            for t in transacoes:
                print(f"{t[2]} - {t[0]}: R${t[1]:.2f}")
        except Error as e:
            print(f"❌ Erro ao visualizar extrato: {e}")
# Função: Mostra o histórico de transações da conta.

# ❌ Exclusão de conta e cliente CRUD(elete)
    def deletar_conta(self, id_conta):
        try:
            # Deletar transações associadas
            self.cursor.execute("DELETE FROM transacao WHERE id_conta = %s", (id_conta,))
            # Deletar a conta
            self.cursor.execute("DELETE FROM conta WHERE id_conta = %s", (id_conta,))
            self.conexao.commit()
            print(f"✅ Conta ID {id_conta} deletada com sucesso.")
        except Error as e:
            print(f"❌ Erro ao deletar conta: {e}")

    def deletar_cliente(self, id_cliente):
        try:
            # Deletar transações associadas às contas do cliente
            self.cursor.execute("SELECT id_conta FROM conta WHERE id_cliente = %s", (id_cliente,))
            contas = self.cursor.fetchall()
            for conta in contas:
                id_conta = conta[0]
                self.cursor.execute("DELETE FROM transacao WHERE id_conta = %s", (id_conta,))

            # Deletar contas associadas
            self.cursor.execute("DELETE FROM conta WHERE id_cliente = %s", (id_cliente,))
            # Deletar cliente
            self.cursor.execute("DELETE FROM cliente WHERE id_cliente = %s", (id_cliente,))
            self.conexao.commit()
            print(f"✅ Cliente ID {id_cliente} e todas as suas contas/transações foram deletados com sucesso.")
        except Error as e:
            print(f"❌ Erro ao deletar cliente: {e}")
#Função: Remove uma conta e suas transações, ou um cliente com todas suas contas.

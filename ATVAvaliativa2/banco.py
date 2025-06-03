import mysql.connector
from mysql.connector import Error

class Banco:
    def __init__(self, host='localhost', user='root', password='mysql', database=None):
        try:
            self.conexao = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            self.cursor = self.conexao.cursor()
            if database:
                print(f"✅ Conectado ao banco de dados '{database}'.")
            else:
                print("✅ Conectado ao servidor MySQL (sem banco específico).")
        except Error as e:
            print(f"❌ Erro ao conectar ao banco de dados: {e}")

    def fechar_conexao(self):
        if self.conexao.is_connected():
            self.cursor.close()
            self.conexao.close()
            print("✅ Conexão com o banco de dados fechada.")

def criar_banco_e_tabelas(banco, nome_banco):
    try:
        banco.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {nome_banco}")
        print(f"✅ Banco '{nome_banco}' criado ou já existente.")

        banco.conexao.commit()
        banco.cursor.execute(f"USE {nome_banco}")

        banco.cursor.execute("""
            CREATE TABLE IF NOT EXISTS cliente (
                id_cliente INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                cpf VARCHAR(11) NOT NULL UNIQUE
            )
        """)

        banco.cursor.execute("""
            CREATE TABLE IF NOT EXISTS conta (
                id_conta INT AUTO_INCREMENT PRIMARY KEY,
                id_cliente INT NOT NULL,
                tipo_conta ENUM('corrente', 'poupanca') NOT NULL,
                saldo DECIMAL(10,2) DEFAULT 0.0,
                limite DECIMAL(10,2),
                dia_rendimento INT,
                FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente)
            )
        """)

        banco.cursor.execute("""
            CREATE TABLE IF NOT EXISTS transacao (
                id_transacao INT AUTO_INCREMENT PRIMARY KEY,
                id_conta INT NOT NULL,
                tipo ENUM('deposito', 'saque', 'transferencia') NOT NULL,
                valor DECIMAL(10,2) NOT NULL,
                data DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (id_conta) REFERENCES conta(id_conta)
            )
        """)

        banco.conexao.commit()
        print("✅ Tabelas criadas ou já existentes.")
    except Error as e:
        print(f"❌ Erro ao criar banco/tabelas: {e}")

if __name__ == "__main__":
    nome_banco = 'simulador_banco_BPP'

    banco = Banco()
    criar_banco_e_tabelas(banco, nome_banco)
    banco.fechar_conexao()

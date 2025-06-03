# bank-bpp

<h1>Simulador de Banco - CRUD com POO e Banco de Dados</h1>

<p>
    Este projeto é um simulador de operações bancárias desenvolvido em Python, utilizando programação orientada a objetos (POO), conceitos de herança e integração com banco de dados MySQL. O objetivo deste sistema é praticar e demonstrar os conceitos de CRUD (Create, Read, Update, Delete) e banco de dados relacionais.
</p>

<h2>🚀 Funcionalidades</h2>
<ul>
    <li>Cadastrar clientes e contas bancárias.</li>
    <li>Realizar depósitos e saques.</li>
    <li>Visualizar extratos de movimentações financeiras.</li>
    <li>Listar clientes e contas com todas as informações.</li>
    <li>Deletar contas e clientes, com remoção em cascata das transações.</li>
</ul>

<h2>🛠️ Tecnologias Utilizadas</h2>
<ul>
    <li><strong>Python</strong>: Linguagem principal do sistema.</li>
    <li><strong>MySQL</strong>: Banco de dados relacional para armazenamento das informações.</li>
    <li><strong>mysql-connector-python</strong>: Biblioteca para conexão Python-MySQL.</li>
    <li><strong>Programação Orientada a Objetos (POO)</strong>: Estrutura do sistema baseada em classes e métodos.</li>
</ul>

<h2>📚 Conceitos Aplicados</h2>

<h3>✅ CRUD - Exemplos</h3>
<ul>
    <li><strong>Create</strong>: Inserção de novos clientes e contas - função <code>cadastrar_cliente()</code> e <code>cadastrar_conta()</code> no arquivo <code>operacoes.py</code>.</li>
    <li><strong>Read</strong>: Listagem de clientes e contas - função <code>listar_clientes()</code> e <code>listar_contas()</code>.</li>
    <li><strong>Update</strong>: Atualização do saldo em operações de depósito e saque - funções <code>depositar()</code> e <code>saque()</code>.</li>
    <li><strong>Delete</strong>: Remoção de contas e clientes - funções <code>deletar_conta()</code> e <code>deletar_cliente()</code>.</li>
</ul>

<h3>✅ Programação Orientada a Objetos (POO)</h3>
<ul>
    <li>O sistema é dividido em classes: <code>Banco</code> (arquivo <code>banco.py</code>) para conexão e criação do banco, e <code>BancoOperacoes</code> (arquivo <code>operacoes.py</code>) para operações bancárias.</li>
</ul>

<h3>✅ Herança - Exemplos</h3>
<ul>
    <li>Embora o projeto não utilize herança explícita entre classes, utiliza herança de conceitos de composição: a classe <code>BancoOperacoes</code> recebe a instância de <code>Banco</code> para realizar operações, representando a relação entre objetos.</li>
    <li>Utilização de parâmetros padrão e métodos compartilhados em <code>banco.py</code> e <code>operacoes.py</code> facilita a reutilização e extensão futura, aplicando princípios de herança e encapsulamento.</li>
</ul>

<h3>✅ Banco de Dados</h3>
<ul>
    <li>Criação do banco de dados e tabelas através da função <code>criar_banco_e_tabelas()</code> em <code>banco.py</code>.</li>
    <li>Execução de comandos SQL para criação das tabelas <code>cliente</code>, <code>conta</code> e <code>transacao</code>.</li>
    <li>Exemplo:
        <pre><code>
CREATE TABLE IF NOT EXISTS cliente (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(11) NOT NULL UNIQUE
)
        </code></pre>
    </li>
</ul>

<h3>✅ Módulos e Funções Claras</h3>
<ul>
    <li>Separação das responsabilidades: <code>banco.py</code> cuida da estrutura do banco, <code>operacoes.py</code> gerencia as operações financeiras e <code>menu.py</code> implementa a interface com o usuário.</li>
    <li>Exemplo de função clara:
        <pre><code>
def deletar_conta(self, id_conta):
    self.cursor.execute("DELETE FROM transacao WHERE id_conta = %s", (id_conta,))
    self.cursor.execute("DELETE FROM conta WHERE id_conta = %s", (id_conta,))
    self.conexao.commit()
</code></pre>
    </li>
</ul>

<h3>✅ Funcionamento correto e intuitivo do menu</h3>
<ul>
    <li>Menu dinâmico que exibe ou desativa opções dependendo do contexto (por exemplo, só permite saque se houver clientes e contas).</li>
    <li>Exemplo:
        <pre><code>
if clientes > 0 and contas > 0:
    print("3 - Depositar")
    print("4 - Sacar")
else:
    print("3 - Depositar (desabilitado - cadastre cliente e conta primeiro)")
</code></pre>
    </li>
</ul>

<h2>👥 Integrantes</h2>
<ul>
    <li>Bernardo Araújo Alves</li>
    <li>Pedro Henrique Alves da Silva</li>
    <li>Pedro Luca Fernandes</li>
</ul>

<h2>📦 Como rodar o projeto</h2>
<ol>
    <li>Instale o MySQL e crie um usuário com permissão para criar bancos de dados.</li>
    <li>Clone o repositório:</li>
</ol>
<br><br><br>


## 🏦 Simulador de Banco — Trechos Importantes do Código

## 📁 banco.py
#### 🔌Conexão com o banco de dados

```
class Banco:
    def __init__(self, host='localhost', user='root', password='mysql', database=None):
        self.conexao = mysql.connector.connect(
            host=host, user=user, password=password, database=database
        )
        self.cursor = self.conexao.cursor()
```
#### Função: Este trecho é responsável por inicializar a conexão com o MySQL, permitindo que o sistema se comunique com o banco de dados.


#### 🛠️ Criação do banco e tabelas

```
def criar_banco_e_tabelas(banco, nome_banco):
    banco.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {nome_banco}")
    banco.cursor.execute(f"USE {nome_banco}")
    banco.cursor.execute("CREATE TABLE IF NOT EXISTS cliente (...)")
    banco.cursor.execute("CREATE TABLE IF NOT EXISTS conta (...)")
    banco.cursor.execute("CREATE TABLE IF NOT EXISTS transacao (...)")
```
#### Função:
Cria o banco de dados e as três tabelas principais: `cliente`, `conta` e `transacao`.

## 📁 menu.py
#### 📋 Menu interativo

```
def menu():
    while True:
        print("--- MENU SIMULADOR DE BANCO ---")
        print("1 - Cadastrar Cliente")
        print("2 - Cadastrar Conta")
        ...
        opcao = input("Escolha uma opção: ")
        ...
```
#### Função:
Interface de linha de comando para interagir com o sistema. Permite `cadastrar`, `consultar` e `deletar` dados.

#### 🧠 Verificação de pré-condições

```
if clientes > 0 and contas > 0:
    print("3 - Depositar")
    print("4 - Sacar")
    print("5 - Ver Extrato")
else:
    print("3 - Depositar (desabilitado...)")
```
#### Função:
Evita operações inválidas antes de cadastrar clientes e contas.

## 📁 operacoes.py
#### 👤 Cadastro de cliente C(reate)RUD
```
def menu():
def cadastrar_cliente(self, nome, cpf):
    self.cursor.execute("INSERT INTO cliente (nome, cpf) VALUES (%s, %s)", (nome, cpf))
```
#### Função:
Insere um novo cliente no banco de dados.

#### 💳 Cadastro de conta C(reate)RUD
```
def cadastrar_conta(self, id_cliente, tipo_conta, limite=None, dia_rendimento=None):
    self.cursor.execute("""
        INSERT INTO conta (id_cliente, tipo_conta, limite, dia_rendimento)
        VALUES (%s, %s, %s, %s)
    """, (id_cliente, tipo_conta, limite, dia_rendimento))
```
#### Função:
Cria uma conta corrente ou poupança associada a um cliente.

#### ➕ Depósito CRU(pdate)D
```
def depositar(self, id_conta, valor):
    self.cursor.execute("UPDATE conta SET saldo = %s WHERE id_conta = %s", (novo_saldo, id_conta))
    self.cursor.execute("INSERT INTO transacao (id_conta, tipo, valor) VALUES (%s, 'deposito', %s)", ...)

```
#### Função:
Atualiza o saldo da conta e registra a transação.

#### ➖ Saque com verificação de saldo e limite CRU(pdate)D
```
def sacar(self, id_conta, valor):
    if saldo_atual_decimal + limite_decimal < valor_decimal:
        print("❌ Saldo insuficiente.")
```
#### Função:
Permite saque apenas se o valor não exceder o saldo + limite.

#### 📄 Ver extrato CR(ead)UD
```
def ver_extrato(self, id_conta):
    self.cursor.execute("SELECT tipo, valor, data FROM transacao WHERE id_conta = %s ORDER BY data DESC")
```
#### Função:
Mostra o histórico de transações da conta.

#### ❌ Exclusão de conta e cliente CRUD(elete)
```
def deletar_conta(self, id_conta):
    self.cursor.execute("DELETE FROM transacao WHERE id_conta = %s")
    self.cursor.execute("DELETE FROM conta WHERE id_conta = %s")
```
```
def deletar_cliente(self, id_cliente):
    self.cursor.execute("DELETE FROM cliente WHERE id_cliente = %s")

```
#### Função:
Remove uma conta e suas transações, ou um cliente com todas suas contas.
    <pre><code>git clone https://github.com/SEU_USUARIO/simulador-banco.git</code></pre>
    <li>Instale o conector MySQL:</li>
    <pre><code>pip install mysql-connector-python</code></pre>
    <li>Execute o menu principal:</li>
    <pre><code>python menu.py</code></pre>
</ol>

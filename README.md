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
    <pre><code>git clone https://github.com/SEU_USUARIO/simulador-banco.git</code></pre>
    <li>Instale o conector MySQL:</li>
    <pre><code>pip install mysql-connector-python</code></pre>
    <li>Execute o menu principal:</li>
    <pre><code>python menu.py</code></pre>
</ol>

import requests, json
from flask import Flask, render_template, url_for, redirect, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'xastreedb'
mysql = MySQL(app)

URL_API = "https://reqres.in/api/users?page=1"

# -------------------- ROTAS --------------------
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/listarClientes')
def listarClientes():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM clientes")
    lista_clientes = cur.fetchall()
    cur.execute("SELECT * FROM investimentos")
    lista_investimentos = cur.fetchall()
    cur.close()

    return render_template('lista-clientes.html', clientes=lista_clientes, investimentos=lista_investimentos)

# -------------------- CONTROLE --------------------
@app.route('/controleClientes')
def controleClientes():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM clientes")
    lista_clientes = cur.fetchall()
    cur.execute("SELECT * FROM investimentos")
    lista_investimentos = cur.fetchall()
    cur.close()

    return render_template('controle-clientes.html', clientes=lista_clientes, investimentos=lista_investimentos)

@app.route('/controleInvestimentos')
def controleInvestimentos():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM investimentos")
    lista_investimentos = cur.fetchall()
    cur.close()

    return render_template('controle-investimentos.html', investimentos=lista_investimentos)

# -------------------- CREATE --------------------
@app.route('/createCliente',methods=["POST"])
def createCliente():
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    email = request.form['email']
    id_investimento = request.form['investimento']

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO clientes (nome, sobrenome, email, id_investimento) VALUES (%s, %s, %s, %s)", (nome, sobrenome, email, id_investimento,))
    mysql.connection.commit()

    return redirect(request.referrer)

@app.route('/createInvestimento',methods=["POST"])
def createInvestimento():
    investimento = request.form['investimento']

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO investimentos (investimento) VALUES (%s)", (investimento,))
    mysql.connection.commit()

    return redirect(request.referrer)

# -------------------- UPDATE --------------------
@app.route('/updateCliente', methods=["POST"])
def updateCliente():
    id_cliente = request.form['id_cliente']
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    email = request.form['email']
    id_investimento = request.form['investimento']

    cur = mysql.connection.cursor()
    cur.execute("UPDATE clientes SET nome=%s, sobrenome=%s, email=%s, id_investimento=%s WHERE id=%s", (nome, sobrenome, email, id_investimento ,id_cliente,))
    mysql.connection.commit()

    return redirect(request.referrer)

@app.route('/updateInvestimento', methods=["POST"])
def updateInvestimento():
    id_investimento = request.form['id_investimento']
    investimento = request.form['investimento']

    cur = mysql.connection.cursor()
    cur.execute("UPDATE investimentos SET investimento=%s WHERE id=%s", (investimento, id_investimento,))
    mysql.connection.commit()

    return redirect(request.referrer)

# -------------------- DELETE --------------------
@app.route('/delete/<string:tabela>/<string:id_dado>', methods=["GET"])
def delete(tabela, id_dado):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM %s WHERE id=%s" % (tabela, id_dado,))
    mysql.connection.commit()

    return redirect(request.referrer)

# -------------------- SEARCH --------------------
@app.route('/pesquisar', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        email = request.form['email']

        cur = mysql.connection.cursor()
        # Procura o cliente pelo email informado
        cur.execute("SELECT * from clientes WHERE email=%s", (email,))
        mysql.connection.commit()
        dados_cliente = cur.fetchall()

        # Envia a lista com todos os investimentos (Poderia ser otimizado)
        cur.execute("SELECT * FROM investimentos")
        lista_investimentos = cur.fetchall()
        cur.close()

        return render_template('pesquisa.html', cliente=dados_cliente, investimentos=lista_investimentos)

    return render_template('pesquisa.html')

# ---------- Rotas de Manipulação da API e Banco de Dados ----------
@app.route('/inserirAPI')
def insertAPI_DB():
    # Envia uma requisição do tipo GET e salva o retorno na variável "res" (response)
    res = requests.get(url = URL_API) 
    # Converte os dados em formato JSON 
    dado = res.json()
    cur = mysql.connection.cursor()

    for cadastro in dado['data']:
        # Coloca 1 no campo id_investimento pois assim se relaciona com o investimento "Nenhum"
        cur.execute("INSERT INTO clientes (nome, sobrenome, email, id_investimento) VALUES (%s, %s, %s, %s)",(cadastro['first_name'], cadastro['last_name'], cadastro['email'], 1,))
        mysql.connection.commit()
    
    return redirect(url_for('home'))

@app.route('/resetDB')
def resetDB():
    cur = mysql.connection.cursor()
    # Esse loop faz executar linha a linha os comandos que estão no arquivo "db_reset_tables.sql"
    # *** IMPORTANTE: Colocar um comando por linha e não pular linha de um para o outro ***
    for linha in open('db_reset_tables.sql').read().split(';\n'):
        cur.execute(linha)
    mysql.connection.commit()

    return redirect(url_for('home'))

# -------------------- APP Run --------------------
if __name__ == '__main__':
    app.run(debug=True)
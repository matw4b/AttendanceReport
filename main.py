import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/adicionar')
def novo_aluno():
    return render_template('aluno.html')


@app.route('/registro', methods = ['POST', 'GET'])
def registro():
    if request.method == 'POST':
        try:
            name = request.form['name']
            mat = request.form['mat']

            with sqlite3.connect("alunos.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO students (nome, matricula) VALUES (?,?)", (name,mat))
                con.commit()
                msg = "Registro feito com sucesso"

        except:
            con.rollback()
            msg = "Erro na inserção"

        finally:
            con.close()
            return render_template("result.html", msg = msg)


@app.route('/chamada')
def chamada():
    con = sqlite3.connect("alunos.db")
    con.row_factory =sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from alunos")
    rows = cur.fetchall();
    return render_template("chamada.html", rows = rows)


@app.route('/')
def home():
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True)

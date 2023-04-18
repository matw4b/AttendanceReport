import sqlite3

#criando o banco dos alunos
conn = sqlite3.connect('alunos.db')
print("Banco criado com sucesso");

conn.execute('CREATE TABLE alunos (nome TEXT, matricula TEXT)')
print("Tabela criada com sucesso");
conn.close()
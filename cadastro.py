import sqlite3

conn = sqlite3.connect('biblioteca.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuario (
            id INTEGER PRIMARY KEY AUTOINCREMENT ,
            nome TEXT NO TLL,
            cpf TEXT NOT NULL UNIQUE    
)
''')
conn.commit()

print('      _Sistema bibliotecario_       ')

def cadastro_usuario():
    nome = input('nome: ').strip()
    cpf = input('cpf: ').strip()

    if not 'cpf' or not 'name':
        raise ValueError('você não pode continuar! nome e cpf são obrigatorio.')
    
    try:
        cursor.execute('INSERT INTO usuario (nome, cpf) VALUES (?, ?)', (nome, cpf))
        conn.commit()
        print(f'Usuario {nome} com CPF {cpf} cadastrado com sucesso!')
    except sqlite3.IntegrityError:
        print('Erro: Este Cpf já está cadastrado.')


cadastro_usuario()

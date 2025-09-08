import sqlite3
import tkinter as tk
from tkinter import messagebox

#Criando Banco de Dados
conn = sqlite3.connect('biblioteca.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NO NULL,
            livro TEXT NO NULL,
            cpf TEXT NOT NULL UNIQUE
)
''')

conn.commit()

#Funcao Cadastro
def cadastro_usuario():
    nome = entry_nome.get().strip()
    cpf = entry_cpf.get().strip()
    livro = entry_livro.get().strip()

    if not nome or not cpf:
        messagebox.showerror('Erro', 'Nome e CPF são obrigatórios.')
        return

    try:
        cursor.execute('INSERT INTO usuario (nome, cpf, livro) VALUES (?, ?, ?)', (nome, cpf, livro))
        conn.commit()
        messagebox.showinfo('Sucesso', f'Usuário {nome} com CPF {cpf} cadastrado com sucesso!')
        entry_nome.delete(0, tk.END)
        entry_cpf.delete(0, tk.END)
        entry_livro.delete(0, tk.END)
    except sqlite3.IntegrityError:
        messagebox.showerror('Erro', 'Este CPF já está cadastrado.')

# Interface gráfica
root = tk.Tk()
root.title('Cadastro de Usuário - Sistema Bibliotecário')
root.geometry('400x250')

label_titulo = tk.Label(root, text='Cadastro de Usuário', font=('Arial', 16, 'bold'))
label_titulo.pack(pady=10)

# Campo Nome
label_nome = tk.Label(root, text='Nome:')
label_nome.pack()
entry_nome = tk.Entry(root, width=40)
entry_nome.pack()

# Campo CPF
label_cpf = tk.Label(root, text='CPF:')
label_cpf.pack()
entry_cpf = tk.Entry(root, width=40)
entry_cpf.pack()

# nome do livro
label_livro = tk.Label(root, text='Livro: ')
label_livro.pack()
entry_livro = tk.Entry(root, width=40)
entry_livro.pack()

# Botão de Cadastro
btn_cadastrar = tk.Button(root, text='Cadastrar', command=cadastro_usuario)
btn_cadastrar.pack(pady=10)

# Inicia a interface
root.mainloop()

# Fecha conexão com banco (opcional, após a janela fechar)
conn.close()

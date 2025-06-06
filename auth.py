import tkinter as tk
from tkinter import messagebox
from banco import criar_tabela
from banco import registrar_usuario, autenticar_usuario
from cadastro import abrir_cadastro

criar_tabela()

janela = tk.Tk()
janela.title("Login de usuário")

email_log = tk.StringVar()
senha_log = tk.StringVar()
nome_cad = tk.StringVar()
email_cad = tk.StringVar()
senha_cad = tk.StringVar()

def fazer_login():
    resultado = autenticar_usuario(email_log.get(), senha_log.get())
    if resultado:
        messagebox.showinfo("Login", f"Bem vindo(a), {resultado[1]}")
        janela.destroy()
    else:
        messagebox.showerror("Erro", "E-mail ou senha incorretos.")


# Área da interface do login 

tk.Label(janela, text="E-mail:").grid(row=0, column=0)
tk.Entry(janela, textvariable=email_log).grid(row=0, column=1)

tk.Label(janela, text="Senha:").grid(row=1, column=0)
tk.Entry(janela, textvariable=senha_log, show="*").grid(row=1, column=1)

tk.Button(janela, text="Criar conta", command=lambda: abrir_cadastro(janela)).grid(row=2,column=1)

tk.Button(janela, text="Entrar", command=fazer_login).grid(row=2, column=0)

janela.mainloop()
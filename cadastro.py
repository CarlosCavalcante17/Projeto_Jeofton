import tkinter as tk
from tkinter import messagebox
from banco import registrar_usuario

def abrir_cadastro(janela_pai):
 cadastro = tk.Toplevel(janela_pai)
 cadastro.title("Criar Conta")

 nome_reg = tk.StringVar()
 email_reg = tk.StringVar()
 senha_reg = tk.StringVar()

 tk.Label(cadastro, text="Nome completo:").grid(row=0, column=0)
 tk.Entry(cadastro, textvariable=nome_reg).grid(row=0, column=1)

 tk.Label(cadastro, text="E-mail:").grid(row=1, column=0)
 tk.Entry(cadastro, textvariable=email_reg).grid(row=1, column=1)

 tk.Label(cadastro, text="Senha:").grid(row=2, column=0)
 tk.Entry(cadastro, textvariable=senha_reg, show="*").grid(row=2, column=1)

 def registrar():
    nome = nome_reg.get()
    email = email_reg.get()
    senha = senha_reg.get()
    if not nome or not email or not senha:
        messagebox.showerror("Erro", "Preencha nome, e-mail e senha para criar a conta")
        return
    sucesso = registrar_usuario(nome, email, senha)
    if sucesso == True:
        messagebox.showinfo("Sucesso", "Conta criada com sucesso!!!")
        cadastro.destroy()
    elif sucesso == "email":
       messagebox.showerror("Erro", "E-mail já cadastrado!!!!")
    elif sucesso != "senha":
       messagebox.showerror("Erro","A senha já está sendo utilizada por outro usuário!!!!") 
    else:
        messagebox.showerror("Erro", "Erro ao criar conta.")    

 tk.Button(cadastro, text="registrar", command=registrar).grid(row=3, column=0, columnspan=2)
    
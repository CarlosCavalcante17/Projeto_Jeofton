import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from banco import registrar_usuario

ctk.set_appearance_mode("Dark")

# Função para abrir a janela de cadastro
def abrir_cadastro(janela_pai):
 cadastro = ctk.CTkToplevel(janela_pai)
 cadastro.title("Criar Conta")
 cadastro.geometry("400x400")

 nome_reg = tk.StringVar()
 email_reg = tk.StringVar()
 senha_reg = tk.StringVar()

 ctk.CTkLabel(cadastro, text='Área de Cadastro', font=("Arial", 16, "bold")).pack(pady=10)
 ctk.CTkLabel(cadastro, text="Preencha os campos abaixo para criar uma conta").pack(pady=5)

 ctk.CTkLabel(cadastro, text="Nome completo:").pack(pady=5)
 ctk.CTkEntry(cadastro, textvariable=nome_reg).pack(pady=5)

 ctk.CTkLabel(cadastro, text="E-mail:").pack(pady=5)
 ctk.CTkEntry(cadastro, textvariable=email_reg).pack(pady=5)

 ctk.CTkLabel(cadastro, text="Senha:").pack(pady=5)
 ctk.CTkEntry(cadastro, textvariable=senha_reg, show="*").pack(pady=5)

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

 ctk.CTkButton(cadastro, text="Registrar", command=registrar).pack(pady=10)
    
import customtkinter as ctk
import datetime
from banco import salvar_transacao
from tkinter import messagebox

def adicionar_transacao(usuario_id):
    transacao = ctk.CTkToplevel()
    transacao.title("Nova Transação")
    transacao.geometry("400x400")

    tipo = ctk.StringVar(master=transacao, value="Entrada")
    valor = ctk.StringVar(master=transacao)
    categoria = ctk.StringVar(master=transacao)
    descricao = ctk.StringVar(master=transacao)
    data = ctk.StringVar(master=transacao, value=datetime.date.today().strftime("%Y-%m-%d"))

    ctk.CTkLabel(transacao, text="Tipo:").pack()
    ctk.CTkOptionMenu(transacao, variable=tipo, values=["Entrada", "Saída"]).pack()
    ctk.CTkLabel(transacao, text="Valor:").pack()
    ctk.CTkEntry(transacao, textvariable=valor).pack()
    ctk.CTkLabel(transacao, text="Categoria:").pack()
    ctk.CTkEntry(transacao, textvariable=categoria).pack()
    ctk.CTkLabel(transacao, text="Descrição:").pack()
    ctk.CTkEntry(transacao, textvariable=descricao).pack()
    ctk.CTkLabel(transacao, text="Data (YYYY-MM-DD):").pack()
    ctk.CTkEntry(transacao, textvariable=data).pack()

    def salvar():
        try:
            salvar_transacao(
                usuario_id,
                tipo.get(),
                float(valor.get()),
                categoria.get(),
                descricao.get(),
                data.get(),
            )
            messagebox.showinfo("Sucesso", "Transação salva com sucesso!")
            transacao.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar transação: {e}")
    ctk.CTkButton(transacao, text="Salvar", command=salvar).pack(pady=10)
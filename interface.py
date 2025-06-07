import customtkinter as ctk
from tkinter import messagebox
from relatorio import abrir_relatorio
from banco import salvar_transacao
import datetime

def abrir_janela_principal(usuario_id, nome):
    app = ctk.CTk()
    app.title("Área Principal")
    app.geometry("400x400")

    def adicionar_transacao():
        transacao = ctk.CTkToplevel(app)
        transacao.title("Nova Transação")
        transacao.geometry("350x400")

        tipo = ctk.StringVar(value="Entrada")
        valor = ctk.StringVar()
        categoria = ctk.StringVar()
        descricao = ctk.StringVar()
        data = ctk.StringVar(value=datetime.date.today().strftime("%Y-%m-%d"))

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
                salvar_transacao(tipo.get(), float(valor.get()), categoria.get(), descricao.get(), data.get(), usuario_id)
                messagebox.showinfo("Sucesso", "Transação salva.")
                transacao.destroy()
            except:
                messagebox.showerror("Erro", "Verifique os dados!")

        ctk.CTkButton(transacao, text="Salvar", command=salvar).pack(pady=10)

    ctk.CTkLabel(app, text=f"Bem-vindo(a), {nome}", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=20)

    ctk.CTkButton(app, text="Adicionar Transação", width=200, command=adicionar_transacao).pack(pady=10)
    ctk.CTkButton(app, text="Ver Relatórios", width=200, command=lambda: abrir_relatorio(usuario_id)).pack(pady=10)
    ctk.CTkButton(app, text="Sair", width=200, fg_color="red", command=app.destroy).pack(pady=20)

    app.mainloop()
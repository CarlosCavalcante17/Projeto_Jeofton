import customtkinter as ctk
from tkinter import messagebox
from relatorios import abrir_relatorio
from add_transacao import adicionar_transacao

def abrir_janela_principal(usuario_id, nome):
    app = ctk.CTk()
    app.title("Área Principal")
    app.geometry("400x400")

    
    ctk.CTkLabel(app, text=f"Bem-vindo(a), {nome}", font=("Arial", 16, "bold")).pack(pady=20)

    ctk.CTkButton(app, text="Adicionar Transação", width=200, command=lambda: adicionar_transacao(usuario_id)).pack(pady=10)
    ctk.CTkButton(app, text="Ver Relatórios", width=200, command=lambda: abrir_relatorio(usuario_id)).pack(pady=10)
    ctk.CTkButton(app, text="Sair", width=200, fg_color="red", command=app.destroy).pack(pady=20)

    app.mainloop()
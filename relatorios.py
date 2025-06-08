import customtkinter as ctk
import sqlite3
import matplotlib.pyplot as plt
import tkinter.messagebox

def abrir_relatorio(usuario_id):
    relatorio = ctk.CTkToplevel()
    relatorio.title("Relatorio Financeiro")
    relatorio.geometry("400x300")

    conn = sqlite3.connect("dados.db")
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(valor) FROM transacoes WHERE tipo='Entrada' AND usuario_id=?", (usuario_id,))
    total_entradas = cursor.fetchone()[0] or 0

    cursor.execute("SELECT SUM(valor) FROM transacoes WHERE tipo='Saída' AND usuario_id=?", (usuario_id,))
    total_saidas = cursor.fetchone()[0] or 0

    saldo = total_entradas - total_saidas

    ctk.CTkLabel(relatorio, text=f"Entradas: R$ {total_entradas:.2f}").pack(pady=5)
    ctk.CTkLabel(relatorio, text=f"Saídas: R$ {total_saidas:.2f}").pack(pady=5)
    ctk.CTkLabel(relatorio, text=f"Saldo: R$ {saldo:.2f}", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=10)

    ctk.CTkButton(relatorio, text="Gerar Gráfico", command=lambda: gerar_grafico(usuario_id)).pack(pady=5)
    ctk.CTkButton(relatorio, text="Filtrar Dados", command=lambda: abrir_filtros(usuario_id)).pack(pady=5)

    conn.close()

def gerar_grafico(usuario_id):
    conn = sqlite3.connect("dados.db")
    cursor = conn.cursor()
    cursor.execute(""" SELECT categoria, SUM(valor) FROM transacoes
        WHERE usuario_id=?
        GROUP BY categoria""", (usuario_id,))
    dados = cursor.fetchall()
    conn.close()

    if not dados:
        tkinter.messagebox.showinfo("Sem dados", "Nenhuma transação para gerar gráfico.")
        return

    categorias = [d[0] for d in dados]
    valores = [d[1] for d in dados]

    plt.figure(figsize=(6, 6))
    plt.pie(valores, labels=categorias, autopct='%1.1f%%')
    plt.title("Distribuição por categoria")
    plt.show()

def abrir_filtros(usuario_id):
    filtro = ctk.CTkToplevel()
    filtro.title("Filtrar Transações")
    filtro.geometry("350x350")

    tipo_filt = ctk.StringVar()
    categoria_filt = ctk.StringVar()
    data_ini_filt = ctk.StringVar()
    data_fim_filt = ctk.StringVar()

    ctk.CTkLabel(filtro, text="Tipo (Entrada/Saída):").pack(pady=2)
    ctk.CTkEntry(filtro, textvariable=tipo_filt).pack()

    ctk.CTkLabel(filtro, text="Categoria:").pack(pady=2)
    ctk.CTkEntry(filtro, textvariable=categoria_filt).pack()

    ctk.CTkLabel(filtro, text="Data inicial (YYYY-MM-DD):").pack(pady=2)
    ctk.CTkEntry(filtro, textvariable=data_ini_filt).pack()

    ctk.CTkLabel(filtro, text="Data final (YYYY-MM-DD):").pack(pady=2)
    ctk.CTkEntry(filtro, textvariable=data_fim_filt).pack()

    def aplicar_filtros():
        query = "SELECT tipo, valor, categoria, descricao, data FROM transacoes WHERE usuario_id=?"
        params = [usuario_id]

        if tipo_filt.get():
         query += " AND tipo=?"
         params.append(tipo_filt.get())

        if categoria_filt.get():
         query += " AND categoria LIKE ?"
         params.append(f"%{categoria_filt.get()}%")
        if data_ini_filt.get():
         query += " AND  date(data) >= ?"
         params.append(data_ini_filt.get())
        if data_fim_filt.get():
         query += " AND date(data) <= ?"
         params.append(data_fim_filt.get())

        conn = sqlite3.connect("dados.db")
        cursor = conn.cursor()
        cursor.execute(query, params)
        resultados = cursor.fetchall()
        conn.close()

        resultado_janela =ctk.CTkToplevel()
        resultado_janela.title("Resultados Filtrados")
        resultado_janela.geometry("500x300")

        for row in resultados:
          texto = f"Tipo: {row[0]} | Valor: R${row[1]:.2f} | Categoria: {row[2]} | Desc: {row[3]} | Data: {row[4]}"
          ctk.CTkLabel(resultado_janela, text=texto, anchor="w"). pack(padx=5, pady=2)

    ctk.CTkButton(filtro, text="Aplicar filtros", command=aplicar_filtros).pack(pady=15)

       

    
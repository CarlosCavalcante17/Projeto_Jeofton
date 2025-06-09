import customtkinter as ctk
from banco import autenticar_usuario
from banco import criar_tabela
from cadastro import abrir_cadastro
import interface

criar_tabela()

# configuração da aparencia
ctk.set_appearance_mode("Dark")

# Verificar se o usuario e senha estão corretos
def fazer_login():
   usuario = campo_usuario.get()
   senha = campo_senha.get()
   resultado_login = autenticar_usuario(usuario, senha)
   if resultado_login:
      resultado.configure(text="Login feito com sucesso!", text_color="green")
      app.after(500, app.destroy)
      usuario_id, nome = resultado_login
      interface.abrir_janela_principal(usuario_id, nome)

      
   else:
      resultado.configure(text="E-mail ou senha incorretos.", text_color="red")

# Criação da janela principal
app = ctk.CTk()
app.title("Login")
app.geometry("400x400")

# Criação dos campos
ctk.CTkLabel(app, text=f"Sistema de Controle Financeiro Pessoal", font=("Arial", 16, "bold")).pack(pady=20)
# Label
label_usuario = ctk.CTkLabel(app, text="E-mail:")
label_usuario.pack(pady=10)
# Entry
campo_usuario = ctk.CTkEntry(app, placeholder_text="Digite seu e-mail")
campo_usuario.pack(pady=10)
# Label
label_senha = ctk.CTkLabel(app, text="Senha:")
label_senha.pack(pady=10)
# Entry
campo_senha = ctk.CTkEntry(app, placeholder_text="Digite sua senha", show="*")
campo_senha.pack(pady=10)
# Botão
botao_Login = ctk.CTkButton(app, text="Login", command=fazer_login)
botao_Login.pack(pady=10)
# Botão
botao_registrar = ctk.CTkButton(app, text="Registrar", command=lambda: abrir_cadastro(app))
botao_registrar.pack(pady=5)
# Campo feedback de login
resultado = ctk.CTkLabel(app, text="")
resultado.pack(pady=10)

# Iniciar o loop da aplicação
app.mainloop()
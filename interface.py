import tkinter as tk
import customtkinter as ctk

# configuração da aparencia
ctk.set_appearance_mode("Dark")

# Criação da função de validação do login
def validar_Login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()

# Verificar se o usuario e senha estão corretos
    if usuario == "Nelson" and senha == "123456":
        resultado_login.configure(text="Login feito com sucesso!", text_color="green")
    else:
        resultado_login.configure(text="Usuário ou senha incorretos.", text_color="red")

# Criação da janela principal
app = ctk.CTk()
app.title("Login")
app.geometry("400x400")

# Criação dos campos
# Label
label_usuario = ctk.CTkLabel(app, text="Usuário:")
label_usuario.pack(pady=10)
# Entry
campo_usuario = ctk.CTkEntry(app, placeholder_text="Digite seu usuário")
campo_usuario.pack(pady=10)
# Label
label_senha = ctk.CTkLabel(app, text="Senha:")
label_senha.pack(pady=10)
# Entry
campo_senha = ctk.CTkEntry(app, placeholder_text="Digite sua senha", show="*")
campo_senha.pack(pady=10)
# Botão
botao_Login = ctk.CTkButton(app, text="Login", command=validar_Login)
botao_Login.pack(pady=10)
# Botão
botao_registrar = ctk.CTkButton(app, text="Registrar")
botao_registrar.pack(pady=5)
# Campo feedback de login
resultado_login = ctk.CTkLabel(app, text="")
resultado_login.pack(pady=10)

# Iniciar o loop da aplicação
app.mainloop()

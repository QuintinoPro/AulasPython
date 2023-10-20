import tkinter as tk

# Função para executar quando o botão for pressionado
def on_button_click():
    label.config(text="Olá, Mundo!")

# Cria uma janela
janela = tk.Tk()
janela.title("Exemplo com Tkinter")

# Cria um rótulo
label = tk.Label(janela, text="Clique no botão abaixo")
label.pack()

# Cria um botão
button = tk.Button(janela, text="Clique aqui", command=on_button_click)
button.pack()

# Inicia o loop principal da janela
janela.mainloop()

# # GUI 
# import tkinter as tk

# janela  =  tk.Tk()
# # janela.geometry('500x500')
# janela.title('Isso é uma Janela')

# def soma():
#     n1 = float(input_entry1.get())
#     n2 = float(input_entry2.get())
#     soma  =  n1  + n2
#     resultado.config(text=f'Resultado {int(soma)}')


# def sub():
#     n1 = float(input_entry1.get())
#     n2 = float(input_entry2.get())
#     sub  =  n1  - n2
#     resultado.config(text=f'Resultado {int(sub)}')

# def div():
#     n1 = float(input_entry1.get())
#     n2 = float(input_entry2.get())
#     div  =  n1  // n2
#     resultado.config(text=f'Resultado {div}')

# def mult():
#     n1 = float(input_entry1.get())
#     n2 = float(input_entry2.get())
#     mult  =  n1  * n2
#     resultado.config(text=f'Resultado {mult}')


# text_label =  tk.Label(janela, text='CALCULADORA', fg = 'black', bg='white')
# text_label.grid(row = 0, column = 1)
# # text_label.pack()


# input_entry1 = tk.Entry(janela, width = 5)
# input_entry1.grid(row = 2, column = 2 , padx = 10)
# # input_entry1.pack()

# input_entry2 = tk.Entry(janela, width = 5)
# input_entry2.grid(row = 2, column = 4, padx = 10 )
# # input_entry2.pack()


# btn_soma  = tk.Button(janela, text= '+', command = soma, fg='white', bg='black')
# btn_soma.grid(row = 3, column = 3, padx = 10, pady=10)
# # btn_soma.pack()  

# btn_sub  = tk.Button(janela, text= '-', command = sub, fg='white', bg='black')
# btn_sub.grid(row = 3, column = 2, padx = 10, pady=10)
# # btn_sub.pack()  

# btn_div  = tk.Button(janela, text= '/', command = div, fg='white', bg='black')
# btn_div.grid(row = 3, column = 4, padx = 10, pady=10)
# # btn_div.pack()  

# btn_mult  = tk.Button(janela, text= '*', command = mult, fg='white', bg='black')
# btn_mult.grid(row = 3, column = 5, padx = 10, pady=10)
# # btn_mult.pack()  

# resultado =  tk.Label(janela, text='Resultado')
# resultado.grid(row = 2, column = 6, padx = 5, pady=5)
# # resultado.pack()

# janela.mainloop()






# EXERCICIOS




import tkinter as tk
from tkinter import ttk

def calcular_imc():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        if altura <= 0:
            label_resultado.config(text="Altura deve ser maior que zero.")
            return
        imc = peso / (altura ** 2)
        label_resultado.config(text=f"Seu IMC é: {imc:.2f}")
    except ValueError:
        label_resultado.config(text="Por favor, insira valores válidos.")

# Cria a janela principal
root = tk.Tk()
root.title("Calculadora de IMC")
root.geometry("500x500")

# Cria e posiciona os widgets
label_peso = tk.Label(root, text="Peso (kg):")
label_peso.pack(pady=10)
entry_peso = tk.Entry(root)
entry_peso.pack(pady=5)

label_altura = tk.Label(root, text="Altura (m):")
label_altura.pack(pady=10)
entry_altura = tk.Entry(root)
entry_altura.pack(pady=5)

button_calcular = tk.Button(root, text="Calcular IMC", command=calcular_imc)
button_calcular.pack(pady=20)

# Label para exibir o resultado
label_resultado = tk.Label(root, text="Seu IMC será exibido aqui.")
label_resultado.pack(pady=20)

# Inicia o loop da interface gráfica
root.mainloop()

import tkinter as tk
from tkinter import ttk
import datetime as dt

type_list = ["Galão", "Caixa", "Saco", "Unidade"]
code_list = []

window = tk.Tk() # Cria a janela

#Criação da Função
def register():
    description = entry_description.get()
    type_ = combobox_select_type.get()
    amount = entry_amount.get()
    creation_date = dt.datetime.now()
    creation_date = creation_date.strftime("%d/%m/%Y %H:%M")
    code = len(code_list) + 1
    str_code = f'COD-{code}'
    code_list.append((str_code, description, type_, amount, creation_date))


#Título da janela
window.title("Ferramenta de cadastro de materiais")

label_description = tk.Label(text="Descrição do Material")
label_description.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

entry_description = tk.Entry()
entry_description.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

label_unit_type = tk.Label(text="Tipo da Unidade do Material")
label_unit_type.grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

combobox_select_type = ttk.Combobox(values=type_list)
combobox_select_type.grid(row=3, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)

label_amount = tk.Label(text="Quantidade na Unidade de Material")
label_amount.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

entry_amount = tk.Entry()
entry_amount.grid(row=4, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)

button_create_code = tk.Button(text="Criar Código", command=register)
button_create_code.grid(row=5, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

# A janela fica em loop
window.mainloop() 

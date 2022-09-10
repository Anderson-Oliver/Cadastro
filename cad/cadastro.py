from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme('Reddit')
layout =[
    [sg.Text('Usuario'), sg.Input(key='usuario')],
    [sg.Text('senha'), sg.Input(key='senha',password_char='*')],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Enter')]
]
# Janela

# Ler os eventos
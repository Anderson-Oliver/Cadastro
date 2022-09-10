from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme('Reddit')
layout =[
    [sg.Text('Usuario'), sg.Input(key='usuario', size = (20,1))],
    [sg.Text('Senha'), sg.Input(key='senha',password_char='*', size = (20,1))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Enter')]
]
# Janela
janela = sg.Window('Tela de Login',layout)
# Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Enter':
        if valores['usuario'] == 'Anderson' and valores['senha'] == '2328':
            print("Bem vindo!")
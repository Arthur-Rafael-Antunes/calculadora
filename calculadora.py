from PySimpleGUI import *

import PySimpleGUI as sg

sg.theme('DarkTeal6')

layout = [ 
    [sg.Input('', key='-DISPLAY-', size=(17, 1)) ],
    [sg.Button('C', key='C',size=(3,1)), sg.Button('<-', key='Backspace',size=(3,1)), sg.Button('%', key="%", size=(3,1)), sg.Button('/', key='/', size=(3,1))],
    [sg.Button('7', key='7',size=(3,1)), sg.Button('8', key='8',size=(3,1)), sg.Button('9', key='9',size=(3,1)), sg.Button('*', key='*',size=(3,1))], 
    [sg.Button('4', key='4',size=(3,1)), sg.Button('5', key='5',size=(3,1)), sg.Button('6', key='6',size=(3,1)), sg.Button('-', key='-',size=(3,1))],
    [sg.Button('1', key='1',size=(3,1)), sg.Button('2', key='2',size=(3,1)), sg.Button('3', key='3',size=(3,1)), sg.Button('+', key='+', size=(3,1))],
    [sg.Button('+/-', key='plus_minus', size=(3,1)), sg.Button('0', key='0',size=(3,1)),  sg.Button('.', key='.',size=(3,1)), sg.Button('=', key='=',size=(3,1))],
]

window = sg.Window('Calc 3Ia', layout, font="monospace 30", element_justification='center')

exp = ''

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event in '1234567890':
        exp += event
        window['-DISPLAY-'].update(exp)
    elif event == '=':
        try:
            result = eval(exp)  # Avalia a expressão matemática
            window['-DISPLAY-'].update(str(result))
            exp = str(result)  # Define a expressão como o resultado para cálculos subsequentes
        except:
            window['-DISPLAY-'].update('Erro')
            exp = ''
    elif event == 'C':
        exp = ''
        window['-DISPLAY-'].update(exp)
    elif event == 'Backspace':
        exp = exp[:-1]
        window['-DISPLAY-'].update(exp)
    elif event == 'plus_minus':
        if exp and exp[0] == '-':
            exp = exp[1:]
        else:
            exp = '-' + exp
        window['-DISPLAY-'].update(exp)
    elif event == '%':
        try:
            result = eval(exp) / 100  # Avalia a expressão matemática e divide por 100 para obter o valor percentual
            window['-DISPLAY-'].update(str(result))
            exp = str(result)  # Define a expressão como o resultado para cálculos subsequentes
        except:
            window['-DISPLAY-'].update('Erro')
            exp = ''
    else:
        exp += event
        window['-DISPLAY-'].update(exp)

window.close()

import PySimpleGUI as sg

sg.theme('Reddit')  # Let's set our own color theme


layout = [ 
            [sg.Input('', key='-DISPLAY-', size=(12,1))],
            [sg.B('7', key='7'),sg.B('8', key='8'),sg.B('9', key='9'),sg.B('/', key='/')],
            [sg.B('4', key='4'),sg.B('5', key='5'),sg.B('6', key='6'),sg.B('*', key='*')],
            [sg.B('1', key='1'),sg.B('2', key='2'),sg.B('3', key='3'),sg.B('-', key='-')],
            [sg.B('.', key='.'),sg.B('0', key='0'),sg.B('=', key='='),sg.B('+', key='+')],
]

window = sg.Window('Calc 3Ia',layout,font="monospace 30")

exp=''

while True:
    event, values = window.read()   
    print(event, values)
    if event == sg.WIN_CLOSED :     
      break
    elif event in '1234567890' :
      exp+=event
      window['-DISPLAY-'].update(exp)
window.close()

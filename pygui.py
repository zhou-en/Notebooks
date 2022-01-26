import PySimpleGUI as sg
# All the stuff inside your window. This is the PSG magic code compactor...
layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.OK(), sg.Cancel()]]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events"
while True:             
    event, values = window.Read()
    if event in ('OK', 'Cancel'):
        break

window.Close()

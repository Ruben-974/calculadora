import PySimpleGUI as sg

def create_decorator(value):

    def create_function(funct):

        def inner(txt):

            return funct(txt, value)

        return inner
    
    return create_function


def convert_to_number(x):
    try:
        return int(x)
    except ValueError:
        return None
        

@create_decorator(7)

def model_button(txt, num):

    return sg.Button(txt, size=num)


input_ = ''

layout = [[sg.Input(key='input', size=40, justification='right', default_text=input_, disabled=True)],
          [model_button('7'), model_button('8'), model_button('9'), model_button('+')],
          [model_button('4'), model_button('5'), model_button('6'), model_button('-')],
          [model_button('1'), model_button('2'), model_button('3'), model_button('x')],
          [model_button(','), model_button('0'), model_button('='), model_button('/')]
          ]

window = sg.Window('Calculator', layout)

while True:

    event, value = window.read()

    if event is None:

        break
    
    if convert_to_number(event) is None:   

        if value['input'] == '':

            continue
        
    else:

        input_ += event

    if event in '+-x/=':

        print(event)
    
    window['input'].update(input_)
    window.refresh()

   

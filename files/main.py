import PySimpleGUI as sg

def create_decorator(value):

    def create_function(funct):

        def inner(txt):

            return funct(txt, value)

        return inner
    
    return create_function


def convert_to_number(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None

@create_decorator(8)

def model_button(txt, num):

    return sg.Button(button_text=txt, size=num)


input_, previous_value, current_value, operator, result, save_input_ = '', None, None, None, None, None

layout = [[
    sg.Input(key='operator', size=5, justification='center', default_text=input_, disabled=True, ),
    sg.Input(key='memory', size=18, justification='center', default_text=input_, disabled=True, ), 
    sg.Input(key='input', size=29, justification='right', default_text=input_, disabled=True, )
    
    
    ],
           
          [model_button('7'), model_button('8'), model_button('9'), model_button('C'), model_button('^')],
          [model_button('4'), model_button('5'), model_button('6'), model_button('CE'), model_button('%')],
          [model_button('1'), model_button('2'), model_button('3'), model_button('x'), model_button('+')],
          [model_button('.'), model_button('0'), model_button('='), model_button('/'), model_button('-')]
          ]

window = sg.Window('Calculator', layout)

while True:

    event, value = window.read()

    if event is None:

        break

    if event not in '+-/x=CE':

        if event not in '.':

            input_ += event

        current_value = convert_to_number(input_)
    
    if event == '.' and '.' not in input_:

        input_ += '.'

    if event in ('+', '-', 'x', '/', 'CE', 'C', '='):

        print(value, operator)

        if event == 'C':

            previous_value = current_value = result = None

        print(f'OPERATION! old: {previous_value} | new: {current_value} | operator: {operator} | result: {result} | input_: {input_}')

        input_ = ''

        if previous_value != None and current_value != None:

            if operator == '+':

                result = previous_value + current_value

            if operator == '-':

                result = previous_value - current_value
            
            if operator == 'x':

                result = previous_value * current_value
            
            if operator == '/':

                result = previous_value / current_value

            if operator == 'CE':

                result = None

        if operator == '=' or event == '=':

            if convert_to_number(result) != None:
                input_ = str(result)

        else:

             operator = event

        previous_value = result
            
        if result is None:

            previous_value = current_value

        current_value = None
        
        #print(f'OPERATION! old: {previous_value} | new: {current_value} | operator: {operator} | result: {result}')

    window['input'].update(input_)
    if event != 'C':
        window['memory'].update(result)
    else:
        window['memory'].update('')
    if convert_to_number(event) is None:
        window['operator'].update(event)
    window.refresh()

window.close()
print('end')

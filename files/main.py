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
    except ValueError:
        return None

@create_decorator(7)

def model_button(txt, num):

    return sg.Button(button_text=txt, size=num)


input_, previous_value, current_value, operator, result = '', None, None, None, None

layout = [[sg.Input(key='input', size=30, justification='right', default_text=input_, disabled=True), model_button('<<')],
          [model_button('7'), model_button('8'), model_button('9'), model_button('+')],
          [model_button('4'), model_button('5'), model_button('6'), model_button('-')],
          [model_button('1'), model_button('2'), model_button('3'), model_button('x')],
          [model_button('.'), model_button('0'), model_button('='), model_button('/')]
          ]

window = sg.Window('Calculator', layout)

while True:

    event, value = window.read()

    if event is None:

        break

    if event not in '+-/x=<<':

        if event not in '.':

            input_ += event

        current_value = convert_to_number(input_)
    
    if event == '.' and '.' not in input_:

        input_ += '.'

    if event == '<<':

        input_ = input_[:-1]
        current_value = convert_to_number(input_)

    if event in '+-/x=':

        input_ = ''

        #print(f'OPERATION! old: {previous_value} | new: {current_value} | operator: {operator} | result: {result}')

        if previous_value != None and current_value != None:

            if operator == '+':

                result = previous_value + current_value

            if operator == '-':

                result = previous_value - current_value
            
            if operator == 'x':

                result = previous_value * current_value
            
            if operator == '/':

                result = previous_value / current_value

        if operator == '=' or event == '=':

            input_ = str(result)
            
            previous_value = result

        else:

            operator = event

        if result is None:

            previous_value = current_value

        current_value = None

        print(f'OPERATION! old: {previous_value} | new: {current_value} | operator: {operator} | result: {result}')


    window['input'].update(input_)
    window.refresh()

window.close()
print('end')

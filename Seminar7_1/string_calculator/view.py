from decimal import Decimal


def first_input():
    first_input = input('Input number or string expression: ')
    return first_input

def input_number(text: str):
    while True:
        try:
            number = float(input(f'{text}'))
            number = Decimal(str(number))
            return number
        except:
            print('Input number!!!')


def input_operation():
    while True:
        operation = input('Input operator: ')
        if operation in ['+', '-', '*', '/', '=']:
            return operation
        else:
            print('Check if the operator input is correct'
                  '(+, -, *, /, =)')


def print_memory(value):
    print(value)

def print_result(value: Decimal):
    if value == int(value):
        print(f'Result: {int(value)}')
    else:
        print(f'Result: {round(value,4)}')

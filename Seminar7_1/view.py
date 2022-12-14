def input_number() -> int:
    while True:
        try:
            number = int(input('Input integer number: '))
            return number
        except:
            print('Mistake')

def input_operation():
    while True:
        operation  = input('Input operation: ')
        if operation in ['+', '-', '*', '/', '=']:
            return operation
        else:
            print('Input correct operation')


def print_to_console(value_text):
    print(value_text)

def log_off():
    print('Good Bye!')

def print_division_by_zero():
    print('Divide by zero is forbidden!')

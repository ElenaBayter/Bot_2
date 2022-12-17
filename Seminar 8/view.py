def main_menu():
    print('\n1. Show phone_book')
    print('2. Open phone_book file ')
    print('3. Save phone_book file')
    print('4. Add contact')
    print('5. Change contact')
    print('6. Delete contact')
    print('7. Find contact')
    print('0. Exit\n')
    return choice_main_menu()

def choice_main_menu():
    while True:
        try:
            choice = int(input('Choose the command from menu: '))
            if choice in range(0, 8):
                print()
                return choice
            else:
                print('Try again')
        except:
            print('Input error! Incorrect data!')

def print_phone_book(phone_book: list):
    if len(phone_book) > 0:
        for id, contact in enumerate(phone_book, 1):
            print(id, *contact)
    else:
        print('Phone book is empty or not downloaded')

def log_off():
    print('Good bye, see you soon!')

def load_seccess():
     print('Phone book is downloaded!')

def save_success():
    print('Phone book is saved!')

def change_success():
    print('Contact changed')

def remove_success():
    print('Contact deleted')

def print_founded_contact():
    print('Contact founded')

def input_new_contact():
    name = input('Input contact name: ')
    phone = input('Input contact phone number: ')
    comment = input('Input comment to contact: ')
    return [name, phone, comment]

def input_remove_contact():
    id = int(input('Input contact ID, which you want to delete: '))
    return id

def input_change_contact():
    id = int(input('Input contact ID, which you want to change: '))
    return id




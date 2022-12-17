phone_book = []

def get_phone_book():
    global phone_book
    return phone_book

def set_phone_book(new_phone_book):
    global phone_book
    phone_book = new_phone_book

def add_contact(contact: list):
    global phone_book
    phone_book.append(contact)

def remove_contact(id):
    global phone_book
    name = phone_book[id-1][0]
    confirm = input(f'Do you really want to delete contact {name}? (y/n')
    if confirm.lower() == 'y':
        phone_book.pop(id-1)
        return True
    return False

def change_contact(id):
    global phone_book
    name = phone_book[id-1][0]
    new_info = input('Input changed information about you contact')
    confirm = str(input(f'Do you really want to change contact {name}? (y/n'))
    if confirm.lower() == 'y':
        name.replace(phone_book[id-1], new_info)
        return True
    return False

def find_contact(contact: list):
    global phone_book
    name = input('Input name of contact you are looking for: ')
    number = input('Input number of contact you are looking for: ')
    if name in phone_book[id-1][0] or number in phone_book[id-1][1]:
        return phone_book[id-1]



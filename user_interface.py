def get_info ():
    info = []
    last_name = input('Введите фамилию: ')
    info.append(last_name)
    first_name = input('Введите имя: ')
    info.append(first_name)
    phone_number = input('Введите телефон: ')
    info.append(phone_number)
    return info

# Поиск
def find_contact(phonebook,req):
    a = ''
    for i  in phonebook:
        if i.find(req) != -1:
            a = i
    if a == '':
        return "Empty"
    else:
        return a





from user_interface import get_info as gi

info = gi()

def writing_txt ():
    file = 'phonebook.txt'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'Фамилия: {info[0]}\nИмя: {info[1]}\nНомер телефона: {info[2]}\n\n')
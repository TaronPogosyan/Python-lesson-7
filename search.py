def find_contact(phonebook,req):
    a = ''
    for i  in phonebook:
        if i.find(req) != -1:
            a = i
    if a == '':
        return "Empty"
    else:
        return a
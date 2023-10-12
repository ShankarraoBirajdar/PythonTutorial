def convetCase(name):
    new_string = ''
    for s in name:
        if s.isupper():
            new_string += s.lower()
        else:
            new_string += s.upper()
    return new_string


print(convetCase('Shankar'))
print(convetCase('SHANKAR'))
print(convetCase('shankar'))



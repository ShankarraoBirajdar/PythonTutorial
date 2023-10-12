def title(str1):
    tokens = str1.split()
    for i in range(len(tokens)):
        tokens[i] = capitalize(tokens[i])
    str1 = ' '.join(tokens)
    return str1


def capitalize(str1):
    new_str = ''
    for i in range(len(str1)):
        if i == 0:
            new_str += str1[i].upper()
        else:
            new_str += str1[i]
    return new_str


print(capitalize('shankar'))
print(title('hello how are you'))


def remove_word_before(email, char):
    index = email.find(char)
    return email.replace(email[:index], '')


x = remove_word_before('abc@gmail.com', '@')
print(x)


def remove_duplicate_from_list():
    list_1 = [1, 1, 2, 2, 3, 3, 4, 4]
    list_2 = []

    for i in list_1:
        if i not in list_2:
            list_2.append(i)
    print(list_2)


remove_duplicate_from_list()

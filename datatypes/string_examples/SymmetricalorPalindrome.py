def symmetrical_palindrome(name):
    half = int(len(name) / 2)
    first_str = name[:half]
    second_str = name[half:]

    # symmetric
    if first_str == second_str:
        print(name, 'string is symmetrical')
    else:
        print(name, 'string is Not symmetrical')

        # palindrome
    if first_str == second_str[::-1]:  # ''.join(reversed(second_str)) [slower]
        print(name, 'string is palindrome')
    else:
        print(name, 'string is not palindrome')


symmetrical_palindrome('khokho')
symmetrical_palindrome('amaama')

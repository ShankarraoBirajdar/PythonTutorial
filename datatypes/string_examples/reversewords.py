# Python code
# To reverse words in a given string

def reversing_words(string):
    # reversing words in a given string
    s = string.split()[::-1]
    print(s)

    # mehtod 1
    print(' '.join(s))

    # method 2
    l = []
    for i in s:
        # appending reversed words to l
        l.append(i)
        # printing reverse words
    print(" ".join(l))


if __name__ == "__main__":
    reversing_words('geeks quiz practice code')


def reverse_function(name):
    for i in range(len(name) - 1, -1, -1):
        print(name[i], end='')


reverse_function('Shankar')






def main():
    # print('Welcome to Python Programming')
    try:
     first_num = input("Enter a first number\t")
     second_num = input("Enter a second number\t")
     result = int(first_num) + int(second_num)
     print('result = ',result)
    except ValueError:
        ('Please enter a positive number:')

main()
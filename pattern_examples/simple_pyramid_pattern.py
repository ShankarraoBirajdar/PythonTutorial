class SimplePyramid:
    def simple_pyramid():
        row = int(input('Enter the no row\n'))
        pattern=input('Enter the pattern\n')
        for i in range(row+1):
            for j in range(i):
                print(pattern,end='')
            print('')


    def simple_pyramid1(row):
        for i in range(row+1):
            for j in range(i):
                print(i,end='')
            print('')


    def simple_pyramid2(row):
        for i in range(row+1):
            for j in range(i):
                print(j,end='')
            print('')

    def simple_pyramid3(row):
        for i in range(row+1):
            print('@'*i,)

    simple_pyramid()
    simple_pyramid1(5)
    simple_pyramid2(5)
    simple_pyramid3(5)
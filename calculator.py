while True:
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. Break')
    a=int(input('Enter your choice'))
    if a==5:
        break


    x=int(input('Enter first number'))
    y=int(input('Enter second number'))

    if a==1:
        print('x+y=',x+y)
    if a==2:
        print('x-y=',x-y)
    if a==3:
        print('x*y=',x*y)
    if a==4:
        print('x/y=',x/y)


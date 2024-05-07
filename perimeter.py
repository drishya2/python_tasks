while True:
    print('1. Circle')
    print('2. Rectangle')
    print('3. Square')
    print('4. Break')

    x=int(input('Enter your choice'))
    if x==4:
        break
    if x==1:
        a=int(input('Enter the radius'))
        print('perimeter=',2*3.14*a)
    if x==2:
        l=int(input('Enter the length'))
        h=int(input('Enter the height'))
        print('perimeter=',2*(l+h))
    if x==3:
        s=int (input('Enter the side'))
        print('perimeter=',4*s)



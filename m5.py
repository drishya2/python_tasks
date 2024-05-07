import m1
import m2
import m3
import m4
while True:

    print('1.addition')
    print('2.subtraction')
    print('3.multiplication')
    print('4.division')

    n=int(input('enter choice'))
    if n==1:
        m1.add()
    if n==2:
        m2.sub()
    if n==3:
        m3.multiply()
    if n==4:
        m4.div()

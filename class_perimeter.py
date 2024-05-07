
class perimeter:
    def circle(self):
        a=int(input('enter radius'))
        p=2*3.14*a
        print('perimeter=',p)



    def rectangle(self):
        a=int(input('enter length'))
        b=int(input('enter height'))
        p=2*(a+b)
        print('perimeter=', p)



    def square(self):
        a=int(input('enter side'))
        p=4*a
        print('perimeter=', p)

per=perimeter()

while True:
    print('1.circle')
    print('2.rectangle')
    print('3.square')
    print('4.break')
    c=int(input('enter choice'))

    if c==1:
        per.circle()
    if c==2:
        per.rectangle()
    if c==3:
        per.square()
    if c==4:
        break







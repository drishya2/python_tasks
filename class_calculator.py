
class calculator:
    def addition(self):

        a=int(input('Enter first number'))
        b = int(input('Enter second number'))
        print('sum is:',a+b)



    def subtraction(self):
        a = int(input('Enter first number'))
        b = int(input('Enter second number'))
        print('difference is:',a - b)

    def multiplication(self):
        a = int(input('Enter first number'))
        b = int(input('Enter second number'))
        print('product is:',a * b)

    def division(self):
        a = int(input('Enter first number'))
        b = int(input('Enter second number'))
        print('division is:',a / b)
s=calculator()

while True:
    print('1.addition')
    print('2.subtraction')
    print('3.multiplication')
    print('4.division')
    print('5.break')

    c=int(input ('enter choice'))
    if c==1:
        s.addition()
    if c==2:
        s.subtraction()
    if c==3:
        s.multiplication()
    if c==4:
        s.division()
    if c==5:
        break




while True:
    print('1.addition')
    print('2.subtarction')
    print('3.multiplication')
    print('4.division')

    n=int(input('Enter your choice'))

    def addition(a,b):
        sum=a+b
        print('answer:',sum)

    def subtraction(a,b):
        sub=a-b
        print('answer:',sub)

    def multiply(a,b):
        mult=a*b
        print('answer:',mult)

    def divide(a,b):
        div=a/b
        print('answer:',div)

    x=int(input('enter first number'))
    y=int(input('enter second number'))

    if n==1:
        addition(x,y)
    if n==2:
        subtraction(x,y)
    if n==3:
        multiply(x,y)
    if n==4:
        divide(x,y)







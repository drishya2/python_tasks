# def multiply():
#     a=int(input('enter first number'))
#     b=int(input('enter second number'))
#     m=a*b
#     print(m)



#vehicle

list=[]

class vehicle:
    def __init__(self):
        self.number=0
        self.name=0
        self.price=0
        self.wheel=0

    def add(self):
        self.number=int(input('enter number'))
        self.name=input('enter name')
        self.price=int(input('enter price '))
        self.wheel=int(input('enter wheels'))
    def display(self):
        print('number:',self.number)
        print('name:', self.name)
        print('price:', self.price)
        print('wheels:', self.wheel)



while True:
    print('1.add vehicle')
    print('2.display vehicle')
    c=int(input('enter choice'))


    if c==1:
        obj=vehicle()
        s=obj.add()
        list.append(s)


    if c==2:
        while True:
            print('1) 2 wheels')
            print('2) 3 wheels')
            print('3) 4 wheels')
            c=int(input('enter choice'))

            if c==1:
                for i in list:
                    if i.wheel==2:
                        obj.display()

            if c==2:
                for i in list:
                    if i.wheel==3:
                        obj.display()

            if c==3:
                for i in list:
                    if i.wheel==4:
                        obj.display()










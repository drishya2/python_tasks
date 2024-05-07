list=[]
class vehicle:
    def __init__(self):
        self.number=0
        self.name=0
        self.price=0
        self.wheel=0
    def add(self):
        self.number=int(input('Enter vehicle number'))
        self.name=input('Enter vehicle name')
        self.price=int(input('Enter vehicle price'))
        self.wheel=int(input('Enter number of wheels'))




    def display(self):
        print('vehicle number:',self.number)
        print('vehicle name:', self.name)
        print('vehicle price:', self.price)
        print('number of wheels:', self.wheel)



while True:
    print('1.add vehicle')
    print('2.display vehicle')
    print('3.break')
    c=int(input('enter your choice'))



    if c==1:
        v = vehicle()
        v.add()
        list.append(v)



    if c==2:
        while True:
            print('1. 2 wheels')
            print('2. 3 wheels')
            print('3. 4 wheels')
            a=int(input('choice'))
            if a==1:
                for i in list:
                    if i.wheel==2:
                        i.display()
            if a==2:
                for i in list:
                    if i.wheel==3:
                        i.display()
            if a==3:
                for i in list:
                    if i.wheel==4:
                        i.display()










    if c==3:
        break

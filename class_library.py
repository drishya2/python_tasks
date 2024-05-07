
lib=[]
user=[]

class library:
    def __init__(self):
        self.id=0
        self.title=0
        self.price=0
        self.author=0
        self.edition=0

        self.id2=0
        self.name=0
        self.email=0
        self.phone=0
        self.password=0
        self.cpassword=0


    def add_book(self):
        self.id=int(input('enter id'))
        self.title=input('enter title')
        self.price=int(input('enter price'))
        self.author=input('enter author')
        self.edition=int(input('enter edition'))
    def display(self):
        print('id:',self.id)
        print('title:', self.title)
        print('price', self.price)
        print('author:', self.author)
        print('edition', self.edition)


    def register(self):
        self.id2=int(input('enter id'))
        self.name=input('enter name')
        self.email=input('enter email')
        self.phone=int(input('enter phone number'))
        self.password=input('enter password')
        self.cpassword=input('confirm password')
        if self.password==self.cpassword:
            print('Registered')

    def display_user(self):
        print('id:',self.id2)
        print('name:',self.name)
        print('email:',self.email)
        print('phone:',self.phone)






while True:
    print('1.admin')
    print('2.user')
    c=int(input('enter your choice'))


    if c==1:
        while True:
            print('1.add a book')
            print('2.update book')
            print('3.delete book')
            print('4.display book')
            print('5. break')
            c=int(input('enter choice'))

            if c==1:
                l=library()
                l.add_book()
                lib.append(l)

            if c==2:
                while True:
                    print('1.title')
                    print('2.price')
                    print('3.author')
                    print('4.edition')
                    print('5.break')
                    c=int(input('enter choice'))
                    if c==1:
                        k=int(input('enter id'))
                        new=input('enter new title')
                        for i in lib:
                            if k==i.id:
                                i.title=new

                    if c==2:
                        k=int(input('enter id'))
                        new=int(input('enter new price'))
                        for i in lib:
                            if k==i.id:
                                i.price=new

                    if c==3:
                        k=int(input('enter id'))
                        new=input('enter new author')
                        for i in lib:
                            if k==i.id:
                                i.author=new


                    if c==4:
                        k=int(input('enter id'))
                        new=int(input('enter new edition'))
                        for i in lib:
                            if k==i.id:
                                i.edition=new
                    if c==5:
                        break




            if c==3:
                k=int(input('enter id'))
                for i in lib:
                    if i.id==k:

                        lib.remove(i)









            if c==4:
                k=int(input('enter id'))
                for i in lib:
                    if i.id==k:
                        l.display()

    if c == 2:


        while True:

            print('1. Register')
            print('2. Login')
            print('3. display user')
            c=int(input('enter choice'))



            if c==1:
                u=library()
                u.register()
                user.append(u)

            if c==2:
                name=input('enter name')
                password=input('enter password')
                for i in user:
                    if i.name==name and i.password==password:
                        print('successfully logged in')
                    else:
                        print('wrong password or email')

            if c==3:
                d=int(input('enter id'))
                for i in user:
                    if i.id2==d:
                        o=library()
                        o.display_user()





                


                















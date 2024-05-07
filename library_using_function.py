library=[]
while True:
    print('1.add book')
    print('2.display book')
    print('3.update book')
    print('4.delete book')
    c=int(input('Enter your choice'))

    def create():
        id=int(input('enter id'))
        name=input('enter title')
        price=int(input('enter price'))
        author=input('enter author')
        l=[]
        l.append(id)
        l.append(name)
        l.append(price)
        l.append(author)
        library.append(l)
        print(library)


    def display():
        print(library)

    def update():
        while True:
            print('1.update title')
            print('2.update price')
            print('3.update author')
            print('5. break')
            u=int(input('enter your choice:'))
            if u==1:
                for i in library:
                    k = int(input('enter key'))

                    if i[0]==k:
                        t=input('enter new title')
                        i[1]=t
            if u==2:
                for i in library:
                    if i[0]==k:
                        r=input('enter new price')
                        i[2]=r

            if u==3:
                for i in library:
                    if i[0]==k:
                        s=input('enter new author')
                        i[3]=s
            if u==5:
                break
            print(library)


    def delete():
        k=int(input('enter ID'))
        for i in library:
            if i[0]==k:
                library.remove(i)

    if c==1:
        create()
    if c==2:
        display()
    if c==3:
        update()
    if c==4:
        delete()














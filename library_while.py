library=[[1,'abc',77,'pqr','xyz'],[2,'two',100,'aaa','bbb']]
while True:
    print('1. Add book')
    print('2. Delete book')
    print('3.Price of Book')
    print('4. Update book')
    print('5. Display Books')


    c=int(input('Enter your Choice'))
    if c==1:
        id=int(input('Enter ID of the Book'))
        title=input('Title of Book')
        price=int(input('Enter the Price'))
        author=input('Enter Authors name')
        publisher=input('Enter Publisher')
        l=[]
        l.append(id)
        l.append(title)
        l.append(price)
        l.append(author)
        l.append(publisher)
        library.append(l)
        print('Book added')

    if c==2:

        id=int(input('Enter ID of the book'))
        for i in library:
            if id==i[0]:
                library.remove(i)



                print('Book Deleted')


    if c==3:
        id=int(input('Enter ID of book'))
        for i in library:
            if id==i[0]:
                print('price=',i[2])

    # if c==4:
    #
    #     id=int(input('Enter ID of Book'))
    #     for i in library:
    #         if id==i[0]:
    #             price=int(input('Enter updated price'))
    #             i[2]=price
    #             print('Price updated')
    #updation


    if c==4:
        while True:
            print('1.title')
            print('2.price')
            print('3.author')
            print('4.publisher')
            print('5.break')

            n=int(input('enter your choice'))

            if n==1:
                c=int(input('enter id'))
                for i in library:
                    if c==i[0]:
                        t=input('enter new title')
                        i[1]=t
            if n==2:
                c=int(input('enter id'))
                p=int(input('enter new price'))
                for i in library:
                    if c==i[0]:
                        i[2]=p
            if n==3:
                c=int(input('enter id'))
                a=input('enter author')
                for i in library:
                    if c==i[0]:
                        i[3]=a

            if n==4:
                c=int(input('enter id'))
                a=input('enter publisher')
                for i in library:
                    if c==i[0]:
                        i[4]=a

            if n==5:
                break














    if c==5:
        for i in library:
            print('ID:',i[0])
            print('Title:',i[1])
            print('Price',i[2])
            print('Author:',i[3])
            print('Publisher:',i[4])







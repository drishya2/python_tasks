from pack1.module_1 import library

def update():
    print('1.update title')
    print('2.update price')
    print('3.update author')
    print('4.update publisher')
    print('5.break')


    c=int(input('enter choice'))
    if c==1:
        k=int(input('enter key'))
        t=input('enter new title')
        for i in library:
            if i[0]==k:
                i[1]=t

    if c==2:
        k=int(input('enter key'))
        t=input('enter new price')
        for i in library:
            if i[0]==k:
                i[2]=t

    if c==3:
        k=int(input('enter key'))
        t=input('enter new author')
        for i in library:
            if i[0]==k:
                i[3]=t


    if c==4:
        k=int(input('enter key'))
        t=input('enter new publisher')
        for i in library:
            if i[0]==k:
                i[4]=t



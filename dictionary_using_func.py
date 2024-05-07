
dict={}


def create():
    x = int(input('key'))
    y = input('value')

    dict.update({x: y})


def update():
    x = int(input('enter key'))
    y = input('enter new value')

    if x in dict:
        dict[x] = y


def display():
    print(dict)


def delete():
    y = int(input('enter key'))
    del dict[y]


while True:


    print('1.create')
    print('2.update')
    print('3.display')
    print('4.delete')


    choice=int(input('enter your choice'))

    if choice==1:

        create()
        print(dict)

    if choice==2:
        update()
        print(dict)
    if choice==4:

        delete()
        print(dict)

    if choice==3:
        display()



























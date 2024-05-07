from pack1 import module_1,module_2,module_3,module_4
while True:
    print('1.add book')
    print('2.display book')
    print('3.update book')
    print('4.delete book')

    c = int(input('enter your choice'))



    if c==1:
        module_1.create()
    if c==2:
        module_2.display()
    if c==3:
        module_3.update()
    if c==4:
        module_4.delete()


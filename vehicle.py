v=[]
while True:

    print('1.add vehicle')
    print('2.display vehicle')

    c=int(input('enter your choice'))
    if c==1:
        num=input('Enter number')
        name=input('enter name')
        pr=int(input('enter price'))
        wheels=int(input('number of wheels'))
        a=[]

        a.append(num)
        a.append(name)
        a.append(pr)
        a.append(wheels)
        v.append(a)
        print(v)


    if c==2:

        while True:

            print('1. two  wheels')
            print('2. three wheels')
            print('3. four wheels')
            print('4. break')
            x=int(input('enter your choice'))


            if x==1:
                for i in v:
                    if i[3]==2:
                        print('number of vehicle is',i[0])
                        print('name of vehicle is', i[1])
                        print('price is', i[2])


            if x==2:
                for i in v:
                    if i[3]==3:
                        print('number of vehicle is',i[0])
                        print('name of vehicle is', i[1])
                        print('price is', i[2])

            if x==3:
                for i in v:
                    if i[3]==4:
                        print('number of vehicle is',i[0])
                        print('name of vehicle is', i[1])
                        print('price is', i[2])

            if x==4:
                break











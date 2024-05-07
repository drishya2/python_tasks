dict={}
while True:
    print('1.create')
    print('2.update')
    print('3.display')
    print('4.delete')

    n=int(input('enter your choice'))

    if n==1:
        r=int(input('enter range'))
        for i in range(r):
            k=int(input('enter the key'))
            v=input('enter value')
            dict.update({k:v})
        print(dict)

    if n==2:
        k=int(input('enter key'))
        if k in dict:
            u=input('enter value')
            dict[k]=u
            print(dict)
    if n==3:
        print(dict)


    if n==4:
        k=int(input('enter key'))
        if k in dict:
            del dict[k]
            print(dict)




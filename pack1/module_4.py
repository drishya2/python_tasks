from pack1.module_1 import library

def delete():
    k=int(input('enter key'))
    for i in library:
        if i[0]==k:
            library.remove(i)


    print(library)

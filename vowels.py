# n=str(input('Enter a word'))
# if 'a' in n or 'e' in n or 'i' in n or 'o' in n or 'u' in n:
#     print('Vowel is present')
# else:
#     print('Vowel is not present')



#library

l=[]
while True:
    print('1.add book')
    print('2.update')
    print('3.display')
    print('4.delete')

    c=int(input('enter your choice'))

    if c==1:
        k=[]
        book=input('title of the book')
        price=int(input('enter price'))
        author=input('enter author')
        publisher=input('enter publisher')
        k.append(book)
        k.append(price)
        k.append(author)
        k.append(publisher)
        l.append(k)
    print(l)


    if c==2:
        while True:
            print('1.title')
            print('2.price')
            print('3.author')
            print('4.publisher')







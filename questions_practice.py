# a=input('Enter first string')
# b=input('Enter second string')
# p=list(a)
# q=list(b)
# p.sort()
# q.sort()
# if p==q:
#     print('Anagram')
# else:
#     print('Not anagram')



# adding even numbers
# a=0
# s=[1,2,3,4,6,2,1,5]
# for i in s:
#     if i%2==0:
#         a=a+i
# print(a)
from collections import Counter

# name='haai'
# for i in name:
#     if name.count(i) > 1:
#         print('false')
#
#     else:
#         print('True')



n='name'
s=[]
for i in n:
    if i in s:
        print('not unique')
        break
    s.append(i)
else:
    print('unique')





















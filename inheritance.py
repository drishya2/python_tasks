#single inheritance

# class A:
#     def display(self):
#         print('Hello')
# class B(A):
#     def display2(self):
#         print('World')
#
# b=B()
# b.display()
# b.display2()




# multiple inheritance

# class A:
#     def display(self):
#         print('hello')
#
# class B:
#     def display2(self):
#         print('world')
# class C(A,B):
#     def display3(self):
#         print('welcome')
#
# c=C()
# c.display()
# c.display2()
# c.display3()




#multilevel inheritance


# class A:
#     def display(self):
#         print('hello')
# class B(A):
#     def display2(self):
#         print('world')
#
# class C(B):
#     def display3(self):
#         print('how are')
# class D(C):
#     def display4(self):
#         print('you')
#
# d=D()
# d.display()
# d.display2()
# d.display3()
# d.display4()





#hierarchial inheritance


# class A:
#     def display(self):
#         print('hello')
# class B:
#     def display2(self):
#         print('world')
# class C(A,B):
#     def display3(self):
#         print('how are you')
#
# c=C()
# c.display()
# c.display2()
# c.display3()



#hybrid inheritance


# class A:
#     def display(self):
#         print('a')
# class B(A):
#     def display2(self):
#         print('b')
# class C(A):
#     def display3(self):
#         print('c')
# class D(B,C):
#     def display4(self):
#         print('d')
# class E(C):
#     def display5(self):
#         print('e')
# class F(D,E):
#     def display6(self):
#         print('f')
#
# f=F()
# f.display()
# f.display2()
# f.display3()
# f.display4()
# f.display5()
# f.display6()



#super function

# class A:
#     def __init__(self):
#         self.x='hello'
# class B(A):
#     def __init__(self):
#         super().__init__()
#         self.y='world'
#     def display(self):
#         print(self.x)
#         print(self.y)
#
# b=B()
# b.display()


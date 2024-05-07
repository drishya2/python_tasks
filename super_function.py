class A:
    def __init__(self):
        self.x='heello'


class B(A):
    def __init__(self):
        super().__init__()
        self.y='world'

a=B()
print(a.x)
print(a.y)
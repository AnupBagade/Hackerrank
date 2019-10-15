class A:
    def __new__(cls, *args, **kwargs):
        print('inside A new')
        return super(A, cls).__new__(cls, *args, **kwargs)

    def __init__(self):
        print('inside A init')

class B(A):
    def __new__(cls, *args, **kwargs):
        print('inside B new')
        return super(B, cls).__new__(cls, *args, **kwargs)

    def __init__(self, a):
        super().__init__()
        self.a = a
        print('inside B init')


if __name__ == '__main__':
    b = B(2)
    print(b.a)
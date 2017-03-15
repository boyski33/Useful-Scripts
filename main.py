class A(object):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


a = A("Jimmy")
b = a

b.name = "Pedro"
print(str(a))

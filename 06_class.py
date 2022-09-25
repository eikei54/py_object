class MyClass:
    def __init__(self):
        self.a = 0
        b = 0

    def set_a(self, value):
        self.a = value

    def get_a(self):
        return self.a

    def set_b(self, value):
        b = value

    def get_b(self):
        return b

instance = MyClass()
instance.set_a(3)
print(instance.get_a())

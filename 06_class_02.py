class MyClass:
    #def __init__(self):
    #    self.a = 'a'
    #    self.b = 'b'

    def __init__(self):
        print(f'1:{dir(self)}')
        self.a = 'a'
        self.b = 'b'
        print(f'2:{dir(self)}')

instance = MyClass()
print(f'3:{dir(instance)}')

instance.c = 'c'
print(f'4:{dir(instance)}')


def new_method(self):
    return 'hello new method'

MyClass.new_method = new_method
print(instance.new_method())


print(f'5:{dir(instance)}')



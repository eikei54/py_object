class MyClass:
    def __init__(self):
        print('constructer')

    def method1(self, a):
        print(a)


    def method2(self):
        print(f'self type: {type(self)}')
        print(f'self ref: {self}')

instance = MyClass()

#instance.method1('hello')
print(f'instance type: {type(instance)}')
print(f'instance ref: {instance}')

print('--------------------')
instance.method2()

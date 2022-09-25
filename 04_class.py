class TestClass:
    def print0(self):
        print('0.')

    def print1(self, a, b):
        print(f'1: {a} {b}')

    def get100(self):
        return 100

instance = TestClass()
instance.print0()

instance.print1('A', 'B')

inst_a = instance.get100()
print(inst_a)

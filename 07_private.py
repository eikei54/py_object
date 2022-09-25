class TestPrivate:
    def __init__(self):
        self.var1 = 'var1'
        self.__var2 = 'var2' #PRIVATE

    def method1(self):
        print(self):


    def __method2(self):
        print('method2')



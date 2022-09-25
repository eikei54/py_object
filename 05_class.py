class UserInfo:
    def __init__(self):
        print('initialize instance') # HERE
        self.name = ""
        self.birth = 0
        self.address = ""

    def __init__(self, name, birth, address):
        self.name = name
        self.birth = birth
        self.address = address


taro = UserInfo('taro', 1980, 'tokyo')


print(taro.name)
print(taro.birth)
print(taro.address)



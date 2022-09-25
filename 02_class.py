class UserInfo:
    def __init__(self):
        self.name = 'Unknown'
        self.birth = 0
        self.address = 'Unknown'


taro = UserInfo()
taro.name = 'Taro'
taro.birth = 1986
taro.address = 'Tokyo'

print(f'{taro.name} {taro.birth} {taro.address}')


unknown_instance = [1, 2, 3]
print(type(unknown_instance))
print(unknown_instance)

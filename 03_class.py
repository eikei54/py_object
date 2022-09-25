class Score:
    def __init__(self):
        self.name = 'Unknown'
        self.math = 0
        self.english = 0
        self.japanese = 0

    def get_average(self):
        return (self.math+self.english+self.japanese)/3

taro = Score()
taro.math = 85
taro.english = 90
taro.japanese = 80

ave=taro.get_average()
print(ave)
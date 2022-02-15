# MoreCalculator
from day30.class_lib.calculator import Calculator

class MoreCalculator(Calculator):
    # pass
    def div(self):   #메서드 재정의(오버라이딩-overriding)
        if self.y == 0:
            return 0         # 0으로 리턴
        else:
            return self.x / self.y

    def pow(self):
        return self.x ** self.y


cal = MoreCalculator(10, 4)
print(cal.div())
print(cal.pow())

# 0으로 나눌 때 에러를 처리해 준다.
cal2 = MoreCalculator(10, 0)
print(cal2.div())
print(cal2.pow())
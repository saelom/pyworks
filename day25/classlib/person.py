# 정보 은닉(Information Hide)
# 언더스코어가 1개(_) 또는 2개(__)가 있으면 멤버 접근 불가(pricate 속성으로 변함)
class Person:
    def __init__(self):
        self._name = ""
        self._age = 0

p1 = Person()
#p1. 멤버 변수에 접근 불가
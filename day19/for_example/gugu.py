# 구구단 출력
"""
dan = 7
for i in range(1, 10):
    print(dan, 'x', i, '=', (dan * i))
"""

"""
# 단을 입력받아서 구구단 출력
dan = int(input("단 입력 : "))
for i in range(1, 10):
    print(dan, 'x', i, '=', (dan * i))
"""

"""
print("단 입력 : ")
dan = int(input())
for i in range(1, 10):
    print(dan, 'x', i, '=', (dan * i))   
"""


dan = int(input("단 입력 : "))
for i in range(1, 10):
    print("{} x {} = {}".format(dan, i, dan *i))
    

import sys
#args 대신 다른 거 써도 가능
args = sys.argv[1:]

total = 0
for i in args:
    total += int(i)   # 입력받은 문자를 숫자로 변환

print(total)

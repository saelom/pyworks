import random as r

# 컴퓨터가 1~100 중 난수를 저장
com = r.randint(1, 100)
min_v = 1
max_v = 100

for i in range(10):
    guess = int(input("맞혀 보세요([%d회] %d ~ %d) :" % (i+1, min_v, max_v)))  #숫자로 입력
    # 정답일 때 "정답", guess가 클 때 "너무 커요", 아니면 "너무 작아요"
    if com == guess:
        print("정답")
        break
    elif com < guess:
        print("너무 커요.")
        max_v = guess   #최대값 변경
    else:
        print("너무 작아요.")
        min_v = guess   #최소값 변경

print("점수 : %d점" % ((10-i)*10))
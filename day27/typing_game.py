# 영어 타자 게임
import random
import time
"""
word = ['sky', 'earth', 'moon', 'flower', 'tree',
        'strawberry', 'grape', 'garlic', 'onion']
"""
try:

    # 외부의 word.txt 읽기
    f = open("./output/word.txt", 'r')
    word = f.read().split()


    n = 1        # 문제 번호
    print('[타자 게임] 준비 되면 엔터')
    input()
    start = time.time()       #게임 시작 시간
    while n < 11:
        print("문제", n)
        question = random.choice(word)  # 문제
        print(question)
        answer = input()    # 사용자가 입력

        # if문 처리
        if question == answer:
            print("통과!")
            n += 1   #다음 문제
        else:
            print("오타! 다시 도전!")

     # n += 1  ( 딱 10문제만 풀 수 있다. )
    end = time.time()    # 게임 끝난 시간
    print("타자 시간 : %.2f 초" % (end - start))
except:
 print("파일을 열 수 없습니다.")
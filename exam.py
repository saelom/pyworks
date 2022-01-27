#파이썬 시험

#입장객 수에 따른 줄 수 계산
customer = int(input("입장객 수 : "))
col = int(input("열의 수 : "))

if customer % col == 0:
    #row = int(customer / col)
    row = customer // col
else:
    row = int(customer / col) + 1

print("줄 수 : " ,row)


#평균 구하기
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

total = 0
for score in A:
    total += score

print(len(A))
average = total / len(A)        #평균 = 합계 / 개수
print (average)


total = 0
for score in A:
    total += score

print(len(a))
average = total /len(A)

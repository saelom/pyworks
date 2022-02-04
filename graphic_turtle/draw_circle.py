import turtle as t

t.setup(500, 500)   # 무대의 크기
t.bgcolor('black')  # 배경 색
t.color('yellow')   # 선 색
t.pensize(2)

n = 50
t.speed(0)   # 속도 1~10, 0이 가장 빠름
for x in range(n):
    t.circle(80)
    t.left(360 / n)

t.mainloop()
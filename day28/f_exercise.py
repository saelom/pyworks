# p180 / Q5
f1 = open("./output/test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("./output/test.txt", 'r')
print(f2.read())
f2.close()

#6
"""
user_input = input("저장할 내용을 입력하세요: ")
f = open('./output/test3.txt','a')
f.write(user_input)
f.write('\n')
f.close()
"""

#7
with open('./output/test4.txt','w') as f1:
    f1.write("Life is too short. \n you need java")

with open('./output/test4.txt','r') as f1:
    body = f1.read()

body = body.replace('java', 'python')

with open('./output/test4.txt','w') as f2:
    f2.write(body)


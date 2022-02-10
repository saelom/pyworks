# 파일 쓰기 - 파일 생성( p. 171 )

# 파일 열기 - open(경로, 모드)
f = open("c:/pyfile/test.txt", 'a')   # 'a' 는 추가 모드

# 파일 쓰기
f.write("안녕하세요\n")


# 파일 닫기
f.close()
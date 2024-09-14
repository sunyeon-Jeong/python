'''
author : mallang
createdAt : 2024.09.14
'''
# 파일 생성하기
f = open("fileCreate.txt", 'w')
f.close()

'''
- 'r' : 읽기모드. 파일을 읽기만 할 때 사용
- 'w' : 쓰기모드. 파일에 내용을 쓸 때 사용
- 'a' : 추가모드. 파일의 마지막에 새로운 내용을 추가할 때 사용
'''

# 파일 내용작성
f = open("/Users/sunyeonjeong/dev/github/python/fileCreate.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)
f.close()

# 파일 읽는 방법
'''readline 함수'''
f = open("/Users/sunyeonjeong/dev/github/python/fileCreate.txt", 'r')
line = f.readline()
print(line)
f.close()

f = open("/Users/sunyeonjeong/dev/github/python/fileCreate.txt", 'r')
while True:
    line = f.readline()
    
    if not line: break
    
    print(line)
    
f.close()

'''readlines 함수 : 파일의 모든 줄을 읽어서 각각의 줄을 요소로 가지는 리스트를 리턴'''
f = open("/Users/sunyeonjeong/dev/github/python/fileCreate.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

'''read 함수 : 파일 내용 전체를 문자열로 리턴'''
f = open("/Users/sunyeonjeong/dev/github/python/fileCreate.txt", 'r')
data = f.read()
print(data)
f.close()

'''파일 객체 for문과 함께 사용'''
f = open("/Users/sunyeonjeong/dev/github/python/fileCreate.txt", 'r')
for line in f:
    print(line)
f.close()

# 파일에 새로운 내용 추가하기
f = open("/Users/sunyeonjeong/dev/github/python/fileCreate.txt", 'a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)
f.close()

# 파일 열고닫기 자동처리하기
'''
with문을 사용하면 with 블록을 벗어나는 순간, 열린 파일 객체 f가 자동으로 닫힘
'''
f = open("fileAuto", 'w')
f.write("Life is too short. you need python")
f.close()

with open("fileAuto", 'w') as f:
    f.write("Life is too short, you need python")
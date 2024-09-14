'''
author : mallang
createdAt : 2024.09.14
'''
# 사용자 입력 활용
'''input 사용 : 사용자가 키보드로 입력한 모든것을 문자열로 저장함'''
a = input()
a

'''프롬프트 띄워 사용자 입력받기'''
num = input("값을 입력하세요: ")
print(num)
type(num) # -> input에 입력되는 모든 값은 문자열로 취급

# print
'''문자열 쉼표로 띄어쓰기'''
print("life", "is", "too short")

'''한줄에 결과값 출력하기'''
for i in range(10):
    print(i, end = ' ') # end 매개변수의 초기값은 줄바꿈 문자임(\n)
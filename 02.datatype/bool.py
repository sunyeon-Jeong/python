'''
author : mallang
createdAt : 2024.09.08
'''

# 불 자료형
'''
- True/False 값만 가질 수 있음
- 파이썬의 예약어로 첫글자 대문자 필수
'''

a = True
b = False
type(a)
type(b)

2 > 1
1 > 2

# 자료형의 참과 거짓
'''
- 문자열, 리스트, 튜플, 딕셔너리 등의 값이 empty -> False
- 숫자형의 경우 0 또는 None -> False
'''

a = [1, 2, 3, 4]
while a:
    a.pop()

# 불 연산
bool('python')
bool('')
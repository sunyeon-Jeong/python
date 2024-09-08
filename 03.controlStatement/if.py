'''
author : mallang
createdAt : 2024.09.08
'''

# if문
'''
- 조건을 판단하여(True or False) 해당 조건에 맞는 수행하는데 사용
  if 조건문:
    수행1 -> 조건문 True
    수행2 -> 조건문 True
  else:
    수행a -> 조건문 False
    수행b -> 조건문 False
- if문 뒤에는 반드시 콜론(:) 붙일 것
'''

money = True
if money:
    print("택시 타고 집가기")
else:
    print("걸어 가기")

money = 2000
if money >= 3000:
    print("택시")
else:
    print("도보")

'''
- 비교연산자 : <, >, <=, >=, ==, !=
- or, and, not
'''

# Q1.돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 그렇지 않으면 걸어가라
money = 2000
card = True
if money >= 3000 or card:
    print("택시")
else:
    print("도보")
    
# x in s, x not in s
'''
- x in 리스트, x not in 리스트
- x in 튜플, x not in 튜플
- x in 문자열, x not in 문자열
'''
1 in [1, 2, 3]
1 not in [1, 2, 3]

'a' in ('a', 'b', 'c')
'a' not in ('a', 'b', 'c')

# Q2. 만약 주머니에 돈이 있으면 택시, 없으면 도보
pocket = ['paper', 'phone', 'money']
if 'money' in pocket:
    print("택시")
else:
    print("도보")
    
# Q3. 주머니에 돈이 있으면 가만히 있고, 주머니에 돈이 없으면 카드를 꺼내라
pocket = ['paper', 'money', 'phone']
if 'money' in pocket:
    pass
else:
    print("카드 꺼내기")
    
# elif문 (다중 조건 판단)
'''
- elif 개수 제한 없이 무한 사용 가능
- 마지막 조건문에는 else 필수사용
'''
pocket = ['paper', 'phone']
card = True
if 'money' in pocket:
    print("택시")
elif card:
    print("택시")
else:
    print("도보")
    
# 조건부 표현식
score = 79

if score >= 60:
    message = "success"
else:
    message = "failure"
    
print(message)

message = "success" if score >= 60 else "failure"
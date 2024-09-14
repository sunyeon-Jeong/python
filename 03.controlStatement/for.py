'''
author : mallang
createdAt : 2024.09.10
'''

# for문
'''
- 리스트, 튜플, 문자열의 첫번째 요소부터 마지막요소까지 차례로 변수에 대입하여 수행

- for 변수 in 리스트/튜플/문자열:
    수행1
    수행2
'''

test_list = ['one', 'two', 'three'] # 리스트
for i in test_list:
    print(i)
    
a = [(1, 2), (3, 4), (5, 6)] # 튜플
for (first, last) in a:
    print(first + last)
    
score = [90, 25, 67, 45, 80]
student_num = 0
for grade in score:
    student_num += 1
    
    if grade >= 60:
        print("%d번째 학생은 합격입니다." %student_num)
    
    else:
        print("%d번째 학생은 불합격입니다." %student_num)
        
# for문과 continue문
scores = [90, 25, 67, 45, 80]
student_num = 0
for score in scores:
    student_num += 1
    
    if score < 60 : continue
    print("%d번 학생 축하합니다. 합격입니다." %student_num)
    
# for문과 range함수
'''
- range 함수 : 숫자 리스트를 자동으로 만들어주는 함수
- range(이상, 미만)
'''
a = range(10)
a # -> 1이상 10미만의 숫자를 포함하는 객체 생성

a = range(1, 11)
a

add = 0
for i in range(1, 11):
    add += i # -> 1부터 10까지의 숫자를 계속 더하는 형태
print(add)

add = 0
for i in range(1, 101):
    add += i
print(add)

for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end=" ")
    print('')

# 리스트 포함(리스트에 for문을 포함)
nums = [1, 2, 3, 4]
result = []

for num in nums:
    result.append(num * 3) # append() : 리스트 마지막 요소에 값 삽입하는 함수

print(result)

# 리스트 컴프리헨션
'''
[포현식 for 항목 in 반복_가능_객체 if 조건문]
'''
a = [1, 2, 3, 4]
result = [num * 3 for num in nums] # [수행 + for문]
print(result)

a = [1, 2, 3, 4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)

result = [x * y for x in range(2,10) for y in range(1,10)]
print(result)
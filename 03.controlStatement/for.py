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
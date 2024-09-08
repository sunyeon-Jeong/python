'''
author : mallang
createdAt : 2024.09.08
'''

# 문자열
"Hello World"
'python is fun'
"""Life is too short. You need python"""
'''Life is too short. You need python'''

# 문자열 안에 따옴표 포함
"Python's favorite food is mango"
food = "Python's favorite food is mango"
food

mallang = "Mallang said \'I want to be a backend developer\'."
mallang

# 줄바꿈
multiline = "Life is too short\nYou need python"
print(multiline)

# 문자열 연산 (더하기)
head = "Python"
tail = " is fun"
head + tail

# 문자열 연산 (곱하기)
a = "Python"
a * 2
"Python" * 2

print("=" * 50)
print("My Program")
print("=" * 50)

# 문자열 길이 구하기
a = "Life is too short"
len(a)

# 문자열 인덱싱 (지정해서 추출)
a = "Life is too short, You need Python"
a[3]
a[-0] # a[0]과 같은 결과값
a[-1] # 역순은 1부터 시작


# 문자열 슬라이싱 (지정해서 잘라냄_~이상, ~미만)
a[0:5]
a[0:]

# 문자열 요소 변경
'''
파이썬 문자열 요소값은 바꿀 수 없음.
즉, 인덱싱 기법으로 꺼내어 요소 변경이 불가능.
슬라이싱 기법으로 구분하여 요소값 변경은 가능.
'''
a = "Pyihon"
a[:2] + 't' + a[3:]

# 문자열 포맷팅 : 문자열 안의 특정한 값을 변경하면서 쓸때 
'''
정수형 : %d, 실수형 : %f, 문자열 : %s, 문자1개 : %c
%s로 모두 커버 가능하지만, 자동으로 %뒤에 있는 값이 문자열로 바뀐다.
'''
"I eat %d apples." %3 # %d -> 숫자형

"I eat %s apples." %"five" # %s -> 문자형

number = 3
"I eat %d apples." %number # 변수형

number = 10
day = "three"
"I ate %d apples. so I was sick for %s days." %(number, day)

"Error is %d%%" %98

# 포맷코드 정렬과 공백
'''
%포맷코드 사이 숫자 : 전체길이
+숫자 : right정렬
-숫자 : left정렬
'''
"%10s" %"hi"
"%-10s" %"hi"
"%-10smallang" %"hi"

# 소수점 표현하기
"%0.4f" %3.141592 # '소수점아래 4자리까지'
"%10.4f" %3.141592 # right 정렬
"%-10.4f" %3.141592 # left 정렬

# format 함수 포맷팅
"I eat {0} apples.".format(3)
"I eat {0} apples.".format("five")
number = 3
"I eate {0} apples.".format(number)

number = 10
day = "three"
"I ate {0} apples. so I was sick for {1} days.".format(number, day)

"I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3)

# f 문자열 포맷팅
'''
변수값을 선 생성한 후에 그 값을 참조
표현식을 지원함 (변수 및 수식어)
'''
name = 'mallang'
age = 23
f'나의 이름은 {name}입니다. 나이는 {age}입니다.'

age = 23
f'나는 내년이면 {age+1}살이 된다.'

d = {'name' : 'mallang', 'age' : 23}
f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.'

# 문자열 관련 내장함수
'''문자열 중 특정문자 개수 세기'''
a = "hobby"
a.count('b')

'''위치 알려주기(find) -> 존재하지 않으면 -1 반환'''
a = "Python is the best choice"
a.find('b')
a.find('k')

'''위치 알려주기(index) -> 존재하지 않으면 오류 발생'''
a = "Life is too short"
a.index('t')
a.index('k')

'''문자열 삽입(join) -> 공백 없게 하면 이어붙이기로 응용 가능'''
",".join('abcd')

'''소문자 -> 대문자'''
a = "hi"
a.upper()

'''대문자 -> 소문자'''
a = "HI"
a.lower()

'''왼쪽 공백 지우기(lstrip)'''
a = "   hi"
a.lstrip()

'''오른쪽 공백 지우기(rstrip)'''
a = "   hi   "
a.rstrip()

'''양쪽 공백 지우기(strip)'''
a = "   mallang   "
a.strip()

'''문자열 바꾸기(replace)'''
a = "Life is too short"
a.replace("Life", "Your leg")

'''문자열 나누기 : 문자열 split -> 리스트형으로 변환'''
a = "Life is too short"
a.split()
b = "a:b:c:d"
b.split(':')
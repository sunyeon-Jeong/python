'''
author : mallang
createdAt : 2024.09.14
'''

# 함수
'''
def 함수_이름(매개변수):
    수행할_문장1
    수행할_문장2
'''
def add(a, b):
    return a + b

a = 3
b = 4
c = add(a, b)
print(c)

# 매개변수와 인수
'''
- 매개변수(parameter) : 함수에 입력으로 전달된 값을 받는 변수
- 인수 : 함수를 호출할때 전달하는 입력값
'''
def add(a, b): # a, b -> 매개변수
    return a + b

print(add(3, 4)) # 3, 4 -> 인수

# 일반함수
'''
def 함수_이름(매개변수):
    수행할_문장
    return 리턴값
'''
def add(a, b):
    result = a + b
    return result

a = add(3, 4)
print(a)

# 입력값이 없는 함수
def say():
    return "HI, MALLANG"

a = say()
print(a)

# 리턴값이 없는 함수
def add(a, b):
    print("%d, %d의 합은 %d 입니다." %(a, b, a+b))

add(3, 4)

# 입력값, 리턴값 모두 없는 함수
def say():
    print("HI, MALLANG")

say()

# 매개변수를 지정하여 호출하기
def sub(a, b):
    return a - b

result = sub(a=7, b=3)
print(result)

# 입력값(매개변수)이 여러개일 경우
'''
def 함수_이름(*매개변수):
    수행할_문장

-> 매개변수 앞에 *를 붙이면, 입력값을 모두 모아 튜플로 변경 후 for문에 대입
'''
def add_many(*args):
    result = 0
    
    for i in args:
        result += i
        
    return result

result = add_many(1, 2, 3)
print(result)

result = add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        
        for i in args:
            result += i
    
    elif choice == "mul":
        result = 1
        
        for i in args:
            result *= i
    
    return result

result = add_mul('add', 1, 2, 3, 4, 5)
print(result)

result = add_mul('mul', 1, 2, 3, 4, 5)
print(result)

# 키워드 매개변수
'''
- 키워드 매개변수 사용 시 매개변수 앞에 ** -> 2개 붙임
- (**매개변수) : 매개변수는 딕셔너리가 되고, 모든 Key=Value 형태의 입력값이 딕셔너리에 저장
'''

def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)

print_kwargs(name = "mallang", age = 23)

# 함수의 리턴값은 언제나 하나
def add_and_mul(a, b):
    return a+b, a*b

result = add_and_mul(3, 4) # 리턴값은 하나로, 튜플값으로 리턴됨
print(result)

result1, result2 = add_and_mul(3, 4)
print(result1, result2) # 리턴값은 각각 하나씩

def add_and_mul(a, b):
    return a+b
    return a*b # 함수는 리턴문을 만나는 순간 빠져나감. 즉, 실행 X

result = add_and_mul(2, 3)
print(result)

# return 단독 사용
def say_mallang(arg):
    if arg == "developer":
        return
    
    print("나는 %s 입니다." %arg)
    
say_mallang("mallang")
say_mallang("developer")

# 매개변수에 초기값 미리 설정하기
def say_myself(name, age, woman=True):
    print("나의 이름은 %s 입니다." %name)
    print("나이는 %d살 입니다." %age)
    
    if woman:
        print("여자")
    else:
        print("남자")

say_myself("정선연", 23)
say_myself("정선연", 23, False)

# 함수 안에서 선언한 변수의 효력범위
a = 1
def vartest(a):
    a += 1

vartest(a)
print(a)

# 함수 안에서 함수 밖의 변수를 변경하는 방법
a = 1
def vartest(a):
    a += 1
    return a
a = vartest(a)
print(a)

# global
a = 1
def vartest():
    global a # 함수안에서 함수밖의 a변수를 직접 사용 (-> 종속성 이슈)
    a = a+1
vartest()
print(a)
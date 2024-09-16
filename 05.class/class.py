'''
author : mallang
createdAt : 2024.09.14
'''
result = 0
def add(num):
    global result # 이전에 계산한 결과값을 유지하기 위해 전역변수 사용
    
    result += num
    
    return result

print(add(3))
print(add(4))

# 결과값을 각각 유지하는 함수
result1 = 0
result2 = 0

def add1(num):
    global result1
    result1 += num
    return result1

def add2(num):
    global result2
    result2 += num
    return result2

print(add1(3))
print(add1(4))
print(add2(3))
print(add2(7))

# 클래스
class Calculator:
    def __init__(self):
        self.result = 0
        
    def add(self, num):
        self.result += num
        return self.result
    
    def sub(self, num):
        self.result -= num
        return self.result

cal1 = Calculator() # 객체1
cal2 = Calculator() # 객체2

print(cal1.add(3))
print(cal2.add(3))
print(cal1.add(4))
print(cal2.add(4))

class Cookie:
    pass

a = Cookie()
b = Cookie()

'''self 매개변수 = 객체'''
class FourCal:
    # 객체에 연산할 숫자 지정하는 메서드
    def setdata(self, first, second):
        self.first = first
        self.second = second
        
    # 덧셈 메서드
    def add(self):
        result = self.first + self.second
        return result
    
    # 뺄셈 메서드
    def sub(self):
        result = self.first - self.second
        return result
    
    # 곱셈 메서드
    def mul(self):
        result = self.first * self.second
        return result
    
    # 나눗셈 메서드
    def div(self):
        result = self.first / self.second
        return result
    
a = FourCal()
b = FourCal()

a.setdata(4, 2)
b.setdata(3, 8)

a.first

a.add()
a.sub()
a.mul()
a.div()

b.add()
b.sub()
b.mul()
b.div()

# 생성자 (Constructor)
'''
- 클래스 내 메서드 호출을 통해 초깃값을 설정하는 것보다 생성자 구현이 더 안전한 방법
- 생성자 : 객체가 생성될 때 자동으로 호출되는 메서드
- __init__을 메서드명으로 사용
'''
class FourCal:
    # 생성자
    def __init__(self, first, second):
        self.first = first
        self.second = second
        
    # 객체에 연산할 숫자 지정하는 메서드
    def setdata(self, first, second):
        self.first = first
        self.second = second
        
    # 덧셈 메서드
    def add(self):
        result = self.first + self.second
        return result
    
    # 뺄셈 메서드
    def sub(self):
        result = self.first - self.second
        return result
    
    # 곱셈 메서드
    def mul(self):
        result = self.first * self.second
        return result
    
    # 나눗셈 메서드
    def div(self):
        result = self.first / self.second
        return result
    
a = FourCal(4, 2)
a.add()

# 클래스 상속
'''
- class 클래스명(상속할 클래스명)
- A클래스를 B가 상속받으면, B는 A클래스의 모든 기능을 사용할 수 있음
- 기존 클래스는 유지하면서 클래스 기능을 확장할 때 사용
'''
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(4, 2)
a.add()
a.mul()
a.sub()
a.div()
a.pow()

# 메서드 오버라이딩
'''
- 부모클래스에 있는 메서드를 동일한 이름으로 다시 만드는 것(+ 수정)
- 오버라이딩 이후에는 부모클래스 메서드 대신, 오버라이딩한 메서드가 호출됨
'''
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second
        
# 클래스 변수
'''
- 메서드 변수와 달리 클래스 변수는 해당 클래스로 만든 모든 객체에 공유됨
'''
class Family:
    lastname = "Kim"
    
Family.lastname

a = Family()
b = Family()

a.lastname
b.lastname
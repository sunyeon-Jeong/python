'''
author : mallang
createdAt : 2024.09.10
'''

# while문
'''
- 반복해서 문장을 수행해야 할 경우 사용
- while문은 조건문이 참일 동안에 반복해서 수행
- 조건문이 거짓이 되면 다음으로 넘어감
- while 조건문:
    수행1
    수행2
    수행3
'''

treeHit = 0
while treeHit < 10:
    treeHit += 1
    print("나무를 %d번 찍었습니다." %treeHit)
    
    if treeHit == 10:
        print("나무 넘어갑니다.")
        
# 여러 선택지 중 하나를 선택해서 입력받는 예제
prompt = """
    1. Add
    2. Del
    3. List
    4. Quit
    
    Enter number : """
    
number = 0
while number != 4:
    print(prompt)
    number = int(input()) # -> 사용자 입력값
    
# while문 강제로 빠져나가기(break문)
coffee = 10
money = 300

while money:
    print("돈을 받았으니 커피를 줍니다")
    
    coffee -= 1
    print("남은 커피의 양은 %d 입니다." %coffee)
    
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

coffee = 10
while True:
    money = int(input("돈을 넣어주세요 : "))
    
    if money == 300:
        print("커피 제공")
        coffee -= 1
        
    elif money > 300:
        print("거스름돈 %d를 주고, 커피를 줍니다." %(money - 300))
        coffee -= 1
    
    else:
        print("돈을 다시 돌려주고, 커피를 제공하지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." %coffee)
    
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
    
# while문의 처음으로 돌아가기(continue)
'''
- 조건문이 F일 경우, 다음으로 넘어가지 않고
- while문의 맨 처음 조건문으로 다시 돌아가게 함
'''
a = 0
while a < 10:
    a += 1
    
    if a % 2 == 0 : continue # 2의 배수일경우 다음으로 넘어가지 않고 다시 처음으로 돌아감
    
    print(a)
    
a = 0
while a < 10:
    a += 1
    
    if a % 3 == 0 : continue
    
    print(a)

# 무한루프
'''
- 파이썬에서 무한루프는 while문으로 구성
- while문의 조건문이 항상 True
- ctrl + c를 통해 나갈 수 있음
'''
while True:
    print("Ctrl + C로 While문을 탈출하세요.")
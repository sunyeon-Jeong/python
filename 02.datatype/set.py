'''
author : mallang
createdAt : 2024.09.08
'''

# 집합 자료형
'''
- 중복을 허용하지 않음 (출력값에 중복되는 요소는 1개로 반환)
- 순서가 없음 -> 인덱싱을 통해 자료형의 값을 얻을 수 없음
  * 리스트, 튜플 : 순서 O, 인덱싱 O
  * 딕셔너리, 집합 : 순서 X, 인덱싱 X
'''
s1 = set([1, 2, 3])
s1

s2 = set("Hello")
s2

s1 = set([1, 2, 3])
l1 = list(s1) # 집합형을 리스트로 변환
l1

t1 = tuple(s1)
t1
t1[0]

# 교집합(&)
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

s1 & s2

# 합집합(|)
s1 | s2
s1.union(s2)

# 차집합(-)
s1 - s2
s2 - s1
s1.difference(s2)
s2.difference(s1)

# 값 한개 추가하기(add)
s1 = set([1, 2, 3])
s1.add(4)
s1

# 값 여러개 추가하기(update)
s1 = set([1, 2, 3])
s1.update([4, 5, 6])
s1

# 특정 값 제거하기(remove)
s1 = set([1, 2, 3])
s1.remove(2)
s1
'''
author : mallang
createdAt : 2024.09.08
'''

# 딕셔너리
'''
- key : value
- 리스트나 튜플처럼 순차적으로 요소값을 요구하지 않고, key를 통해서 value를 얻음
- key는 변하지 않는 값
- value는 변하지 않는 값 or 변하는 값 모두 가능
- key는 고유한 값으로 중복되는 값 설정시 나머지 것들이 모두 무시됨
- key에 리스트 사용 X, 튜플은 (불변이므로) 사용 O
'''

# 딕셔너리 쌍 추가 / 삭제
'''
{key1 : value1} 추가하고 싶으면
딕셔너리변수명[key1] = value1
'''
a = {1: 'a'}
a[2] = 'b'
a['name'] = 'mallang'
a

del a[1] # -> 제거할 쌍의 key값 입력

# key값을 사용해 value 얻기 -> 리스트/튜플/문자열은 인덱싱 or 슬라이싱, 딕셔너리는 Key값으로
grade = {'mallang' : 'A', 'potato' : 'B'}
grade['mallang']

# 딕셔너리 관련 함수
'''key 리스트 만들기'''
a = {'name' : 'mallang', 'phone' : '01011112222', 'birth' : '020412'}
a.keys() # -> 리스트 형태의 객체(dict_keys)를 반환하지만, 리스트 고유 함수는 사용불가
list(a.keys())

'''value 리스트 만들기'''
a.values()
list(a.values())

'''key, value 쌍 얻기(items) -> 튜플로 반환'''
a.items()

'''key, value 쌍 모두 지우기(clear)'''
a.clear()
a

'''key로 value 얻기(get)'''
a = {'name' : 'mallang', 'phone' : '01011112222', 'birth' : '020412'}
a.get('name')
a.get('potato') # -> 아무값도 반환하지 않음
a.get('potato', 'NONE') # -> 반환할 값이 없으면 내가 지정한 값을 반환하도록 함

'''해당 key가 딕셔너리 안에 있는지 조사(in) -> boolean으로 반환됨'''
a = {'name' : 'mallang', 'phone' : '01011112222', 'birth' : '020412'}
'name' in a
'grade' in a
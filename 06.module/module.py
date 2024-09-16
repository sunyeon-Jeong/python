'''
author : mallang
createdAt : 2024.09.16
'''
# 모듈
'''
- 모듈 : 함수, 변수, 클래스를 모아놓은 파이썬 파일
- 다른 파이썬 프로그램에서 불러와 사용할 수 있음
'''

'''
맥 터미널로 본 경로에 직접 들어와 python 실행
'''
import mod1
print(mod1.add(3, 4))
print(mod1.sub(4, 2))

from mod1 import add
add(3, 4)

from mod1 import sub
sub(4, 2)

from mod1 import add, sub
from mod1 import *

import mod2
print(mod2.PI)
a = mod2.Math()
print(a.solv(2))

# sys.path.append 사용하기
''' 터미널
>>> import sys
>>> sys.path
>>> sys.path.append("경로")
'''
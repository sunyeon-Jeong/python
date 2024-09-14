'''
author : mallang
createdAt : 2024.09.14
'''
# sys 모듈 사용
'''
- sys모듈 -> 프로그램에 인수를 전달 가능
- sys모듈 사용을 위해서는 import 명령어 사용 필수
'''

import sys

args = sys.argv[1:]

for i in args:
    print(i)
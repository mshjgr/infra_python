# Step04_Str3.py
# yaml 형식의 문자열 다루기

# yaml 문자열을 다룰때는 외부 모듈을 pip 로 설치를 해서 import 를 해야한다.
# python 가상환경을 구성하고  pip install  pyyaml  설치후에  yaml 을 다룰수 있다.
import yaml

info = '''
name: 키티
addr: 강원도
foods:
  - 삼겹살
  - 김밥
iswoman: true
body:
  weight: 10
  height: 20
'''
# 검색 혹은 ai 의 도움을 받아서  info 에 들어 있는 문자열을 dict type 으로 바꾸세요
# 그런 다음 dict 에 들어 있는 내용을 확인후 다시 dict 에 있는 내용을 이용해서  yaml 문자열 형식으로 변환해보세요.

# yaml 형식의 문자열을 로딩해서 dict type 으로 변경하기
result = yaml.safe_load(info)

print(result)

# result(dict type) 을 다시 yaml 형식으로 변환하기
result2=yaml.dump(result, allow_unicode=True, sort_keys=False)

print(result2)

print("종료 합니다")
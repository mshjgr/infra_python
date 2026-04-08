#step04_str2.py
'''
    여러분의 이름과, 주소, 좋아하는 음식 2가지를 작성해서 챗팅창에 올려보세요
    json, xml, yaml ...
    json은 javascript객체 표기법을 따르는 문서 형식이다
    {
        "name":"키티",
        "addr":"강원도"
        "foods":["삼겹살","김밥"]
    }
'''
#json 모듈 import 하기
import json

#info는 str type 이긴 한데 문자열이 특별한 형식(json)을 띄고있다
info='''{
        "name":"키티",
        "addr":"강원도",
        "foods":["삼겹살","김밥"]
}'''

#result는 str(json형식)의 문자열이 python 의 dict로 변경된 값을 가지고 있다
result=json.loads(info)

print(result["name"])
print(result["addr"])
print(result["foods"])
print(result["foods"][0])
print(result["foods"][1])

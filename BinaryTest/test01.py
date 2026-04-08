# BinaryText/test01.py

# python 에서 2 진수 다루기

# 2진수는 숫자를 만들때 prefix 로 0b 
num1 = 0b1010 # 10 진수로 환산했을때 10 이된다

result = num1+5
print(result)

# 10 진수를 2진수로 변환
num2 = 150 
result2:str = bin(num2) # bin() 함수 호출하면서 10진수를 넣어주면 2 진수 숫자 값이 나온다. 
print(result2)

print("-------")

line = "abcde12345"

print(line[5:10]) # 5번 인덱스 이상, 10번 인덱스 미만 인덱스의 문자열 얻어내기

# 위의 result2 문자열에서 (0bxxxx) 에서 0b 를 제거한 순수 2진수 형태의 문자열만 얻어내려면?
print(result2[2:])    
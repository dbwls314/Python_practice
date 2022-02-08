# 02. 파이썬 변수
# 15 type 함수
a = 128
print(type(a)) # <class 'int'>

a = "132"
print(type(a)) # <class 'str'>

print("-"*20)
# 16 문자열 -> 정수 변환
num_str = "720" 
print(type(num_str)) # <class 'str'>
print(type(int(num_str))) # <class 'int'>

print("-"*20)
#17 정수 -> 문자열 100 변환
num = 100
print(type(num)) # <class 'int'>
print(type(str(num))) # <class 'str'>

print("-"*20)
#18 문자열 -> 실수 변환
float_num = "15.79"
print("float_num :",type(float(float_num))) # <class 'float'>

print("-"*20)
# 19 문자열 -> 정수 변환
year = "2022"
print("year :", int(year)) # 2022
print("year - 1 :", int(year) - 1) # 2021
print("year - 2 :", int(year) - 2) # 2020

print("-"*20)
# 20 파이썬 계산
month_cost = 48584
total_cost = month_cost * 36
print("total_cost :", total_cost)

print("-"*20)
# 03. 파이썬 문자열
# 21 문자열 인덱싱 -> 첫번째, 세번쨔 문자 출력
letters = 'python'
print("letters 첫번째, 세번째 :", letters[0], letters[2])
# print("letters 세번쨰 : ", letters[2])

print("-"*20)
# 22 문자열 슬라이싱 -> 자동차 뒤 4자리만 출력
license_plate = "24가 2210"
print("license_plate 뒤 4자리 :", license_plate[-4:])
print("license_plate 뒤 4자리 :", license_plate[4:])

print("-"*20)
# 23 문자열 인덱싱 -> '홀'만 출력 :: [start:end:간격]
string = "홀짝홀짝홀짝"
print("홀만출력 :", string[::2])

print("-"*20)
# 24 문자열 슬라이싱 -> 문자열 거꾸로 출력
string = "PYTHON"
print("string 거꾸로 :", string[::-1])

# +) 파이썬 제공 함수
# (reversed(뒤집을 문자열) :: 문자열에서 사용가능 / reverse(뒤질을 list 타입) :: 문자열X, list 가능 )
# print("reversed 객체 :",reversed(string))
# print("reversed() 결과 :", ''.join(reversed(string)))

print("-"*20)
# 25 문자열 치환 -> 하이픈('-') 제거하고 출력
phone_number = "010-1111-2222"
print(phone_number.replace('-', " "))

print("-"*20)
# 26 문자열 다루기 -> 공백 제거하고 출력
print(phone_number.replace('-', ""))

print("-"*20)
# 27 문자열 다루기 -> url에서 도메인만 출력하기
url = "http://sharebook.kr"
print(url.split('.')[1])
print(url.split('.')[-1])

print("-"*20)
# 28 문자열은 immutable
# lang = 'python'
# lang[0] = 'P'
# print(lang)

print("-"*20)
#29 replace 메서드 -> 소문자 => 대문자 변경
string = 'abcdfe2a354a32a'
print(string.replace('a', 'A'))

print("-"*20)
# 30 replace 메서드 -> print()결과는? 
string = 'abcd'
string.replace('b', 'B')
print('string :', string) # 'aBcd(X), abcd(O)

print("-"*20)
#31 문자열 합치기
a = "3"
b = "4"
print("a + b :",a + b) # 34

print("-"*20)
#32 문자열 곱하기
print("hi" * 3) # hihihi

print("-"*20)
#33 문자열 곱하기 -> '-' 80번 출력하기
print("- 80번 출력 결과 :",'-' * 80)

print("-"*20)
#34 문자열 곱하기 -> 더하기와 곱하기 이용해서 출력결과 : 'python java python java python java python java'처럼 출력하기
t1 = 'python'
t2 = 'java'

result = t1 + " " + t2 + " "
print("출력결과 :", result * 4) # 정답
print("출력결과 :", ((t1 + " " + t2) + " ") * 4) # 내가 푼 정답

print("-"*20)
# 35 문자열 출력 -> % formatting을 사용하여, 출력결과 : '이름: 김민수 나이: 10/n 이름: 이철희 나이: 13'
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13

print("이름: %s 나이: %d" % (name1, age1)) # 정답
print("이름: %s 나이: %d" % (name2, age2))
print(f"이름: {name1} 나이: {age1}") # 내가 푼 정답

print("-"*20)
# 36 문자열 출력 -> formate() 메서드 사용해서 35번 다시 풀기
print("이름: {} 나이: {}".format(name1, age1))
print("이름: {} 나이: {}".format(name2, age2))

print("-"*20)
# 37 문자열 출력 -> f-string 사용해서 35번 다시 풀기
print(f"이름: {name1} 나이: {age1}") # 내가 푼 정답

print("-"*20)
# 38 컴마제거하기 -> 컴마 제거 후, 정수로 변환
상장주식수 = "5,969,782,550"
coma_remove = 상장주식수.replace(',',"")
print("컴마제거 결과 :", coma_remove)
print("정수변환 결과 :", int(coma_remove))

print("-"*20)
# 39 문자열 슬라이싱 -> 출력결과: '2020/03'
분기 = "2020/03(E) (IFRS연결)"
print("출력결과 :", 분기[:7])

print("-"*20)
# 40 strip 메서드 -> 좌우 공백 제거
data = "   삼성전자    "
print("출력결과 :", data.strip())
print(data)


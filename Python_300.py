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

print("-"*20)
# 41 upper 메서드 -> 대문자 변경
print("-"*20)
ticker = "btc_krw"
print("upper() :", ticker.upper())

print("-"*20)
# 42 lower 메서드 -> 소문자 변경
ticker = "BTC_KRW"
print("lower() :", ticker.lower())

print("-"*20)
# 43 capitalize 메서드 -> 'hello'있다면, 'Hello'로 변경
# capitalize란? : 문자열 첫글자 대문자, 나머지 소문자 변환
word = 'hello'
print(word.capitalize())

print("-"*20)
# 44 endswith 메서드 -> 파일 이름이 'xlsx'로 끝나는지 확인
# 문자열 중 특정 문자 찾기, 특정문자 시작하는 문자열, 특정문자로 끝나는 문자열 찾는 방법
# 1) find(찾을 문자, 찾기 시작할 위치) : 위치 없는 경우, -1 반환
# 2) startswith(시작하는 문자, 시작 지점) : Bloon 값으로 반환
# 3) endswith(끝나는 문자, 문자열 시작, 문자열 끝) : : Bloon 값으로 반환
file_name = "보고서.xlsx"
print(file_name.endswith('xlsx')) # True

print("-"*20)
# 45 endswith 메서드 -> 파일 이름이 'xls' or 'xlsx'로 끝나는지 확인
print(file_name.endswith(('xls','xlsx'))) # True
# print(file_name.endswith('xls','xlsx')) # TypeError: slice indices must be integers or None or have an __index__ method

print("-"*20)
# 46 startwith 메서드 -> 파일 이름 '2020' 시작하는지 화긴
file_name = "2020_보고서.xlsx"
print(file_name.startswith('2020')) # True

print("-"*20)
# 47 split 메서드
a = "hello world"
print(a.split(' ')) # ['hello', 'world']

print("-"*20)
# 48 split 메서드 -> btc와 krw로 나누기
ticker = "btc_krw"
print(ticker.split('_')) # ['btc', 'krw']

print("-"*20)
# 49 split 메서드 -> 년도, 월, 일 나누가
date = "2020-05-01"
print(date.split('-')) # date = "2020-05-01"

print("-"*20)
# 50 rstrip 메서드 -> 오른쪽 공백 제거
data = "039490     "
data = data.rstrip()
print("공백제거 후 :", data)
print(data.rstrip(" "))

print("-"*20)
# 51 리스트 생성
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
print(movie_rank) # ['닥터 스트레인지', '스플릿', '럭키']

print("-"*20)
# 52 리스트 원소 추가
movie_rank.append("배트맨")
print("movie_rank 원소추가:", movie_rank) # ['닥터 스트레인지', '스플릿', '럭키', '배트맨']

print("-"*20)
# 53 리스트의 "슈퍼맨"을 "닥터 스트레인지"와 "스플릿" 사이에 추가하기
movie_rank.insert(1, "슈퍼맨")
print("movie_rank에 '슈퍼맨' 추가 :", movie_rank) # ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']

# 문자열 사이에 원하는 값 추가 : insert(위치할 인덱스, 추가시킬 값)

print("-"*20)
# 54 리스트에서 "럭키" 삭제
print(movie_rank)
del movie_rank[3]
print("movie_rank에서 '럭키' 삭제 :", movie_rank) # ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']

print("-"*20)
# 55 리스트에서 '스플릿' 과 '배트맨'을 를 삭제
print(movie_rank)
del movie_rank[2:]
print("movie_rank에서 '스플릿'&'배트맨' 삭제 ", movie_rank) # ['닥터 스트레인지', '슈퍼맨']

print("-"*20)
# 56 lang1과 lang2의 원소를 모두 갖고 있는 langs 리스트를 만들기 = 리스트 합치기
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]

langs = lang1 + lang2
print("lang1 + lang2 :", langs)

print("-"*20)
# 57 최댓값, 최솟값
nums = [1, 2, 3, 4, 5, 6, 7]

print("최댓값 :", max(nums))
print("최솟값 :", min(nums))

print("-"*20)
# 58 리스트 합
nums = [1, 2, 3, 4, 5]

print("리스트 합 :", sum(nums))

print("-"*20)
# 59 데이터 갯수 구하기
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]

print("리스트 갯수 :", len(cook))

# 갯수 세기 종류 
# 1) count() : list명.count(찾고자 하는 요소)
# 2) len() : list 내의 전체 요소 갯수 = 총 길이

print("-"*20)
# 60 평균 
nums = [1, 2, 3, 4, 5]

print("평균 :", sum(nums) / len(nums))

# 평균구하는 방법 총 4가지 : for 반복문, sum 함수, numpy 모듈이용, statiscics 라이브러리 이용

print("-"*20)
# 61 -> 날짜 제외, 가격만 출력
price = ['20180728', 100, 130, 140, 150, 160, 170]
print("price 가격만 :", price[1:])

print("-"*20)
# 62 -> 슬라이싱 홀수 출력
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("홀수 출력 :", nums[::2])

print("-"*20)
# 63 -> 슬라이싱 짝수 출력
print("짝수 출력 :", nums[1::2])

print("-"*20)
# 64 -> 슬라이싱 사용한, 리스트 역방향 출력
nums = [1, 2, 3, 4, 5]
print("역방향 :", nums[::-1])

print("-"*20) 
# 65 -> 출력 값 : 삼성전자 Naver
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2])

print("-"*20) 
# 66 -> 출력 값 : 삼성전자 LG전자 Naver SK하이닉스 미래에셋대우
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(" ".join(interest))

print("-"*20) 
# 67 -> 삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우
print("/".join(interest))

print("-"*20) 
# 68 -> join 메서드
print("\n".join(interest))

print("-"*20)
# 69 -> split 메서드
string = "삼성전자/LG전자/Naver"
print("'/'구분 :", string.split("/"))

print("-"*20)
# 70 -> 리스트 오름차순 정렬
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)

# list.sort() : list 오름차순 정렬 / list 멤버 함수(메서드) / list 자체 정렬
# list.sorted)() : 새로운 정렬된 list 반환
print("-"*20)
# 71 -> 비어있는 튜플 만들기
my_variable = ()
print("빈 tuple :", type(my_variable), my_variable)

print("-"*20)
# 72 
movie_rank = ("닥터 스트레인지", "스플릿", "럭키")
print("영화제목 :", type(movie_rank), movie_rank)

print("-"*20)
# 73 -> 숫자1 저장된 튜플
number1 = (1)
number2 = (1, )
number3 = (1,2)

print("number1 출력 :", type(number1), number1) # type : int
print("number2 출력 :", type(number2), number2) # type : tuple --> 1개 데이터 저장시, 쉼표 같이 입력하기
print("number3 출력 :", type(number3), number3) # type : tuple

# print("-"*20)
# # 74 -> 에러 원인
# t = (1,2,3)
# t[0] = 'a' # tuple은 데이터 변경 불가 성질 있다.
# print(t)

print("-"*20)
# 75 
t = 1,2,3,4
print("t type :", type(t), t) # 괄호 없어도, 데이터 type은 tuple

print("-"*20)
# 76 
t = ('a', 'b', 'c')
print("첫번째 t :", t)
t = ('A', 'b', 'c')
print("두번째 t :", t)

print("-"*20)
# 77 튜플 -> 리스트 변경
interest = ('삼성전자', 'LG전자', 'SK Hynix')
print("interest type :", type(interest), interest)
print("interest type :", type(list(interest)), list(interest))

print("-"*20)
# 78 리스트 -> 튜플 변경
interest = ['삼성전자', 'LG전자', 'SK Hynix']
print("interest type :", type(interest), interest)
print("interest type :", type(tuple(interest)), tuple(interest))

print("-"*20)
# 79 
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c) # apple banana cake

print("a :", a)
print("b :", b)
print("c :", c)

print("-"*20)
# 80 -> 1 ~ 99 중 짝수만 튜플에 저장
result_list = []
for i in range(1, 100):
    if i % 2 == 0:
        result_list.append(i)
print(tuple(result_list))

# 정답
data = tuple(range(2, 100, 2))
print(data)

print("-"*20)
# 81 별(*) 표현식
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]

*valid_score,_,_ = scores
print("좌측 8개 결과 :", valid_score)

print("-"*20)
# 82 별(*) 표현식
_,_,*valid_score = scores
print("우측 8개 결과 :", valid_score)

print("-"*20)
# 83 별(*) 표현식
_,*valid_score,_ = scores
print("가운데 8개 결과 :", valid_score)

print("-"*20)
# 84
temp = {}
print("빈 dict :", type(temp), temp)

print("-"*20)
# 85
ice_cream = {"메로나" : 1000, "폴라포" : 1200, "빵빠레" : 1800}
print("ice_cream :", ice_cream)

print("-"*20)
# 86 dict 추가
ice_cream["죠스바"] = 1200
ice_cream["월드콘"] = 1500

print("dict 추가 :", ice_cream)

print("-"*20)
# 87 
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}

print("메로나 가격 :", ice["메로나"])

print("-"*20)
# 88 ict 수정
ice["메로나"] = 1300
print("메로나 수정 :", ice)


print("-"*20)
# 89 dict 삭제
del ice["메로나"]

print("메로나 삭제 :", ice)

print("-"*20)
# 91
inventory = {"메로나" : [300, 20], "비비빅" : [400, 3], "죠스바" : [250, 100]}
print("inventory :", type(inventory), inventory)

print("-"*20)
# 92 -> inventory에서 메로나 가격 출력 : "300 원"
print("메로나 가격 :", inventory["메로나"][0], "원")

print("-"*20)
# 93 -> inventory에서 메로나 재고 출력 : "20 개"
print("메로나 재고 :", inventory["메로나"][1], "개")

print("-"*20)
# 94 -> inventory에 데이터 추가
inventory["월드콘"] = [500, 7]
print("월트콘 추가 :", inventory)

print("-"*20)
# 95 -> 딕셔너리 key값만 구성된 리스트 생성 : keys() 메서드
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
keys = icecream.keys()

print("key값들 리스트1 :", type(keys), keys) 
print("key값들 리스트2 :", type(list(keys)), list(keys)) # 정답

print("-"*20)
# 96 -> 딕셔너리 values값만 구성된 리스트 생성 : values()메서드
values = icecream.values()

print("values값들 리스트1", type(values), values)
print("values값들 리스트2", type(list(values)), list(values)) # 정답

print("-"*20)
# 97 -> icecream 판매 금액 총합
values = icecream.values()
values_list =list(values)
print(sum(values_list)) # 방법1)

list_sum = 0 # 방법2)
for i in values_list:
    list_sum += i
print("list_sum :", list_sum)

print("-"*20)
# 98 -> 딕셔너리를 딕셔너리에 추가하기
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}

# 방법1
icecream.update(new_product)
print("new_procdut 병합된 dict :", icecream) 
print("new_product :", new_product)

# 방법2
# print("union(|) 연산자 이용 :", icecream | new_product)

# 방법3
from audioop import avg
from copy import deepcopy
from dataclasses import replace
from datetime import datetime
from posixpath import split
import re
a = deepcopy(icecream)
a.update(new_product)
print("deepcopy참조 :", a)

print("-"*20)
# 99 -> 두개의 튜플를 딕셔너리 변환
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
a = zip(keys, vals)
print("dict :", dict(a))

print("-"*20)
# 100 -> 두개의 리스트를 딕셔너리로 생성
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]

close_table = zip(date, close_price)
print("close_table :", dict(close_table))

# 파이썬 분기ans
print("-"*20)
# 101 -> True False 타입
print(type(True)) # bool
print(type(False)) # bool

print("-"*20)
# 102 
print(3 == 5) # False

print("-"*20)
# 103 
print(3 < 5) # True

print("-"*20)
# 104 
x = 4
print(1 < x < 5) # True

print("-"*20)
# 105 
print ((3 == 3) and (4 != 3)) # T and T => True

print("-"*20)
# 106 
'''
print(3 => 4) # 에러발생이유 : >= 부등호 위치(지원하지 않는 연산자)
'''

print("-"*20)
# 107 
if 4 < 3:
    print("Hello World")

'''
실행결과 : 아무것도 출력되지 않는다.
        왜? 조건식이 '참'일경우에만, "Hello World"가 출력되기 때문
'''

print("-"*20)
# 108 
if 4 < 3:
    print("Hello World.")
else:
    print("Hi, there.")

'''
실행결과 : Hi, there. 출력 
        왜? 4 < 3이 참이 아니므로, else 조건문 실행되기 때문
'''

print("-"*20)
# 109
if True :
    print ("1")
    print ("2")
else :
    print("3")
print("4")

'''
실행결과 : 
1 
2
4
로 출력
왜? 항상 True는 참이고, if절이 끝나면 마지막으로 print("4") 실행되므로
'''

print("-"*20)
# 110
if True :
    if False:
        print("1")
        print("2")
    else:
        print("3")
else :
    print("4")
print("5")

'''
실행결과 : 
3
5
로 출력
왜? 첫번째 if문에서 True 조건식은 항상 참이므로, 두번째 if문을 실행한다.
두번째 if문에서 False 조건식은 항상 참이 아니므로, else 실행하여 print("3")출력
2개의 if문 끝나면 마지막 print("5") 실행됨
'''

# print("-"*20)
# 111 -> 입력받은 문자열 두번 출력
# print(input("문자를 입력하세요 :") * 2)

# print("-"*20)
# 112 -> 입력받은 숫자에 10더하기
# print(int(input("숫자를 입력하세요 :")) + 10)

# print("-"*20)
# 113 -> 입력받은 숫자 홀짝 판별
# num = int(input("숫자하나를 입력하세요 : "))

# if num % 2 == 0:
#     print("짝수")
# if num & 2 == 1:
#     print("홀수")

# print("-"*20)
# 114 -> 입력받은 값 + 20 출력 ==> 255초과시 255출력
# num = int(input("숫자를 입력하세요 : ")) + 20

# 내가 작성한 코드 
# if num <= 255:
#     print("num은", num)
# if num + 20 > 255:
#     print(255)

# 답
# if num > 255:
#     print(255)
# else:
#     print(num)

# print("-"*20)
# 115 -> 입력받은 값 - 20 / 0 < 출력범위 < 255 / 출력값 < 0 : 0출력 , 출력값 > 255 : 255출력
# num = int(input("숫자를 입력하세요2 :")) - 20

# if num < 0:
#     print(0)
# if num > 255:
#     print(255)
# if 0 < num < 255:
#     print(num)

# print("-"*20)
# 116 -> 시간정각 여부 판별 
# time = datetime(input("현재시간: "))

# if time[-2:] == "00":
#     print("정각 입니다.")
# else:
#     print("정각이 아닙니다.")

# print("-"*20)
# 117 -> 입력받은 단어가 리스트내에 fruit 포함여부 출력
# fruit = ["사과", "포도", "홍시"]
# input_fruit = input("좋아하는 과일읍? :")

# if input_fruit in fruit:
#     print("정답입니다.")
# else:
#     print("오답입니다.")

# print("-"*20)
# 118 -> 입력받은 종목명이 투자 경고 종목 리스트 포함여부 출력
# warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
# input_warn_investment_list = input("종목명을 입력하세요 :") 

# if input_warn_investment_list in warn_investment_list:
#     print("투자 경고 종목입니다.")
# else:
#     print("투자 경고 종목이 아닙니다.")

# print("-"*20)
# 119 -> 입력받은 값이 딕셔너리 key값 포함여부 출력
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# input_fruit = input("제가 좋아하는 계절은")

# # 내가 입력한 코드
# if input_fruit in list(fruit.keys()):
#     print("정답입니다.")
# else:
#     print("오답입니다.")

# # 답
# if input_fruit in fruit:
#     print("정답입니다.")
# else:
#     print("오답입니다.")

# print("-"*20)
# 120 -> 입력받은 값이 딕셔너리 value값 포함여부 출력
# input_fruit = input("제가 좋아하는 과일은")
# if input_fruit in list(fruit.values()):
#     print("정답입니다.")
# else:
#     print("오답입니다.")

# print("-"*20)
# 121 -> 입력받은 문자 하나가 소문자일경우 대문자로, 대문자일경우 소문자로 출력
# input_string = input("영어 한개 입력 :")

# # 내가 입력한 코드
# if input_string == input_string.lower():
#     print(input_string.upper())
# if input_string == input_string.upper():
#     print(input_string.lower())

# # 답
# if input_string.islower():
#     print(input_string.upper())
# else:
#     print(input_string.lower())

# print("-"*20)
# 122 -> 입력받은 스코어 학점 출력
# input_score = int(input("점수 입력 :"))

# if input_score >= 81:
#     print("grade is A")
# elif input_score >= 61:
#     print("grade is B")
# elif input_score >= 41:
#     print("grade is C")
# elif input_score >= 21:
#     print("grade is D")
# elif input_score >= 0:
#     print("grade is E")

# print("-"*20)
# 123 
# 통화명 = {
#     "달러" : 1167,
#     "엔" : 1.096,
#     "유로" : 1268,
#     "위안" : 171
# }

# input_data = input("입력 : ")
# data_list = input_data.split()
# # float함수 - 소수점 첫째자리
# # print(1, float(data_list[0]) * 통화명[data_list[1]], "원")

# # "{:.자릿수f}".format(실수) 함수 - 소수점 f자리수
# data_num = float(data_list[0])
# data_num_환율 = data_num * 통화명[data_list[1]]
# print("방법1 :", "{:.2f}".format(data_num_환율), "원")
# print("방법2 :", format(data_num_환율, ".2f"), "원")

# print("-"*20)
# 124 -> 입력받은 숫자 3개중 가장 큰숫자 출력
# 방법1) list 이용
# datas1 = [
#     int(input("input_number1 :")),
#     int(input("input_number2 :")),
#     int(input("input_number3 :"))
# ]
# print(max(datas1))

# # 방법2) dictionary 이용
# datas2 = {
#     "num1" : int(input("input_number1 :")),
#     "num2" : int(input("input_number2 :")),
#     "num3" : int(input("input_number3 :"))
# }
# result = list(datas2.values())
# print(max(result))

# # 방법3) 정답
# num1 = int(input("input_number1 :")) 
# num2 = int(input("input_number2 :"))
# num3 = int(input("input_number3 :"))

# if num1 >= num2 and num1 >= num3:
#     print(num1)
# elif num2 >= num1 and num2 >= num3:
#     print(num2)
# else:
#     print(num3)

# print("-"*20)
# 125

# 내가쓴답)
# phone = {
#     "011" : "SKT",
#     "016" : "KT",
#     "019" : "LGU",
#     "010" : "알수없음"
# }

# input_data = input("휴대전화 번호 입력 :")
# input_data_list = input_data.split("-")
# phone_first_num = list(phone.keys())
# phone_mid_num = phone[input_data_list[0]]

# if input_data_list[0] in phone_first_num:
#     print(f"당신은 {phone_mid_num} 사용자입니다.")

# # 정답)
# number = input("휴대전화 번호 입력 :")
# number_first = number.split("-")[0]

# if number_first == "011":
#     service = "SKT"
# elif number_first == "016":
#     service = "KT"
# elif number_first == "019":
#     service = "LGU"
# else:
#     service = "알수없음"

# print(f"당신은 {service} 사용자입니다.")

# print("-"*20)
# 126
# input_data = input("우편번호 :")
# gu= {
#     "강북구":["010","011","012"], 
#     "도봉구":["013","014","015"], 
#     "노원구":["016","017","018","019"]
# }
# gue_num = list(gu.values())

# if input_data[:3] in gue_num[0]: 
#     print("강북구")
# elif input_data[:3] in gue_num[1]: 
#     print("도봉구")
# elif input_data[:3] in gue_num[2]: 
#     print("노원구")

# print("-"*20)
# 127 -> 입력받은 주민번호로 성별출력하기
# input_data = input("주민등록번호 :")
# num = input_data.split("-")[1] 

# if (num[0] == '1') or (num[0] == '3'):
#     print("남자")
# elif (num[0] == '2') or (num[0] == '4'):
#     print("여자")

# print("-"*20)
# 128
# input_data = input("주민등록번호 :")
# num = input_data.split("-")[1]

# # 내가 쓴 답
# if int(num[1]) == 0:
#     if int(num[2]) in range(9):
#         print("서울 입니다.")
#     elif int(num[2]) == 9:
#         print("서울이 아닙니다.")
# elif int(num[1]) == 1:
#     if int(num[2]) in range(1, 3):
#         print("서울이 아닙니다.") 
# elif int(num[1]) != 0 or int(num[1]) != 1:
#     print("서울이 아닙니다.") 

# # 정답
# if 0 <= int(num[1:3]) <= 8:
#     print("서울입니다.")
# else:
#     print("서울이 아닙니다.")

# print("-"*20)
# # 129
# input_data = input("주민등록번호 :")
# a = input_data.replace("-", "")
# print(a)
# b = a[:-1]

# 곱할수 = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
# c = []
# for i in range(len(곱할수)):
#     c.append(int(b[i]) * 곱할수[i])
# avg = sum(c) / 11
# result = 11 - avg

# # 리스트 컨프리헨션
# # c = [int(b[i]) * 곱할수[i] for i in range(len(곱할수))]

# if input_data[-1] == result:
#     print("유효한 주민등록번호입니다.")
# else:
#     print("유효하지 않은 주민등록번호입니다.")

print("-"*20)
# 130 
# import requests
# btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
# '''
# m_n = 최고가 - 최저가 = btc('max_price') - btc('min_price')
# result = 시가 + 변동폭 = int(btc('opening_price')) - int(m_n)
# '''

# m_n = int(btc['max_price']) - int(btc['min_price'])
# result = int(btc['opening_price']) - int(m_n)

# if result > int(btc['max_price']):
#     print("상승장")
# else:
#     print("하락장")

print("-"*20)
# 131 -> 결과 예측하기
과일 = ["사과", "귤", "수박"]
for 변수 in 과일:
    print(변수)

'''
결과 : 
사과
귤
수박
'''

print("-"*20)
# 132 -> 결과 예측하기
과일 = ["사과", "귤", "수박"]
for 변수 in 과일:
  print("#####")

'''
결과 :
#####
#####
#####
출력
'''

print("-"*20)
# 136
for i in [10, 20, 30]:
    print(i)

print("-"*20)
# 138
for i in [10, 20, 30]:
    print(i)
    print("-------")

print("-"*20)
# 139
for i in ["++++", 10, 20, 30]:
    print(i)

print("-"*20)
# 140
for i in range(4):
    print("-------")

print("-"*20)
# 141 -> 부가세 10 포함한 가격 반환
리스트 = [100, 200, 300]
for i in 리스트:
    print(i + 10)

print("-"*20)
# 142
리스트 = ["김밥", "라면", "튀김"]
for i in 리스트:
    print("오늘의 메뉴:", i)

print("-"*20)
# 143 -> 문자열 길이 출력
리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
for i in 리스트:
    print(len(i))

print("-"*20)
# 144
리스트 = ['dog', 'cat', 'parrot']
for i in 리스트:
    print(i, len(i))

print("-"*20)
# 145 -> 첫글자만 반환
리스트 = ['dog', 'cat', 'parrot']
for i in 리스트:
    print(i[0])

print("-"*20)
# 146
리스트 = [1, 2, 3]
for i in range(len(리스트)):
    print(리스트[2], 'x', 리스트[i])

print("-"*20)
# 147 
리스트 = [1, 2, 3]
for i in range(len(리스트)):
    print(리스트[2], 'x', 리스트[i], '=', 리스트[2]*리스트[i])

print("-"*20)
# 148
리스트 = ["가", "나", "다", "라"]
for i in 리스트[1:]:
    print(i)

print("-"*20)
# 149
# 방법1)
for i in 리스트[::2]:
    print(i)

print("-"*20)
# 150
for i in 리스트[::-1]:
    print(i)

print("-"*20)
# 151
리스트 = [3, -20, -3, 44]

for i in 리스트:
    if i < 0:
        print(i)

print("-"*20)
# 152
리스트 = [3, 100, 23, 44]

for i in 리스트:
    if i % 3 == 0:
        print(i)

print("-"*20)
# 153
리스트 = [13, 21, 12, 14, 30, 18]

for i in 리스트:
    if i < 20 and i % 3 == 0:
        print(i)

print("-"*20)
# 154
리스트 = ["I", "study", "python", "language", "!"]

for i in 리스트:
    if len(i) >= 3:
        print(i)

print("-"*20)
# 155
리스트 = ["A", "b", "c", "D"]

for i in 리스트:
    if i.upper() == i:
        print(i)

print("-"*20)
# 156
리스트 = ["A", "b", "c", "D"]
# 내가 쓴답
for i in 리스트:
    if i.upper() != i:
        print(i)

# 정답
for i in 리스트:
    if i.upper() == False:
        print(i)


print("-"*20)
# 157
리스트 = ['dog', 'cat', 'parrot']
print(리스트[0][0].upper())
print(리스트[0].upper())

for i in 리스트:
    print(i.replace(i[0], i[0].upper()))


print("-"*20)
# 158
리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
for i in 리스트:
    print(i.split(".")[0])


print("-"*20)
# 159
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']

for i in 리스트:
  if i.split(".")[1][0] == "h":
    print(i)

print("-"*20)
# 160
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']

for i in 리스트:
  a = i.split(".")[1][0]
  if a == "h" or a == "c":
    print(i)

print("-"*20)
# 161
for i in range(100):
  print(i)

print("-"*20)
# 162
for i in range(2002,2051,4):
  print(i)

print("-"*20)
# 163
# 내가 쓴답
for i in range(1, 31):
  if i % 3 ==0:
      print(i)

# 정답
for num in range(3, 31, 3):
    print (num)

print("-"*20)
# 164
for i in range(99, -1, -1):
    print(i)

print("-"*20)
# 165 

print("-"*20)
# 166
for i in [3]:
    for j in range(1,10):
        print(i,"x",j,"=",i*j)
        
print("-"*20)
# 167
# 내가 쓴답
for i in [3]:
    for j in range(1, 10):
      if j % 2 == 1:
        print(i,"x",j,"=",i*j)

# 정답
num = 3
for i in range(1, 10, 2) :
    print (num, "x", i, " = ", num * i)

print("-"*20)
# 168
num = 0
for i in range(1, 11):
  num += i
print(num)

print("-"*20)
# 169
num = 0
for i in range(1, 11, 2):
  num += i
print(num)

print("-"*20)
# 170
num = 1
for i in range(1, 10):
  num *= i
print(num)

print("-"*20)
# 171
price_list = [32100, 32150, 32000, 32500]

for i in range(len(price_list)):
  print(price_list[i])

print("-"*20)
# 172
for i in range(len(price_list)):
  print(i, price_list[i])

print("-"*20)
# 173
# 정답
for i in range(len(price_list)):
    print(len(price_list) -1 -i, price_list[i])

print("-"*20)
# 174
for i in range(1, len(price_list)):
    print(90 + 10 * i, price_list[i])
  
print("-"*20)
# 175
my_list = ["가", "나", "다", "라"]

for i in range(1, len(my_list)): 
    print(my_list[i-1], my_list[i])

print("-"*20)
# 176
my_list = ["가", "나", "다", "라", "마"]

for i in range(2, len(my_list)): 
    print(my_list[i-2], my_list[i-1], my_list[i])

print("-"*20)
# 177
my_list = ["가", "나", "다", "라"]

for i in range(len(my_list)-1, 0, -1): 
    print(my_list[i], my_list[i-1]) 

# 178
my_list = [100, 200, 400, 800]

# 내가 푼것
for i in range(1,len(my_list)): 
    print(my_list[i] - my_list[i-1]) 

# 179
my_list = [100, 200, 400, 800, 1000, 1300]

# 내가 쓴답
for i in range(2, len(my_list)): #0,6) # 01,2,3,3,4.5
    sum1 = my_list[i-2] + my_list[i-1] + my_list[i]
    print(sum1 / 3)

print("합계", (my_list[0] + my_list[1] + my_list[2])/3)
print("합계", (my_list[1] + my_list[2] + my_list[3])/3)
print("합계", (my_list[2] + my_list[3] + my_list[4])/3)
print("합계", (my_list[3] + my_list[4] + my_list[5])/3)

# 정답
for i in range(1, len(my_list) - 1):
    print(abs(my_list[i-1] + my_list[i] + my_list[i+1]) / 3)

# 180
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]

volatiltiy = []
for i in range(len(low_prices)):
    변동폭 = high_prices[i] - low_prices[i]
    volatiltiy.append(변동폭)
print(volatiltiy)

# 181
apart = [[101, 102], [201, 202], [301, 302]]

# 182
stock = [[100, 80], [200,210], [300, 330]]

# 183
stock = {
    "시가" : [100, 200, 300],
    "종가" : [80, 210, 330]
}

# 184
stock = {
    "10/10" : [80, 110, 70, 90],
    "10/11" : [210, 230, 190, 200]
}

# 185
apart = [[101, 102], [201, 202], [301, 302]]

for i in apart:
    for j in i:
        print(j, "호") 

# 186
# 내가 쓴답
apart = [[101, 102], [201, 202], [301, 302]]

apart.reverse()
print(apart)

for i in apart:
    for j in i:
        print(j, "호")

# 정답
apart = [[101, 102], [201, 202], [301, 302]]
for i in apart[::-1]:
    for j in i:
        print(j, "호")

# 187
for i in apart[::-1]:
    for j in i[::-1]:
        print(j, "호")

# 188

for i in apart:
    for j in i:
        print(j, "호")
        print("-----")

# 189
for i in apart:
    for j in i:
        print(j, "호")
    print("-----")

# 190
for i in apart:
    for j in i:
        print(j, "호")
print("-----")

# 191
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]

for i in data:
  for j in i:
    print(j * 1.00014)

# 192
for i in data:
  for j in i:
    print(j * 1.00014)
  print("---")

# 193
result = []
for i in data:
  for j in i:
    result.append(j * 1.00014)
print(result)

result = [j * 1.00014 for i in data for j in i]
print(result)

# 194
result = []
for i in data:
  a = []
  for j in i:
    a.append(j * 1.00014)
  result.append(a)
print(result)

#195
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for i in ohlc[1:]:
  print(i[3])

# 196
for i in ohlc[1:]:
  if i[3] > 150:
    print(i[3])

# 197
for i in ohlc[1:]:
  if i[3] > i[0] or i[3] == i[0]:
    print(i[3])

# 198
volatility = []

for i in ohlc[1:]:
    volatility.append(i[1] - i[2])
print(volatility)

volatility = [i[1] - i[2] for i in ohlc[1:]]
print(volatility)

# 199
# 종가(close) > 시가(open)
for i in ohlc[1:]:
    if i[3] > i[0]:
        print(i[1] - i[2])

# 정답
for i in ohlc[1:]:
    open, high, low, close  = i
    if close > open:
        print(high - low)

# 200
result = 0
for i in ohlc[1:]:
    result = result + (i[3] - i[0])
print(111, result)

# 201 함수 정의하기
def print_coin():
    print("비트코인")

# 202 정의한 함수 호출하기
print_coin() 


#203
for i in range(100):
    print_coin()

# 204 함수 정의하기
# 내가 쓴답
def print_coins():
    print("비트코인" * 100)

# 정답
def print_coins():
    for i in range(100):
        print("비트코인")

print_coins() 

# 205 에러 발생하는 이유
'''
hello()
def hello():
    print("Hi")

# hello()함수가 정의되기 '전'에, 함수를 선언했기때문

'''

# 206
'''
def message() :
    print("A")
    print("B")

message()
print("C")
message()

# 출력예상결과
A
B
C
A
B
'''

# 207
'''
print("A")

def message() :
    print("B")

print("C")
message()

# 출력예상결과
A
C 
B
'''

# 208
'''
print("A")
def message1() :
    print("B")
print("C")
def message2() :
    print("D")
message1()
print("E")
message2()

# 출력예상결과
A
C
B
E
D
'''

# 209
'''
def message1():
    print("A")

def message2():
    print("B")
    message1()

message2()

# 출력예상결과
B
A
'''

# 210
'''
def message1():
    print("A")

def message2():
    print("B")

def message3():
    for i in range (3) :
        message2()
        print("C")
    message1()

message3()

# 출력예상결과
B
C
B
C
B
C
A
'''

# 215
def print_with_smile(문자열):
  print(문자열, ":D")

print_with_smile("안녕")

#216
print_with_smile("안녕하세요")

# 217
def print_upper_price(int):
  print(int * 0.3)

print_upper_price(30)

#218
# 내가쓴답
def print_sum(inta, intb):
  print(int(inta) + int(intb))

print_sum(1,2)

# 정답
def print_sum (a, b) :
    print (a + b)

#219
def print_arithmetic_operation(a, b):
  print(a, "+", b, "=", a + b)
  print(a, "-", b, "=", a - b)
  print(a, "*", b, "=", a * b)
  print(a, "/", b, "=", a / b)
  
print_arithmetic_operation(3, 4)

# 220
# 내가 쓴답
def print_max(a, b, c):
  if a > b and a > c:
    print(a)
  if b > a and b > c:
    print(b)
  if c > a and c > b:
    print(c)
    
print_max(1,2,3)

def print_max2(a, b, c):
  input = [a, b, c]
  max = a
  for i in input:
    if i > max:
      max = i
  print(max)

print_max2(4, 5, 10)

# 정답
def print_max3(a, b, c):
    result = 0
    if a > result:
        result = a
    if b > result:
        result = b
    if c > result:
        result = c
    print(result)

print_max3(10, 100, 200)

# 221 
def print_reverse(a):
    b = list(a)
    b.reverse()
    print("".join(b))

print_reverse("apple")

def print_reverse1(a):
    reverse_name = ''
    for i in a:
        reverse_name = i + reverse_name
        print(reverse_name)

print_reverse1("apple")

def print_reverse2(a):
    print(a[::-1])

print_reverse2("apple")

# 222
def print_score(score):
    print(sum(score) / len(score))

print_score([1,2,3])

print("-"*20)
# 223
def print_even(score):
    for num in score:
        if num % 2 == 0:
            print(num)

print_even([1, 3, 2, 10, 12, 11, 15])

print("-"*20)
# 224
def print_keys(name_info):
    keys = name_info.keys()
    for key in keys:
        print(key)

print_keys ({"이름":"김말똥", "나이":30, "성별":0})

print("-"*20)
# 225
my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}

def print_value_by_key(my_dict, date):
    if date in my_dict:
        print(my_dict[date])

print_value_by_key(my_dict, "10/26")

print("-"*20)
# 226
def print_5xn(string):
    num = int(len(string) / 5) 
    for i in range(num+1): 
        print(string[i * 5: i * 5 + 5])

print_5xn("아이엠어보이유알어걸일이삼사오육칠")

print("-"*20)
# 227
def print_mxn(string, input_num):
    num = int(len(string) / input_num)
    print(num) # 3 range(3) => 0,1,2
    for i in range(num + 1): # 0,1,2,3
        print(string[i * input_num: i * input_num + input_num]) # 0:3 / 3:6 / # 6:9 / 12:15

print_mxn("아이엠어보이유알어걸", 3)

print("-"*20)
# 228
def calc_monthly_salary(annual_salary):
    num = int(annual_salary / 12)
    print(num)

calc_monthly_salary(12000000)

print("-"*20)
# 229
'''
def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(a=100, b=200)

# 출력예상결과
왼쪽: 100
오른쪽: 200
'''

print("-"*20)
# 230
'''
def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(b=100, a=200)

# 출력예상결과
왼쪽: 200
오른쪽: 100
'''

print("-"*20)
# 231
'''
def n_plus_1 (n) :
    result = n + 1

n_plus_1(3)
print (result)

# 출력예상결과
4(틀림)
에러나옴: NameError: name 'result' is not defined(정답)
'''

print("-"*20)
# 232
def make_url(string):
    # return string
    result = "www." + string + ".com"
    return result

print(make_url("naver"))

print("-"*20)
# 233
# 내가 쓴답
def make_list(string):
    result = [i for i in string]
    return result

print(make_list("abcd"))

# 정답
def make_list1(string) :
    return list(string)

print(make_list1("abcd"))

print("-"*20)
# 234
def pickup_even(num_list):
    result = [i for i in num_list if i % 2 == 0]
    return result

print(pickup_even([3, 4, 5, 6, 7, 8]))

print("-"*20)
# 235
def convert_int(num):
    result = num.replace(",", "")
    print(int(result), type(int(result)))

convert_int("1,234,567")

print("-"*20)
# 236
'''
def 함수(num) :
    return num + 4

a = 함수(10)
b = 함수(a)
c = 함수(b)
print(c)

# 출력예상결과
22

# 과정
a = 10 + 4 = 14
b = 14 + 4 = 18
c = 18 + 4 = 22
'''

print("-"*20)
# 237
'''
def 함수(num) :
    return num + 4

c = 함수(함수(함수(10)))
print(c)

# 출력예상결과
22
'''

print("-"*20)
# 238
'''
def 함수1(num) :
    return num + 4

def 함수2(num) :
    return num * 10

a = 함수1(10)
c = 함수2(a)
print(c)

# 출력예상결과
140

# 과정
a = 10 + 4 = 14
c = 14 * 10 = 140
'''

print("-"*20)
# 239
'''
def 함수1(num) :
    return num + 4

def 함수2(num) :
    num = num + 2
    return 함수1(num)

c = 함수2(10)
print(c)

# 출력예상결과
16

# 과정
함수2(10)
    num = 10 + 2 = 12
    return 함수1(num) = 함수1(10) = 16
'''

print("-"*20)
# 240
'''
def 함수0(num) :
    return num * 2

def 함수1(num) :
    return 함수0(num + 2)

def 함수2(num) :
    num = num + 10
    return 함수1(num)

c = 함수2(2)
print(c)

# 출력예상결과
28

# 과정
함수2(2) 
    num = num + 10 = 2 + 10 = 12
    return 함수1(num) = 함수1(12)

함수1(12)
   return 함수0(num + 2) = 함수0(12 + 2) = 함수0(14)

함수0(14)
    return num * 2 = 14 * 2 = 28
'''

print("-"*20)
# 241
import datetime
print(datetime.datetime.now())

print("-"*20)
# 242
print(type(datetime.datetime.now())) #<class 'datetime.datetime'>

print("-"*20)
# 243
now_date = datetime.datetime.now().date()
for i in range(1,6):
    diff = now_date - (datetime.timedelta(i))
    print(diff)

# 정답
now = datetime.datetime.now()

for day in range(5, 0, -1):
    delta = datetime.timedelta(days=day)
    date = now - delta
    print(date)

print("-"*20)
# 244
# time = datetime.datetime.today().strftime("%H:%M:%S")
# time1 = datetime.datetime.now().strftime("%H:%M:%S")
# print(time, type(time)) # type : <class 'str'>
# print(time1)

print("-"*20)
# 245
today_date = '2022-02-28'
time_type = datetime.datetime.strptime(today_date, '%Y-%m-%d')
print(time_type, type(time_type))


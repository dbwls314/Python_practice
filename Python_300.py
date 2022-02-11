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
print("union(|) 연산자 이용 :", icecream | new_product)

# 방법3
from copy import deepcopy
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


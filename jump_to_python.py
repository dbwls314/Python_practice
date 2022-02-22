#02 연습문제
# 1 : 홍길동 평균 점수
score = {"국어" : 80, "영어" : 75, "수학" : 55}
score_values = list(score.values())
print(sum(score_values) / len(score_values))

# 2 : 13 홀짝 판별
num = 13
if num % 2 == 0:
    print(f"{num}은 짝수")
if num % 2 == 1:
    print(f"{num}은 홀수")

# 3 : 슬라이싱 이용하여 "YYYYMMDD"와 뒤 숫자 구분
number = "881120-1068234"
print(number[:6])
print(number[7:])

# 4 : 인덱스 이용하여 성별의미하는 숫자 출력
pin = "881120-1068234"
print(pin[7])

# 5 : replace이용하여 : -> #으로 변경
a = "a:b:c:d"
print(a.replace(":", "#"))

# 6 : 내장함수 이용하여 [1, 3, 5, 4, 2] -> [5, 4, 3, 2, 1]
a_list = [1, 3, 5, 4, 2]
a_list.sort()
a_list.reverse()
print(a_list)

# 7 : join함수 사용하여 ['Life', 'is', 'too', 'short'] -> "Life is too short" 출력
b_list = ['Life', 'is', 'too', 'short']
result = " ".join(b_list)
print(result)

# 8 :  (1,2,3) -> (1,2,3,4) 출력
result = (1,2,3) + (4,) 
print(result)

# 9 
'''
>>> a = dict()
>>> a
{}
'''

'''
오류 발생 하는 경우?
1. a['name'] = 'python'
2. a[('a',)] = 'python'
3. a[[1]] = 'python'
4. a[250] = 'python'
'''

'''
정답 3번 : 딕셔너리 키값은 변경가능한 값 사용할 수 없음 --> 'list'는 변경가능'
          딕셔너리 키 사용 가능(변하지 않는 값)? --> 문자열, 튜플, 숫자
'''

a = dict()
a['name'] = 'python'
a[('a',)] = 'python'
# a[[1]] = 'python'
a[250] = 'python'

print(a)

# 10 : pop 이용하여 a에서 'B'출력
a = {'A':90, 'B':80, 'C':70}

# 내가 푼 방식
a.pop('A')
a.pop('C')
print(a)

# 정답
result = a.pop('B') # pop으로 제거한 값을 변수에 할당
print(result)

# 11 : 리스트에서 중복 숫자 제거
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
print(list(set(a)))

# 12  
'''
a = b = [1, 2, 3]
a[1] = 4
print(b)
'''

a = b = [1,2,3]
# a = [1,2,3]
# b =[1,2,3]
a[1] = 4 
print(a) # a[1,4,3]
print(b) # a리스트와 동일하다

#03 연습문제
# 1 출력결과값 예상하기

'''
a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "short" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")
'''

'''
# 출력결과
shirt

그 이유 : if 와 elif는 조건이 참일 경우에만, 해당 출력값 출력후 구문 탈출!(그 다음 구문의 조건이 참이라고 한들)
        즉, if 혹은 elif 조건이 거짓일 경우엔, 다음 elif 혹은 else 구문으로 넘어간다
'''

# 2
# 내가 쓴답
result = []
num = 0
while num < 1000:
    if num % 3 == 0:
        result.append(num)
        num += 1
    else:
        num += 1
print("Result :", sum(result))

# 정답
result = 0
i = 1
while i <= 1000:
    if i % 3 == 0: 
        result += i
    i += 1

print(result)

# 3
# 내가 쓴답
i = 0
while i != 6:
    print("*" * i)
    i += 1

# 정답
i = 0
while True:
    i += 1
    if i > 5: break
    print('*' * i)

# 4
# for i in range(1, 101):
#     print(i)

# 5 
result_sum = 0
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
for i in A:
    result_sum += i
print(result_sum / len(A))

# 6
'''
numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)
'''
numbers = [1, 2, 3, 4, 5]

result = [i * 2 for i in numbers if i % 2 == 1]
print("result :", result)
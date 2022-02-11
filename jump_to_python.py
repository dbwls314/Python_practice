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

# 정담
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

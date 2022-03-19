# 1 - 1 : list 삭제 -> del, remove, pop 사용 가능
# 방법1)
from posixpath import split


nums = [100, 200, 300, 400, 500]
if (400 in nums) and (500 in nums):
    nums.remove(400)
    nums.remove(500)
    print(nums)

'''
리스트.remove(원소) --> 원하는 '원소' 삭제
'''
print('-'*20)

# 답안)
nums = [100, 200, 300, 400, 500]
nums.pop()
nums.pop()
print(nums)

'''
리스트.pop() --> 인덱스 가장 마지막 원소 삭제
리스트.pop(인덱스) --> 원하는 인덱스 원소 삭제
'''

print('-'*20)

# 1 - 2 : list 내장함수 insert
l = [200, 100, 300]
l.insert(2, 10000)
print(l)

print('-'*20)

# 1 - 3 : list type
l = [100, 200, 300]
print(type(l)) # --> type : list 
print('-'*20)

# 1 - 4
a = 1
print(type(a)) # --> type: int
b = 2.22
print(type(b)) # --> type: float
c = 'p'
print(type(c)) # --> type: str
d = [1,2]
print(type(d)) # --> type: list

print('-'*20)


# 1 - 5 --> a + b 예상 출력값
a = 10
b = 2
for i in range(1, 5, 2): # --> 1,3
    a += i
print(a+b)
'''
range(1,5,2) ==> 1,3
10 + 1 = 11
11 + 3 = 14
a = 14
b =2
a+b = 16
'''
print('-'*20)

# 1 - 6
for i in [None, 1, "", 0, bool(0)]:
    print(f"{i}", i == True)
'''
None     # --> Bool(False)
1        # --> Bool(True)
""       # --> Bool(False)
0        # --> Bool(False)
bool(0)  # --> Bool(False)
'''

print('-'*20)

# 1 - 7
'''
문제 : 변수명으로 올바르지 않은것
1)  age
2)  a
3)  as
4)  _age
5)  1age
 
------

답 : 3)as 5)1age
이유 : 
3번 --> as는 예약어! 예약어는 변수 사용X
5번 --> 숫자부터 시작하면 안됨
'''
print('-'*20)

# 1 - 8 : 딕셔너리 출력값은?
d = {'height':180,'weight':78,'weight':84,'temparture':36,'eyesight':1}
print(d['weight']) # --> 84
'''
딕셔너리 키 중복값 있을 경우, 가장 마지막 값 출력
'''

print('-'*20)

# 1 - 9
year = '2019'
month = '04'
day = '26'
hour = '11'
minute = '34'
second = '27'

print(year, month, day, sep="/", end=" ")
print(hour, minute, second, sep=":")

print('-'*20)

# 1 - 10
print('-'*20)

# 1 - 11
print('-'*20)

# 1 - 12
print('-'*20)

# 1 - 13
print('-'*20)

# 1 - 14
print('-'*20)

# 1 - 15
print('-'*20)

# 1 - 16
print('-'*20)

# 1 - 17
print('-'*20)

# 1 - 18
print('-'*20)

# 1 - 19
print('-'*20)

# 1 - 20
print('-'*20)

# 1 - 21
print('-'*20)

# 1 - 22
print('-'*20)

# 1 - 23
print('-'*20)

# 1 - 24
print('-'*20)

# 1 - 25
print('-'*20)

# 1 - 26
print('-'*20)

# 1 - 27
print('-'*20)

# 1 - 28
print('-'*20)

# 1 - 29
print('-'*20)

# 1 - 30
print('-'*20)

# 1 - 31
print('-'*20)

# 1 - 32
print('-'*20)

# 1 - 33
print('-'*20)

# 1 - 34
print('-'*20)

# 1 - 35
print('-'*20)

# 1 - 36
print('-'*20)

# 1 - 37
print('-'*20)

# 1 - 38
print('-'*20)

# 1 - 39
print('-'*20)

# 1 - 40
print('-'*20)

# 1 - 41
print('-'*20)

# 1 - 42
print('-'*20)

# 1 - 43
print('-'*20)

# 1 - 44
print('-'*20)

# 1 - 45
print('-'*20)

# 1 - 46
print('-'*20)

# 1 - 47
print('-'*20)

# 1 - 48
print('-'*20)

# 1 - 49
print('-'*20)

# 1 - 50
print('-'*20)

# 1 - 51
print('-'*20)

# 1 - 52
print('-'*20)

# 1 - 53
print('-'*20)

# 1 - 54
print('-'*20)

# 1 - 55
print('-'*20)

# 1 - 56
print('-'*20)

# 1 - 57
print('-'*20)

# 1 - 58
print('-'*20)

# 1 - 59
print('-'*20)

# 1 - 60
print('-'*20)

# 1 - 61
print('-'*20)

# 1 - 62
print('-'*20)

# 1 - 63
print('-'*20)

# 1 - 64
print('-'*20)

# 1 - 65
print('-'*20)

# 1 - 66
print('-'*20)

# 1 - 67
print('-'*20)

# 1 - 68
print('-'*20)

# 1 - 69
print('-'*20)

# 1 - 70
print('-'*20)

# 1 - 71
print('-'*20)

# 1 - 72
print('-'*20)

# 1 - 73
print('-'*20)

# 1 - 74
print('-'*20)

# 1 - 75
print('-'*20)

# 1 - 76
print('-'*20)

# 1 - 77
print('-'*20)

# 1 - 78
print('-'*20)

# 1 - 79
print('-'*20)

# 1 - 80
print('-'*20)

# 1 - 81
print('-'*20)

# 1 - 82
print('-'*20)

# 1 - 83
print('-'*20)

# 1 - 84
print('-'*20)

# 1 - 85
print('-'*20)

# 1 - 86
print('-'*20)

# 1 - 87
print('-'*20)

# 1 - 88
print('-'*20)

# 1 - 89
print('-'*20)

# 1 - 90
print('-'*20)

# 1 - 91
print('-'*20)

# 1 - 92
print('-'*20)

# 1 - 93
print('-'*20)

# 1 - 94
print('-'*20)

# 1 - 95
print('-'*20)

# 1 - 96
print('-'*20)

# 1 - 97
print('-'*20)

# 1 - 98
print('-'*20)

# 1 - 99
print('-'*20)

# 1 - 100
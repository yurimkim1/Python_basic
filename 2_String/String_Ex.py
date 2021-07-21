# 문자열(String) 문자, 단어 등으로 구성된 문자들의 집합

# 파이썬에서 문자열을 만드는 4가지 방법
print("Hello World")
print('Python is fun')
print("""Life is too short, Yon need python""")
print('''Life is too short, You need python''')

# 문자열 안에 작은따옴표나 큰따옴표를 포함시키고 싶을 때

# 1문자열안에 작은 따옴표 포함시키기
# Python's favorite food is perl
# 반드시 큰따옴표로 둘러써야 한다
# 큰따옴표 안에 있는 작은따옴표는 문자열을 나타내기 위한 기호로 인식되지 않는다
food = "Python's favorite food is perl"
print(food)

# 2문자열에 큰 따옴표 포함시키기
# "Python is very easy." he says.
# 작은 따옴표로 둘러싸기
say = '"Python is very easy." he says.'
print(say)

# 3백슬래시 사용 작은따옴표, 큰따옴표 문자열 포함
food = 'Python\'s favorite food is perl'
say = "\"Python is very easy.\" he says."
print(food)
print(say)

# 여러 줄인 문자열을 변수에 대입하고 싶을 때
# Life is too short
# Yon need python

# 1줄을 바꾸기 위한 이스케이프 코드 \n 삽입
multiline = "Life is too short\nYon need python"
print(multiline)

# 2연속된 작은따옴표 3개(''') 또는 큰따옴표 (""")사용하기
multiline='''
Life is too short
You need python
'''
multiline="""
Life is too short
You need python"""

print(multiline)

# [이스케이프 코드]
# 문자열 예제에서 여러 줄의 문장을 처리할 때 백슬래시 문자와 소문자 n을 조합한 \n 이스케이프 코드 사용
# 이스케이프코드란? 프로그래밍할 때 사용할 수 있도록 미리 정의해 둔 "문자조합"

# \n 문자열 안에서 줄을 바꿀 때 사용
# \t 문자열 사이에 탭 간격을 줄 때 사용
# \\ 문자 \를 그대로 표현할 때 사용
# \' 작은 따옴표를 그대로 표현할 때 사용
# \" 큰 따옴표를 그대로 표현할 때 사용
# \r 캐리지 리턴(줄바꿈문자, 현재커서를 가장앞으로 이동)
# \f 폼 피드(줄 바꿈문자, 현재 커서를 다음 줄로 이동)
# \a 벨 소리(출력할 때 PC스피커에서 삑 소리가 난다)
# \b 백 스페이스
# \000 널문자

# 활용빈도가 높은 것은 \n, \t, \\, \', \"

# 문자열 연산하기

# 1문자열 더해서 연결하기
head = "Python"
tail = " is fun!"
print(head + tail)

# 2문자열 곱하기(문자열 두번반복)
a = "python"
print(a * 2)

# 3문자열 곱하기 응용
print("=" * 50)
print("My Program")
print("=" * 50)

# 4문자열 길이 구하기
a = "Life is too short"
print(len(a))

# 문자열 인덱싱과 슬라이싱
# 인덱싱(indexing)이란 무엇인가를 "가리킨다"라는 의미, 슬라이싱(slicing)은 무엇인가 "잘라낸다"라는 의미

# 1문자열 인덱싱인란?
a = "Life is too short, Yon need Python"

# Life is too short, You need Python
# 0         1         2         3
# 0123456789012345678901234567890123

a = "Life is too short, Yon need Python"
print(a[3])

# a[0]:'L', a[1]:'i', a[2]:'f', a[3]:'e', a[4]:' ', ...

# 2문자열 인덱싱 활용하기
a = "Life is too short, Yon need Python"
print(a[0])
print(a[12])
print(a[-1])
print(a[-0])
print(a[-2])
print(a[-5])

# 3문자열 슬라이싱이란?
a = "Life is too short, Yon need Python"
b = a[0]+a[1]+a[2]+a[3]
print(b)

a = "Life is too short, Yon need Python"
print(a[0:4])
print(a[0:3])

# a[0:3] == 0 <= a < 3
# 간단하게 말해서 a[0:n]면 a[0:n-1까지의 자릿수]

# 4문자열을 슬라이싱하는 방법
print(a[0:5])
print(a[0:2])
print(a[5:7])
print(a[12:17])

# a[시작번호:끝번호]에서 끝번호 생략 후 시작번호부터 문자열끝까지 뽑아낸다
print(a[19:])

# a[시작 번호:끝 번호]에서 시작 번호를 생략하면 문자열의 처음부터 끝 번호까지 뽑아낸다.
print(a[:17])

# a[시작 번호:끝 번호]에서 시작 번호와 끝 번호를 생략하면 문자열의 처음부터 끝까지를 뽑아낸다
print(a[:])

# 슬라이싱에서도 인덱싱과 마찬가지로 마이너스(-)기호를 사용 가능
# 아래 소스코드에서 a[19:-7]이 뜻하는 것은 a[19]에서 a[-8]까지를 말함 , 역시 a[-7]은 불포함
print(a[19:-7])

# 5슬라이싱으로 문자열 나누기
a = "20010331Rainy"
date = a[:8]
weather = a[8:]
print(date)
print(weather)

# 연도, 월, 날씨 세부분으로 나누기
a = "20010331Rainy"
year = a[:4]
day = a[4:8]
weather = a[8:]
print(year)
print(day)
print(weather)

# "Pithon"이라는 문자열을 "Python"으로 바꾸려면?
a = "Pithon"
print(a[1])
# a[1] = 'y' #오류 발생

a = "Pithon"
print(a[:1])
print(a[2:])
print(a[:1] + 'y' + a[2:]) # 중간에 y를 추가해줌

# 문자열 포매팅
# 문자열 안의 특정한 값을 바꿔야 할 경우가 있을 때 이것을 가능하게 해주는 것이 문자열 포매팅기법
# 쉽게 말해 문자열 포매팅이란 문자열 안에 어떤 값을 삽입하느 방법

# 1문자열 포매팅 따라하기
# 1-1 숫자 바로 대입
print("I eat %d apples." % 3)

# 1-2 문자열 바로 대입
print("I eat %s apples." % "five")

# 1-3 숫자 값을 나타내는 변수로 대입
number = 3
print("I eat %d apples." % number)

# 1-4 2개 이상의 값 넣기
number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days." % (number, day))

# 문자열 포맷 코드
# %s 문자열
# %c 문자 1개
# %d 정수
# %f 부동소수
# %o 8진수
# %x 16진수
# %% Literal %(문자 % 자체)

# %s 포맷 코드는 어떤 형태 값이든 변환해 값 삽입 가능
print("I have %s apples" % 3)
print("rate is %s" % 3.234)

# "Error is %d%." % 98

# %d와 %를 같이 쓸 때는 %%를 쓴다
print("Error is %d%%" % 98)

# 2포맷 코드와 숫자 함께 사용하기
# 2-1 정렬과 공백
print("%10s" % "hi")
# %10s 는 전체길이가 10개인 문자열 공간에서 대입되는 값을 오른쪽으로 정렬하고 그앞의 나머지는 공백으로 남겨두라는 의미

print("%-10sjane" % 'hi')
# %-10은 hi는 왼쪽정렬, 나머지는 공백으로 채움

# 2-2 소수점 표현하기
print("%0.4f" % 3.42134234)

print("%10.4f" % 3.42134234)
# 전체 길이가 10개인 문자열 공간에서 오른쪽으로 정렬

# 3 format 함수를 사용한 포매팅

# 3-1 숫자 바로 대입하기
print("I eat {0} apples".format(3))
# {0} 부분이 숫자 3으로 바뀌었다

# 3-2 문자열 바로 대입하기
print("I eat {0} apples.".format("five"))
# {0} 부분이 five라는 문자열으로 바뀌었다

# 3-3 숫자 값을 가진 변수로 대입하기
number = 3
print("I eat {0} apples.".format(number))
# {0} 부분이 number 변수 값인 3으로 바뀌었다

# 3-4 2개 이상의 값 넣기
number = 10
day = "three"
print("I ate {0} apples. so I was sick for {1} days.".format(number, day))
# 2개 이상 값을 넣을 경우 문자열의 {0}, {1}과 같은 인덱스 항목이 format함수의 입력값으로 순서에 맞게 바뀐다.
# 즉 위 예에서 나온 {0}은 format 함수의 첫 번째 입력값인 number로 바뀌고 {1}는 format함수의 두번째 입력값인 day로 바뀐다

# 3-5 이름으로 넣기
print(f"I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3))
# {name} 형태를 사용할 경우 format 함수에는 반드시 name=value와 같은 형태의 입력값이 있어야만 한다.
# 위 예는 문자열의 {number}, {day}가 format함수의 입력값인 number=10, day =3 값으로 각각 바뀌는 것을 보여주고있다.

# 3-6 인덱스와 이름을 혼용해서 넣기
print("I ate {0} apples. so I was sick {day} days.".format(10, day=3))

# 3-7 왼쪽 정렬
print("{0:<10}".format("hi"))
# :<10 표현식을 사용하면 치환되는 문자열을 왼쪽으로 정렬하고 문자열의 총 자릿수를 10으로 맞출 수 있다.

# 3-8 오른쪽 정렬
print("{0:>10}".format("hi"))
# 오른쪽 정렬은 :< 대신 :>을 사용하면 된다. 화살표 방향을 생각하면 어느 쪽으로 정렬되는지 파악 가능

# 3-9 가운데 정렬
print("{0:^10}".format("hi"))
# :^ 가운데 정렬

# 3-10 공백 채우기
print("{0:=^10}".format("hi"))
print("{0:!<10}".format("hi"))
# 공백을 채워넣을 문자값은 정렬 문자 <,>,^ 바로 앞에 넣어야 한다

# 3-11 소수점 표현하기
y = 3.42134234
print("{0:0.4f}".format(y))

print("{0:10.4f}".format(y))
# 자릿수를 10으로 맞출수도 있다

# 3-12 { 또는 } 문자 표현하기
print("{{ and }}".format())
# 중괄호를 포매팅 문자가 아닌 문자 그대로 사용하고 싶은 경우 위 예처럼 {{, }} 2개를 연속해서 사용

# f 문자열 포매팅
name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')
# f 문자열 포매팅은 위와 같이 name, age와 같은 변수 값을 생성한 후에 그 값을 참조할 수 있다.
# 또한 f 문자열 포매팅은 표현식을 지원하기 때문에 다음과 같은 것도 가능하다.

# 표현식이란 문자열 안에서 변수와 +, -와 같은 수식을 함께 사용하는 것
age = 30
print(f'나는 내년이면 {age+1}살이 된다')

# 딕셔너리는 f 문자열 포매팅에서 다음과 같이 사용가능
# 딕셔너리는 key와 value가 한쌍
d = {'name':'홍길동', 'age':30}
print(f'나의 이름은 {d["name"]}입니다 나이는 {d["age"]}입니다')

# 딕셔너리 정렬
print(f'{"hi":<10}') # 왼쪽 정렬
print(f'{"hi":>10}') # 오른쪽 정렬
print(f'{"hi":^10}') # 가운데 정렬

# 딕셔너리 공백채우기
print(f'{"hi":=^10}') # 가운데 정렬하고 '='문자로 공백채우기
print(f'{"hi":!<10}') # 왼쪽 정렬하고 '!' 문자로 공백 채우기

# 소수점 표현
y = 3.42134234
print(f'{y:0.4f}') # 소수점 4자리까지만 표현
print(f'{y:10.4f}') # 소수점 4자리까지 표현, 총 자리수 10자리

# f 문자열에서 {} 문자를 표시할려면 다음과 같이 두개를 동시에 사용해야함
print(f'{{ and }}')

# 문자열 관련 함수
# 문자열 자료형은 자체적으로 함수를 가지고 있다. 다른 말로 문자열 내장 함수라고 한다.
# 내장 함수를 사용할려면 문자열 변수 이름 뒤에 '.'를 붙인 다음 함수 이름을 써준다

# 1-1 문자 개수 세기 (Count)
a = "hobby"
print(a.count('b'))
# b의 갯수 돌려줌

# 1-2 위치 알려주기1 (find)
a = "Python is the best choice"
print(a.find('b'))
print(a.find('k'))
# 찾는 문자, 문자열 존재하지 않을시 -1 반환

# 1-3 위치 알려주기2 (index)
a = "Life is too short"
print(a.index('t')) # 문자열 중 문자 t가 맨 처음으로 나온 위치 반환
#rint(a.index('k'))
# find 함수와 다르게 존재하지 않는 문자를 찾으면 오류 발생

# 1-4 문자열 삽입(join)
print(",".join('abcd'))
# abcd 문자열 각각 사이에 ','를 삽입

# join함수의 입력으로 리스트를 사용하는 예
print(",".join(['a', 'b', 'c', 'd']))

# 1-5 소문자를 대문자로 바꾸기(upper)
a = "hi"
print(a.upper())

# 1-6 대문자를 소문자로 바꾸기(lower)
a = "hi"
print(a.lower())

# 1-7 왼쪽 공백 지우기 (lstrip)
a = " hi "
print(a.lstrip())

# 1-8 오른쪽 공백 지우기 (rstrip)
a = " hi "
print(a.rstrip())

# 1-9 양쪽 공백 지우기 (strip)
a = "Life is too short"
print(a.strip())

# 1-10 문자열 바꾸기 (replace)
a = "Life is too short"
print(a.replace("Life", "Your leg"))
# replace(바뀌게 될 문자열, 바꿀 문자열)처럼 사용해서 문자열 안의 특정한 값을 다른 값으로 치환

# 1-11 문자열 나누기 (split)
a = "Life is too short"
print(a.split())

b="a:b:c:d"
print(b.split(':'))
#split 함수는 a.split()처럼 괄호 안에 아무 값도 넣어 주지 않으면 공백(스페이스, 탭, 엔터 등)을 기준으로 문자열을 나누어 준다.
#만약 b.split(':')처럼 괄호 안에 특정 값이 있을 경우에는 괄호 안의 값을 구분자로 해서 문자열을 나누어 준다. 이렇게 나눈 값은 리스트에 하나씩 들어가게 된다
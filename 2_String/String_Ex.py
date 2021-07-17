# 문자열(String) 문자, 단어 등으로 구성된 문자들의 집합

# 파이썬에서 문자열을 만드는 4가지 방법
print("Hello World")
print('Python is fun')
print("""Life is too short, Yon need python""")
print('''Life is too short, You need python''')

# 문자열 안에 작은따옴표나 큰따옴표를 포함시키고 싶을 때

# 문자열안에 작은 따옴표 포함시키기
# Python's favorite food is perl
# 반드시 큰따옴표로 둘러써야 한다
# 큰따옴표 안에 있는 작은따옴표는 문자열을 나타내기 위한 기호로 인식되지 않는다
food = "Python's favorite food is perl"
print(food)

# 문자열에 큰 따옴표 포함시키기
# "Python is very easy." he says.
# 작은 따옴표로 둘러싸기
say = '"Python is very easy." he says.'
print(say)

# 백슬래시 사용 작은따옴표, 큰따옴표 문자열 포함
food = 'Python\'s favorite food is perl'
say = "\"Python is very easy.\" he says."
print(food)
print(say)

# 여러 줄인 문자열을 변수에 대입하고 싶을 때

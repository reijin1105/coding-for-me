print(1+2)
name=input("당신의 이름은 무엇입니까?")
print("안녕하세요, "+name)

# 데이터 종류
# list []
list_a=[1,2,3]
print(list_a)
print(list_a[1])
list_a.append(4)
print(list_a)
print(list_a[0:4])
list_a.remove(2)
print(list_a)

# tuple ()
print("tuple")
print((1,2,3))
# 튜플은 리스트와 달리 안의 내용 변경 불가능

# dict {"key":"value"}
dict_a={"apple":"a type of fruits",
        "pen":"a type of write",
        "bread":"a type of food"
}
print(dict_a)
# 특정한 값을 찾고 싶을 떄 dict["특정 키 값"]
print(dict_a["apple"])
# 기존 dict에 밸류 값 변경하고 싶을 떄
dict_a["pen"]="somethong to write"
print(dict_a)

# set ({[])
set_a=set([1,2,3])
set_b=set([2,4,6])
print(set_a & set_b)
print(set_a | set_b)
print(set_a - set_b)
# set은 그 안에 중복값을 넣어도 하나의 값만 출력 [3,3,3]이면 3 하나만 나옴
# 집합간의 사칙연산 가능 (합집합, 교집합, 차집합, 여집합)

#참과 거짓 boolean
# if
# True False
# and, or, not
# 하나만 참(1)이어도 되면 True 1이 되고, 둘 다 참(1)이어야 하면 False(0)이 된다.

d=10
if d>10:
    print("숫자는 10보다 큽니다.")
elif d>5 and d<=10:
    print("숫자는 10보다 작거나 같습니다.")
else:
    print("숫자는 5보다 작거나 같습니다.")

# For, range
# while

for num in range(1,10):
    print(num)

num_list=[1,2,3,4,5,6,7,8,9,10]
for num in num_list:
    print(num)

# while True:  무한루프
a=1
while a<10:
    print(a)
    a=a+1

# 구구단 만들기

name=int(input("몇 단을 출력하시겠습니까?"))
for num in range(1,10):
    print("{}*{}={}".format(name,num,name*num))

# 1단에서 9단까지만 구구단

name2=int(input("몇 단을 출력하시겠습니까?"))
if name2>0 and name2<10:
    for num in range(1,10):
        print("{}*{}={}".format(name2,num,name2*num))
else:
    print("2에서 9사이의 숫자만 넣어주세요")

# 함수만들기
# 함수, 입력값(parameters), 변환값(return)

person1="민수"
person2="형식"
person3="진호"
person4="영진"
# 코드 4줄로짜기
print("안녕하세요, {}".format(person1))
print("안녕하세요, {}".format(person2))
print("안녕하세요, {}".format(person3))
print("안녕하세요, {}".format(person4))
#코드 한줄로 짜기
def hello_friends(person):
    print("hi, {}".format(person))

hello_friends(person1)
hello_friends(person2)
hello_friends(person3)
hello_friends(person4)

# 입력값 o 반환값 o
def sum(a,b):
    return(a+b)
# 입력값 o 반환값 x
def hello_friends(person):
    print("안녕하세요, {}".format(person))
# 입력값 x 반환값 o
def return_1():
    return_1
# 입력값 x 반환값 x
def hello_world():
    print("hello world.")

# 리스트에서 랜덤초이스
import random
group=[1,2,3,4,5]
print(random.choice(group))

# 튜플에서 랜덤초이스
import random
tuple=(1,2,3,4,5)
x=random.choice(tuple)
print(x)

# 클래스

title1="개발"
author1="마르코"
content1="개발은 쉬워요"
view_count1=0

title2="코칭"
author2="마르코"
content2="코칭은 쉬워요"
view_count2=0

title3="창업"
author3="마르코"
content3="창업은 쉬워요"
view_count3=0

# areticle class
class Article:
    title="개발"
    author="마르코"
    content="개발은 쉬워요"
    view_count=0

article1=Article()
print(article1.title)

article2=Article()
article2.title="코칭"
print(article1.title)
print(article2.title)

# article class with__init__
class Article():
    author="마르코"
    view_count=0

    def __init__(self,title,content):
        self.title=title
        self.content=content
    def read(self):
        self.view_count=self.view_count+1

article1=Article("개발","개발은 쉬워요")
article2=Article("코칭","코칭은 쉬워요")
article3=Article("창업","창업은 쉬워요")

print(article1.view_count)
article1.read()
print(article1.view_count)

# Article class inheritance 상속
class BrunchArticle(Article):
    source="브런치"

    def read(self):
        self.view_count=self.view_count+2

brunch_article=BrunchArticle("개발","개발은 쉬워요")
print(brunch_article.title)
print(brunch_article.source)
print(brunch_article.view_count)
brunch_article.read()
print(brunch_article.view_count)

# 미니과제2

class School():
    name="ㅇㅇ대학교"
    foundation="1930"
    address="서울시 영등포구 여의도동..."

school_article=School()
print(school_article.name)
print(school_article.foundation)
print(school_article.address)

# 에러처리, 예외처리
# ZeroDivisionError
def divided_by(first,second):
    return first/second  # 함수만들기

# print(divided_by(1,0)) # 제로디비젼에러 일어남

def divided_by(first,second):
    try:
        return first/second # 실행할 함수공식
    except ZeroDivisionError:
        return "0으로 나눌 수 없습니다."
        # 예상되는 에러를 이렇게 예외로 뺴서 다른 반응이 나오게
print(divided_by(1,0))
# 에러가 아니라 0으로 나눌 수없다는 문구 나옴

class EvenNumberDivisionError(Exception): # 클래스에서만 캐멀식표시
    pass
    # try와 except를 추가로 입력하지 않겠다.
def divide_by_odd_number(first,second):
    if second % 2 ==0: # 2로 나눴을 때 나머지가 없음
        raise EvenNumberDivisionError
        # 짝수로 나누면 일부러 에러를 일으킴
    else:
        return first/second

print(divide_by_odd_number(6,3))
# print(divide_by_odd_number(6,2)) 이븐넘버디비전에러 일어남

# 과제 1

name=input("한식, 중식, 일식 중 한가지를 고르세요.")

if name=="한식":
    import random
    group1=["일미식당","영자네분식","명인만두"]
    print(random.choice(group1))

elif name=="중식":
    import random
    group2=["양러우촨","라이라이","어향반점"]
    print(random.choice(group2))

elif name=="일식":
    import random
    group3=["산쵸메","이치란라멘","후쿠오카함바그"]
    print(random.choice(group3))

else:
    print("한식, 중식, 일식 중에 한 가지만 입력주세요")

# 과제 1 해답풀이

import random
# 1) 리스트를 만든다
Korean_food=["일미식당","영자네분식","명인만두"]
Chinese_food=["양러우촨","라이라이","어향반점"]
Japanese_food=["산쵸메","이치란라멘","후쿠오카함바그"]
# 2) 사용자로부터 입력
user_choice=input("한식, 중식, 일식 중 한가지를 고르세요.")

# 3) 임의로 추천
if user_choice=="한식":
    choice_result=random.choice(Korean_food)
    # choice_result=Korean_food(random.randomint(0,len(Korean_food)))
elif user_choice=="중식":
    choice_result=random.choice(Chinese_food)
elif user_choice=="일식":
    choice_result=random.choice(Japanese_food)
else:
    print("한식, 중식, 일식 중에 하나만 입력해 주세요.")

if choice_result:
    print("{} 중에서 {}이(가) 선택되었습니다. ".format(user_choice,choice_result))

# 과제 2

# 사람 기본요소 입력
name=input("성함이 어떻게 되십니까?")
age=input("나이는 어떻게 되십니까?")
gender=input("성별이 어떻게 되십니까?")

class Human():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
human_article=Human(name,age,gender)

# 동료의 기본직급은 대리 (상속이용)
class Colleague(Human):
    position="대리"
colleague_article=Colleague(name,age,gender)
print("안녕하세요, {}세/{}/{} {}님.".format(age,gender,name,Colleague.position))

# 직급변경
position=input("직급이 어떻게 되십니까?")
class Colleague(Human):
    def __init__(self,position):
        self.position=position
colleague_article=Colleague(position)
print("안녕하세요, {}세/{}/{} {}님.".format(age,gender,name,position))

# 과제 2 해답풀이

# 1) 사람클래스
class Person:
# 이름, 나이, 성별
# 2) 새로만들 때 입력
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
# 3) 직장동료 클래스
# 상속
class Colleague(Person):
    position="대리"
# 4) 새로만들 때 입력
    def __init__(self,name,age,gender,position):
        super().__init__(name,age,gender) # 부모클래스의 요소를 전부 가져옴
        self.position=position

colleague=Colleague("미미",20,"Female","대리")
# cmd에서 입력받지는 않았지만 편집기 안에서 만들어짐
# 만약 colleague=Colleague()만 입력하면 오류
# 왜? 클래스 안에는 이름, 나이, 성별, 직급을 넣어야 출력되게 했으므로
print(colleague.__dict__)
# 위에 만들어진 항목을 딕셔너리 형태로 전부 보여줌
# 만약 print(colleague.name)라고 치면 '미미' 출력

# 과제 3

import random
ai=["바위","가위","보"]
a=0
b=0
while a<3 or b<3:
    user=input("가위바위보 게임을 시작합니다. 무엇을 내시겠습니까?")
    if user=="바위":
        computer_choice = random.choice(ai)
        if computer_choice=="바위":
            print("비겼습니다.")
        if computer_choice=="가위":
            print("이겼습니다.")
            a=a+1
        if computer_choice=="보":
            print("졌습니다.")
            b=b+1
    if user=="가위":
        computer_choice = random.choice(ai)
        if computer_choice=="보":
            print("졌습니다.")
            b=b+1
        if computer_choice=="가위":
            print("비겼습니다.")
        if computer_choice=="보":
            print("이겼습니다.")
            a=a+1
    if user=="보":
        computer_choice = random.choice(ai)
        if computer_choice=="바위":
            print("이겼습니다.")
            a=a+1
        if computer_choice=="가위":
            print("졌습니다.")
            b=b+1
        if computer_choice=="보":
            print("비겼습니다.")

    if a==3:
        print("{}:{}으로 플레이어가 이겼습니다.".format(a,b))
        break
    if b==3:
        print("{}:{}으로 플레이어가 졌습니다.".format(a,b))
        break

# 과제 3 해답풀이
import random
Rock="바위"
Scissors="가위"
Paper="보"
RSP_List=[Rock,Scissors,Paper]

win_count=0
lose_count=0

while win_count<3 and lose_count<3:
# 1) 사용자 입력
    user_choice=input("{},{},{}: ".format(Scissors,Rock,Paper))
# 2) 컴퓨터 임의선택
    computer_choice=random.choice(RSP_List)
# 3) 승패확정
    if user_choice==computer_choice:
        print("비겼습니다.")
    elif ((user_choice==Rock and computer_choice==Scissors)
        or(user_choice==Scissors and computer_choice==Paper)
        or(user_choice==Paper and computer_choice==Rock)):
        print("이겼습니다.")
        win_count=win_count+1
    elif user_choice not in RSP_List:
        ("가위, 바위, 보 중에서 하나를 입력해 주세요.")
    else:
        print("졌습니다.")
        lose_count=lose_count+1
if win_count==3:
    print("사용자가 최종승리 하였습니다.")
else:
    print("컴퓨터가 최종승리 하였습니다.")

# 과제 4 해답풀이

for a in range(1,6):
    print("1"*a)
# 1
# 11
# 111
# 1111
# 11111 이렇게 출력됨

for a in range(1,6):
    print("1"*a + "0"*(5-a))
# 각 행에 1이 차지하는 부분을 뺀 나머지 부분을 0으로 채움
# 10000
# 11000
# 11100
# 11110
# 11111 이렇게 출력됨

for a in range(1,6):
    a=a-3
    if a<0:
        a=-a   # a가 음수가 되면 양수로 처리
    print("0"*a + "1"*(5-a*2) + "0"*a)
# a=1, a는 -2에서 2로 변환  00100
# a=2, a는 -1에서 1로 변환  01110
# a=3, a는 0  11111
# a=4, a는 1  01110
# a=5, a는 2  00100

# 과제 5
# 에러처리 이용
def gugudan():
    try:
        dan=int(input("2에서 9사이의 숫자를 입력해 주세요."))
        if dan>2 and dan<10:
            for num in range(1,10):
                print("{}*{}={}".format(dan,num,dan*num))
        else:
            print("2에서 9사이의 숫자만 입력해주세요!!!")
            gugudan()
    except ValueError:
        print("숫자만 입력해주세요.")
        gugudan() # 재귀함수: while처럼 반복해서 함수수행
    except:
        print("알 수 없는 에러가 발생하였습니다.")
        gugudan() # 재귀함수
gugudan()

coffee = 'americano' #str

#내장 함수[int(), str(), float(), bool(), list(), print(), input()]
#len(): 길이을 알려주는 기능

print(len(coffee))

coffee.upper()  #AMERICANO
coffee.lower() #americano
coffee.capitalize() #Americano
coffee.strip() # 빈공간 없애기
coffee.find('c') # 몇 번째에 'c'가 있니? 5    # 없으면 -1
coffee.replace('cano','can') #왼쪽에서 오른쪽으로 바꾸기
coffee.count('a') #'a' 몇 개인지   #없으면 -1

#Quiz1
x = input("소문자로 된 문자열을 입력하시오.:")
print(x.upper())

#Quiz2
lyrics = '''
Memories follow me left and right
I can feel you over here I can feel you over here
you take up every corner of my mind
whatcha gon do now
ever since the da day y-you went away
no I don't know how
how to erase your body from out my brain
whatcha gon do now
maybe I should just focus on me instead
But all I think about
are the nights we were tangled up in your bed
oh no (oh no)
oh no (oh no)
you're going round in circles got you stuck up in my head (yeah)
Memories follow me left and right
I can feel you over here I can feel you over here
you take up every corner of my mind
your love stays with me day and night
I can feel you over here I can feel you over here
you take up every corner of my mind
whatcha gon do now
ever since the da da day y-you went away
someone tell me how
how much more do I gotta drink for the pain
whatcha gon do now
you did things to me that I just can't forget
now all I think about
are the nights we were tangled up in your bed
oh no (oh no)
oh no (oh no)
you're going round in circles got ya stuck up in my head
Memories follow me left and right
I can feel you over here I can feel you over here
you take up every corner of my mind
your love stays with me day and night
I can feel you over here I can feel you over here
you take up every corner of my mind
whatcha gon do now
did ya know you're the one that got away
and even now baby i'm still not ok
did ya know that my dreams they're are the same
everytime I close my eyes
Memories follow me left and right
I can feel you over here I can feel you over here
you take up every corner of my mind
whatcha gon do now
your love stays with me day and night
I can feel you over here i can feel you over here
you take up every corner of my mind
whatcha gon do now
I can feel you over here I can feel you over here
you take up every corner of my mind
whatcha gon do now
'''

print(f"left: {lyrics.count('left')}번, rigth: {lyrics.count('right')}번")
print(f"가사의 길이는 {len(lyrics)} 입니다.")


a = "mega"
b = "study"
c = a + b  #megastudy, + 문자열 연결 연산자
d = a * 3 #megamegamega * 문자열 반복 연산자
e = a[0]  #m, [] 문자열 인덱싱
f = b[0:3]  #stu, [start:end] 문자열 슬라이싱, end 제외(0번째부터 (end-1)번째까지)
g = 'g' in a #'mega'에서 g가 있니? 결과 : True or False

title = "megastudy python programming"
print(title.split()) #빈 공간 기준으로 str에서 list 만들어주기

title1 = "orange, apple, banana"
print(title.split(','))

#user한테 이메일 주소를 입력받고 -> ['유저 아이디', '도메인']
#ex) python@megastudy.com ['python', 'megastudy.com']

user = input("이메일 주소를 입력하시오.:")
list = user.split("@")
print(list)  #['python', 'megastudy.com']

# ['python', 'megastudy', 'com']
a = list[1].split('.') #['megastudy', 'com']
list[1] = a[0]
#list[2] = a[1] list[2]가 없으므로 안됨
list.append(a[1])
print(list)

#join
word = ' '.join(['ice', 'cream'])   # 'ice cream'

id = input("아이디 입력:")
domain = input("도메인 입력:")
print('@'.join([id, domain]))

article = '''
My life's been magic seems fantastic
I used to have a hole in the wall with a mattress
It's funny when you want it
Suddenly you have it
You find out that your gold's just plastic
Every day every night
I've been thinking back on you and I
Every day every night
I worked my whole life
Just to get right just to be like
Look at me I'm never coming down
I worked my whole life
Just to get high just to realize
Everything I need is on the
Everything I need is on the ground
On the ground
Everything I need is on the ground
Nah but they don't hear me though (Yeah what goes up it must come down)
Nah but they don't hear me though (You're running out of time)
My world's been hectic seems electric
But I've been waking up with your voice in my head
And I'm trying to send a message
And let you know that every single minute I'm without you I regret it
Every day every night
I've been thinking back on you and I
Every day every night
I worked my whole life
Just to get right just to be like
Look at me I'm never coming down
I worked my whole life
Just to get high just to realize
Everything I need is on the
Everything I need is on the ground
On the ground
Everything I need is on the ground
Nah but they don't hear me though (Yeah what goes up it must come down)
Nah but they don't hear me though (You're running out of time)
I'm way up in the clouds
And they say I've made it now
But I figured it out
Everything I need is on the ground
Just drove by your house
So far from you now
But I figured it out
Everything I need is on the
Everything I need is on the ground
On the ground
Everything I need is on the ground
Nah but they don't hear me though
On the ground
Nah but they don't hear me though
Everything I need is on the ground
'''

newArticle = article.replace('ground', 'world').replace('everything','anything')
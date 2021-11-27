
# first lesson
# ________________________________________________
# number = 5
# int = integer = butun son e.g: 1,2,3,4,5,6,7,8,9...
# float = residual number = qoldiqli sonlar e.g: 1.2 ; 2.5 ...
# modul = 45 % 6 
# print(modul) # 3 (it prints residues)
# devide = 3 / 2
# print(devide)
# // #(it gives integer)


# ________________________________________________
day = "friday"
tomorrow = " saturday"
result = day + tomorrow
print(result)
result = day * 10
print(result)
# devide & minus are imposible to solve


# list_________________________________________
test1 = [1,2,3,4,5,6,7,8,9]
test2 = ["Monday","Tuesday"]

test = test1 + test2
test1[0] = 2
test = test1 + test2
test.append(571) #it can add smth new at the end
test.pop() #it can remove from the end 
test[2:4] = [] #remove from at the beginning 
test[:2] = ["hello" , "world"]
print(test)

# working with append
user = ['me']
# user.append() append is only able to add one argument !!!!
user[1:] = ['sister' , 'brother' , 'mum' , 'dad']
print(user)
print("Good morning,Have a nice day")
# versiyani tekshirish terminalda python -V yozamiz

print(9**2) #darajaga ko`tarish

print("\"Nexia\" , \"Tico\" , \'Damas\' ko`rganlar qilas havas ")
print(5**4)
print("qoldiq:",22%4)
a = 125
res1 = a*a
res2 = a + a + a + a
print('s=',res1 , 'p=',res2)

d = 12
res3 = d * 3.14
print('surface of the circle', res3)

k1 = 6
k2 = 7
res4 = (k1**2) + (k2**2)
print(res4)

name = "Saidali"
age = 18
print(name)
print(age)

simple = "Hello World"
print(simple)

text = "assalomu alaykum"
text = "va alaykum assalom"
print(text)

# class = "wrong"
# print(class)

taple = (4,5,'monday')
taple1 = taple[:2] #slicing
addingTaples = taple + taple1 #taplelarni qo`shish`
print(addingTaples)

multiply = taple * 5 #ko`paytirish
# del multiply
print(multiply)

# dictionaries
# {'key': 'text'}
c1 = {1:['Monday' ,12 ,'meee'] , 2:'Tuesday' , 3:'Wednesday'}
print(c1[1][2])

# loops
# for & while

for i in range(3):
    print(1)

friends = ['Said', 'Ali', 'Xon']
for a in friends:
    print(a)

text1 = "Saidali"
for k in text1:
    print(k)
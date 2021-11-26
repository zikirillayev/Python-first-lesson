
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


# In addition
var = "Hello world"
print(var)
if var:
    print(True)
else:
    print(False)

List = ['any', 'data', True, 6, 'type', 'can', {'find': 'here'}]
Dict = {
    'name': "Saidali",
    'surname': "Zikirillayev",
    'isMarried': False,
    'language': "Python"
}
print(List)
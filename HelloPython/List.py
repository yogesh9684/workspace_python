''''''''''''''''''''''
x=("Yogesh Pradeep Viraj")
y=x.split()
print(y)

k=['Yogesh', 'Pradeep', 'Viraj']
print(k[1])
k[1]="Aaba"
print(k)
print(len(k))
k.append("Akshay")
print(k)
k.insert(0,"Amol Bapu")
print(k)

List1=['Amol Bapu', 'Yogesh', 'Aaba', 'Viraj', 'Akshay']
List1.pop()
print(List1)

List1.pop(3)
print(List1)

List1.remove("Yogesh")
print(List1)

r=List1.index("Aaba")
print(r)
'''''''''''''''''''''''''''''
# l=[1, 2, 3, 2, 1, 2]
# #j=l.count(1)
# #print(j)
#
# print(len(l))
# print(count(l))

# a = range(10,20)
# print(list(a))
#
# List1 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# Test1=max(List1)
# print(Test1)
#
# Test2=min(List1)
# print(Test2)

X = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
for i in X:
    print("Multilcation of" , str(i),"is",i*10)
import keyword
print("Hello World")
List1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
List1.remove('f')
print(List1)
List1.append('y')
print(List1)
List1.insert(5, 'f')
print(List1)
#List1.clear()
#print(List1)
List1.reverse()
print(List1)
List1.pop(5)
print(List1)
print(keyword.kwlist)
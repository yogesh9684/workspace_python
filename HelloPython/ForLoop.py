x = [1,2,3,4,5,6,7,8,9]
for i in x:
    print('muiplication of', str(i), "is", i*10)


# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     t=x.upper()
#     print(t)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x=="cherry":
      break
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

for x in range(6):
  print(x)
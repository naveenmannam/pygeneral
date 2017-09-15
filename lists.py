list_1 = [2, 3, 4, 5, 6]
list_2 = []

for i in range(len(list_1)):
    list_2.append(list_1[i])

print(list_1)
print(list_2)

list_1[0] = 23

print(list_1)
print(list_2)

print("----------------")

list_1 = [2, 3, 4, 5, 6]
list_2 = [] + list_1


print(list_1)
print(list_2)

list_1[0] = 23

print(list_1)
print(list_2)

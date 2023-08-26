user = input('Input:') # Input use ',' between numerals, Example 1,2,3,4,5,6

list = user.split(',')
print(list)

for i in range(len(list)):
    list[i] = int(list[i])
print(list)

# list = [1,2,3,4,5,6]
pwr = []

for x in list:
    if x % 2 == 0:
        y = x**2
        pwr.append(y)

print(pwr)
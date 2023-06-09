arr = []
my_array = [0] * 6
length = 0

# Add elements to array
for i in range(6):
    arr.append(i + 1)

print(arr)

for i in range(3):
    my_array[i] = i + 2

my_array.insert(0, 1)
my_array.pop()
print(my_array)
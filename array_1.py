import array as arr
num1=arr.array('d', [1.34, 2.76, 3.55, 4.1, 5.09])
print("Original array:", num1)
num = arr.array('i', [10, 20, 30, 40])
print("Original array:", num)

num.append(50)
print("After append(50):", num)

num.insert(2, 25)
print("After insert(2, 25):", num)

num.remove(20)
print("After remove(20):", num)

num.pop()
print("After pop():", num)

num.reverse()
print("After reverse():", num)

print("Index of 30:", num.index(30))

print("Count of 10:", num.count(10))

num.tolist()
print("Array as list:", num.tolist())

num.buffer_info()
print("Buffer info:", num.buffer_info())
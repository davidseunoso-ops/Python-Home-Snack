import random

numbers = []
for index in range(10):
    numbers.append(random.randint(1, 50))
print(numbers)

length = 0
for count in numbers:
    length = length + 1
print("length:", length)

even_sum = 0
for index in range(length):
    if index % 2 == 0:
        even_sum = even_sum + numbers[index]
print("even position sum:", even_sum)

odd_sum = 0
for index in range(length):
    if index % 2 == 1:
        odd_sum = odd_sum + numbers[index]
print("odd position sum:", odd_sum)

multiple = 1
for index in range(length):
    if index % 3 == 2:
        multiple *= numbers[index]
print("every third product:", multiple)


total = 0
for count in numbers:
    total = total + count
average = total / length
print("average:", average)

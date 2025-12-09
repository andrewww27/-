numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
index_none = numbers.index(None)

sum_without_none = 0
for x in numbers:
    if x is not None:
        sum_without_none += x

total_count = len(numbers)
medium = sum_without_none / (total_count)
numbers[index_none] = medium


print("Измененный список:", numbers)

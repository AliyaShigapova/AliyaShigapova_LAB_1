numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

total = sum(number for number in numbers if number is not None)

count = len(numbers)

average = total / count

numbers = [average if number is None else number for number in numbers]

print("Измененный список:", numbers)

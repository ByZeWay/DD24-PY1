numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

s = sum(n for n in numbers if n is not None)
avg = s / (len(numbers))

numbers = [avg if n is None else n for n in numbers]

print("Измененный список:", numbers)

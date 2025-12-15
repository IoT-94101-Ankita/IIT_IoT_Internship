text = input("Enter a string: ")
start = int(input("Enter start index: "))
end = int(input("Enter end index: "))
step = int(input("Enter step value: "))

result = text[start:end:step]

print("Sliced string:", result)
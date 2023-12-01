import regex as re

numbers = []
with open("1-input.txt", "r") as file:
    for line in file.readlines():
        digits = re.findall("[0-9]", line, overlapped=True)
        number = (digits[0] + digits[-1])
        numbers.append(int(number))

print(numbers)
print(sum(numbers))

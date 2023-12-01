import regex as re

numbers = []
with open("1-input.txt", "r") as file:
    for line in file.readlines():
        digits = re.findall("[1-9]|one|two|three|four|five|six|seven|eight|nine", line, overlapped=True)
        first = digits[0]
        last = digits[-1]

        print(digits, first, last)
        number = (first + last).replace("one", "1").replace("two", "2").replace("three", "3").replace("four", "4").replace("five", "5").replace("six", "6").replace("seven", "7").replace("eight", "8").replace("nine", "9").replace("zero", "0")
        print(number)
        numbers.append(int(number))

print(numbers)
print(sum(numbers))

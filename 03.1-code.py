import regex as re

search_pattern = re.compile("[0-9]+")
with open("3-input.txt", "r") as file:
    lines = [line.replace("\n", "") for line in file.readlines()]

    total = 0

    for i in range(len(lines)):
        line = lines[i]
        print(f"line {i}")
        start_index = 0
        while match := search_pattern.search(line, start_index):
            print(match)
            start, end = match.span()
            start_index = end
            num = line[start:end]

            start = max(start - 1, 0)
            end = min(end, len(line) - 1)
            found = False
            if line[start] not in "0123456789.":
                total += int(num)
                found = True
            print(line[end])
            if (line[end] not in "0123456789.") and (not found):
                total += int(num)
                found = True
            if i > 0 and not found:
                above = lines[i - 1]
                for j in range(start, end + 1):
                    if above[j] not in "0123456789.":
                        total += int(num)
                        found = True
                        break
            if i < len(lines) - 1 and not found:
                below = lines[i + 1]
                for j in range(start, end + 1):
                    if below[j] not in "0123456789.":
                        total += int(num)
                        found = True
                        break
            if found:
                print(num)
            else:
                print(f"failed on {num}")
    print(total)
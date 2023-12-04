import regex as re

gear_pattern = re.compile("\\*")
num_pattern = re.compile("[0-9]+")
with open("3-input.txt", "r") as file:
    lines = [line.replace("\n", "") for line in file.readlines()]

    potential_gears = []
    for y, line in enumerate(lines):
        start_index = 0
        while match := gear_pattern.search(line, start_index):
            potential_gears.append((match.start(), y))
            start_index = match.end()

    numbers = []
    for y, line in enumerate(lines):
        line_list = []
        start_index = 0
        while match := num_pattern.search(line, start_index):
            start, end = match.span()
            line_list.append((int(line[start:end]), start, end, y))
            start_index = end
        numbers.append(line_list)

    print(potential_gears)
    print(numbers)
    # return
    total = 0

    for x, y in potential_gears:
        print(f"---------------------- {x} - {y} ---")
        neighbor_positions = [(x + a, y + b) for a, b in [
            (-1, -1), (0, -1), (1, -1),
            (-1,  0),          (1,  0),
            (-1,  1), (0,  1), (1,  1),
        ]]
        matched_numbers = set()
        for nx, ny in neighbor_positions:
            numbers_on_line = numbers[ny]
            for number, start, end, line_num in numbers_on_line:
                if start <= nx < end:
                    print(f"Hit {number} {start} {end} {nx}")
                    matched_numbers.add((number, start, end, line_num))

        if len(matched_numbers) == 2:
            total += matched_numbers.pop()[0] * matched_numbers.pop()[0]

    print(total)
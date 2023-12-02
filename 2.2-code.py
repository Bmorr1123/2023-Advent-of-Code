

sum_of_powers = 0

with open("2-input.txt", "r") as file:
    for line in file.readlines():
        game_str, pulls_str = line.split(":")
        game_num = int(game_str[game_str.find(" ") + 1:])

        failed = False

        maxes = {"red": 0, "green": 0, "blue": 0}

        for pull in pulls_str.split(";"):
            for count in pull.split(","):
                count = count.strip()
                color = count[count.find(" ") + 1:]
                count = int(count[0:count.find(" ")])

                maxes[color] = max(maxes[color], count)

        power = 1
        for color_count in maxes.values():
            power *= color_count

        sum_of_powers += power

print(sum_of_powers)

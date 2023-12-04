
counts = {
    "red": 12,
    "green": 13,
    "blue": 14
}


sum_of_games = 0

with open("2-input.txt", "r") as file:
    for line in file.readlines():
        game_str, pulls_str = line.split(":")
        game_num = int(game_str[game_str.find(" ") + 1:])

        failed = False

        for pull in pulls_str.split(";"):
            for count in pull.split(","):
                count = count.strip()
                color = count[count.find(" ") + 1:]
                count = int(count[0:count.find(" ")])

                if counts[color] < count:
                    failed = True
                    break
            if failed:
                break
        if failed:
            continue

        sum_of_games += game_num

print(sum_of_games)
import regex as re

with open("04-input.txt", "r") as file:

    # Breaking down the cards into 3 lists.
    #   1) Before the colon
    #   2) Winning #'s
    #   3) Card #'s
    cards = [[re.split(" +", section.strip()) for section in re.split(":|\\|", line.replace("\n", ""))] for line in file.readlines()]
    total_value = 0
    for card_info, winning_numbers, card_numbers in cards:
        card_value = 0
        # print(card_info, winning_numbers, card_numbers)
        for number in card_numbers:
            if number in winning_numbers:
                if card_value == 0:
                    card_value = 1
                else:
                    card_value *= 2
        total_value += card_value
    print(total_value)

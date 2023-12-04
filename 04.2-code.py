import regex as re

with open("04-input.txt", "r") as file:

    # Breaking down the cards into 1 number and 3 lists.
    #   0) A single # containing the number of copies
    #   1) Before the colon
    #   2) Winning #'s
    #   3) Card #'s
    cards = [[1] + [re.split(" +", section.strip()) for section in re.split(":|\\|", line.replace("\n", ""))] for line in file.readlines()]

    for copies, card_info, winning_numbers, card_numbers in cards:
        card_number = int(card_info[1])
        matches = 0
        for number in card_numbers:
            if number in winning_numbers:
                matches += 1

        # For each match, we add one card_number we will be "copying" in the for loop
        for copy_card_num in range(card_number, card_number + matches):
            if copy_card_num < len(cards):
                cards[copy_card_num][0] += copies  # For each copy of current, we add another copy to copied card
                print(f"Copying card #{copy_card_num + 1}\n\tCopies: {cards[copy_card_num][0]}")

    print(sum([copies for copies, *_ in cards]))

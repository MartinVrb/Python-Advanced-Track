cards_list = input().split()
faro_shuffles_count = int(input())

for loops in range(faro_shuffles_count):
    mid_index = len(cards_list) // 2
    first_half_list = cards_list[:mid_index]
    second_half_list = cards_list[mid_index:]
    deck_after_shuffling = []

    for card_index in range(mid_index):
        deck_after_shuffling.append(first_half_list[card_index])
        deck_after_shuffling.append(second_half_list[card_index])

    cards_list = deck_after_shuffling

print(cards_list)

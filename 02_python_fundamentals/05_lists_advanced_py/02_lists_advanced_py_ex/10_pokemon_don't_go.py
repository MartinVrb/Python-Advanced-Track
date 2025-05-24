def pokemon(distances:list):
    sum_of_removed_elements = 0
    while len(distances) > 0:
        index = int(input())
        if index < 0:
            removed_element = distances.pop(0)
            distances.insert(0, distances[-1])
        elif index > len(distances) - 1:
            removed_element = distances.pop()
            distances.insert(len(distances), distances[0])
        else:
            removed_element = distances.pop(index)

        sum_of_removed_elements += removed_element

        distances = [num + removed_element if num <= removed_element else num - removed_element for num in distances]

    return sum_of_removed_elements

print(pokemon(list(map(int, input().split()))))

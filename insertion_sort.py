def insertion_sort(list: list[int]):
    length = len(list)

    for i in range(1, length):
        temp = list[i]
        j = i - 1

        while j >= 0 and list[j] > temp:
            list[j + 1] = list[j]
            j -= 1
        
        list[j + 1] = temp
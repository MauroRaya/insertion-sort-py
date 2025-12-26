def insertion_sort(list: list[int]):
    length: int = len(list)

    for i in range(1, length):
        temp: int = list[i]

        for j in range(i - 1, -1, -1):
            if list[j] > temp:
                list[j + 1] = list[j]
                list[j] = temp
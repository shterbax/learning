def common_elements():
    first_r = range(3, 100, 3)
    first_set = {0, }

    for n in first_r:
        first_set.add(n)

    second_r = range(5, 100, 5)
    second_set = {0, }

    for n in second_r:
        second_set.add(n)

    return first_set.intersection(second_set)


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}

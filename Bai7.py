def check_same_frequency(list1, list2):
    count1 = {}
    count2 = {}

    for item in list1:
        count1[item] = count1.get(item, 0) + 1

    for item in list2:
        count2[item] = count2.get(item, 0) + 1

    return count1 == count2

list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]
print(check_same_frequency(list1, list2))

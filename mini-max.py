def mini_max(array):
    sums = 0
    max_1 = 0
    for x in range(0, array.__len__()):
        for j in range(0, array.__len__()):
            if x != j:
                sums += array[j]
            else:
                continue
        if sums > max_1 or sums == max_1:
            max_1 = sums
        sums = 0
    return max_1


def minis(array):
    sums = 0
    mini = mini_max(array)
    for x in range(0, array.__len__()):
        for j in range(0, array.__len__()):
            if x != j:
                sums += array[j]
            else:
                continue
        if sums < mini or sums == mini:
            mini = sums
        sums = 0
    return mini


array_size = int(input("Enter array size : "))
collection = []
for i in range(0, array_size):
    values = int(input("Enter elements : "))
    collection.append(values)
result = mini_max(collection)
result2 = minis(collection)
print "Max ->", result, "&", "Minimum -> ",result2

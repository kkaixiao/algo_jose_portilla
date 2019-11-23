
def finder(arr1, arr2):
    counter = {}
    for item in arr1:
        if item not in counter:
            counter[item] = 1
        else:
            counter[item] += 1

    for item in arr2:
        counter[item] -= 1

    for k,v in counter.items():
        if v > 0:
            return k



arr1 = [1, 2, 3, 4, 5, 6, 7]
arr2 = [3, 7, 2, 1, 4, 6]
print(finder(arr1, arr2))

def finder(arr1, arr2):
    result = 0

    for num in arr1 + arr2:
        result ^= num
        print(result)
    return result


arr1 = [1, 2, 3, 4, 5, 6, 7]
arr2 = [3, 7, 2, 1, 4, 6]

# arr1 = [5, 5, 7, 7]
# arr2 = [5, 7, 7]
print(finder(arr1, arr2))




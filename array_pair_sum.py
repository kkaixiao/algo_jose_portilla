def pair_sum(arr, k):
    count = 0
    for i in range(len(arr)-1):
        j = i+1
        while j < len(arr):
            if (arr[i] + arr[j]) == k:
                print(arr[i], arr[j])
                count += 1
            j += 1
    return count

arr1 = [1,3,2,2]
k1 = 4

print(pair_sum(arr1, k1))
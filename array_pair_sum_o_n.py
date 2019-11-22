def pair_sum(arr, k):
    if len(arr) < 2:
        return

    seen = set()
    output = set()

    for num in arr:
        target = k - num

        if target not in seen:
            seen.add(num)
        else:
            output.add( ((min(num, target)), max(num, target)) )
    print(output)
    return len(output)

arr1 = [1,3,2,2]
k1 = 4

print(pair_sum(arr1, k1))
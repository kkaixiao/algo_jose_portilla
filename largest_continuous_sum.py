def large_cont_sum(arr):
    len_arr = len(arr)
    result_arr=[]
    for i in range(len_arr):
        one_sum = 0
        for j in range(i, len_arr):
            one_sum = one_sum + arr[j]
            one_result = (i, j, one_sum)
            result_arr.append(one_result)

    large_num = result_arr[0][2]
    large_start = result_arr[0][0]
    large_end = result_arr[0][1]
    for item in result_arr:
        if large_num < item[2]:
            large_num = item[2]
            large_start = item[0]
            large_end = item[1]

    #print(large_num, large_start, large_end)
    return large_num

arr1 = [1, 2, -1, 3, 4, 10, 10, -10, -1]

large_cont_sum(arr1)
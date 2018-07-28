def shifted_arr_search(shiftArr, num):
    # find 0 (might not be there)
    start = 0
    end = len(shiftArr)

    def binary_search(l, r, target):
        while l < r:
            m = (l + r) // 2
            if shiftArr[m] == target:
                return m
            if shiftArr[m] < target:
                l = m + 1
            else:
                r = m
        return -1

    # find the pivot
    # [3, 5, 6, 1, 2]
    #           ^    here is the pivot

    pivot = 0
    while start < end:
        mid = (start + end) // 2
        if mid == 0 or shiftArr[mid-1] > shiftArr[mid]:
            pivot = mid
            break
        # [1, 2, 3, 4, 0]
        if shiftArr[start] < shiftArr[mid]:
            start = mid
        # [9, 2, 3, 4, 5]
        else:
            end = mid

    if pivot == 0 or shiftArr[0] > num:
        return binary_search(pivot, len(shiftArr), num)
    return binary_search(0, pivot, num)


print(shifted_arr_search([], 17))
print(shifted_arr_search([1], 1))
print(shifted_arr_search([0, 1, 2, 3], 2))
print(shifted_arr_search([1, 2, 3], 1))
print(shifted_arr_search([0, 1, 2, 3], 1))
print(shifted_arr_search([9,12,17,2,4,5], 17))
print(shifted_arr_search([9,12,17,2,4,5,6], 4))
print(shifted_arr_search([1, 2, 3, 4, 5, 0], 0))


def partitionmid(arr, left, right):
    # partitions the array using the mid point
    # because variable right is the length, and we're going form length to index, we subtract 1
    arrlen = (right - left - 1)
    midindex = ((arrlen // 2) + left)
    # we get the mid index at which the "middle" pivot value is located at
    # we then get the potential pivot points, and then we choose the "middle" out of them
    potentialpivot = [arr[left], arr[midindex], arr[right-1]]
    potentialpivot.sort()
    pivotVal = potentialpivot[1] # selects the middle value as outlined in the problem

    # we then find this index within the array, in order to do the swaps
    pivotIndex = arr.index(pivotVal)
    pivot = arr[pivotIndex]
    # we then swap this value, and do the partitioning as done before
    arr[pivotIndex] = arr[left]
    arr[left] = pivot

    i = left + 1
    for j in range(left + 1, right):
        # we swap their positions
        if arr[j] < pivot:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
            i += 1
    # at the end we swap the pivot point with where the i is located along the array

    arr[left] = arr[i - 1]
    arr[i - 1] = pivot
    return i - 1


def quicksort(arr, left, right):
    global comparisons
    if right > left:
        comparisons += right - left - 1
        index = partitionmid(arr, left, right)
        arr1 = quicksort(arr, left, index)
        arr2 = quicksort(arr, index + 1, right)


if __name__ == '__main__':
    # List = open("IntegerArray.txt").readlines()
    # int_list = [int(i) for i in List]
    # mylist, inversions = countInversions(int_list)
    # print(inversions)
    f = open("QuickSort.txt").readlines()
    myarr = [int(i) for i in f]
    comparisons = 0
    length = len(myarr)
    quicksort(myarr, 0, length)

    print(comparisons)

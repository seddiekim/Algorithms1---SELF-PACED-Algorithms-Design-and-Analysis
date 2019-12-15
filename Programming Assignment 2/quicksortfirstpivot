def partitionfirst(arr, left, right):
    # first element of the array is used as a pivot
    pivot = arr[left]
    i = left + 1
    for j in range(left+1, right):
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
        index = partitionfirst(arr, left, right)
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

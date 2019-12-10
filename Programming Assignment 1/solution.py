
# divide
def countInversions(array=[]):
    if len(array) <= 1:
        return array, 0
    mid = len(array) // 2
    left, leftInv = countInversions(array[:mid])
    right, rightInv = countInversions(array[mid:])
    mergedList, count = merge(array, left, right)
    count += leftInv + rightInv
    return mergedList, count

# and conquer?
def merge(mylist=[], leftArr=[], rightArr=[]):
    if len(mylist) >= 1:
        # divides the input array into two, recursively
        mid = len(mylist) // 2
        i = j = k = 0
        inversions = 0
        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i] <= rightArr[j]:
                mylist[k] = leftArr[i]
                i += 1
                k += 1
            else:
                mylist[k] = rightArr[j]
                # this is where the inversion count occurs, if the value at the right array is greater than
                # that of the left array (inversion)
                inversions += mid - i
                j += 1
                k += 1

        while i < len(leftArr):
            mylist[k] = leftArr[i]
            i += 1
            k += 1
        while j < len(rightArr):
            mylist[k] = rightArr[j]
            j += 1
            k += 1

        return mylist, inversions


if __name__ == '__main__':
    List = open("IntegerArray.txt").readlines()
    int_list = [int(i) for i in List]
    mylist, inversions = countInversions(int_list)
    print(inversions)


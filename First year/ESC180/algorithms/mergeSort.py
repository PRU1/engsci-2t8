L = [1,4,9,2,4,5]

# merge sort
def mergeSort(L):
    # DIVIDE LIST
    if len(L) == 1:
        return L
    mid = len(L) // 2
    leftList = L[:mid]
    rightList = L[mid:]
    sortedLeft = mergeSort(leftList)
    sortedRight = mergeSort(rightList)

    # combine lists 
    return combineLists(sortedLeft, sortedRight)

def combineLists(left, right):
    # sweep left to right and MERGE
    # I wish python had better for loops : (
    rIndex = 0
    lIndex = 0
    combined = []
    while (rIndex < len(right) and lIndex < len(left)):
        # do pairwise comparison
        if left[lIndex] < right[rIndex]:
            combined.append(left[lIndex])
            lIndex += 1
        elif right[rIndex] < left[lIndex]: # this is redundant, will be handled in else 
            combined.append(right[rIndex])
            rIndex += 1
        else:
            combined.append(right[rIndex])
            combined.append(left[lIndex])
            rIndex += 1; lIndex += 1

    # handle any leftovers
    combined.extend(left[lIndex:])
    combined.extend(right[rIndex:])

    return combined

print(mergeSort(L))
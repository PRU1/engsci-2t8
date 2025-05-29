def match_pattern(list1, list2):
    # check if list2 appears in list1

    # case: list1 == list2
    if (list1 == list2):
        return True 
    # case: len(list2) > len(list1)
    if (len(list2) > len(list1)):
        return False 
    # case: len(list2) < len(list1)
    else:
        for i in range(len(list1)-len(list2)):
            temp = []
            for x in range(i, len(2)):
                temp[x-i] = list1[x]
            if temp == list2:
                return True 
    return False
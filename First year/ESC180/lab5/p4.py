def list1_start_with_list2(list1, list2):
    if len(list1) >= len(list2):
        for i in range(len(list2)):
            if list1[i] != list2[i]:
                return False
    else:
        return False
    return True

                
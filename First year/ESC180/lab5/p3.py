def lists_are_the_same(l1,l2):
    if len(l1) == len(l2):
        for i in range(len(l1)):
            if l1[i] != l2[i]:
                return False
    else:
        return False
    return True
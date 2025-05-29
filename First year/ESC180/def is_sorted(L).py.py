def is_sorted(L):
    v1 = sorted(L)
    v2 = sorted(L)
    v2.reverse()
    if L == v1 or L == v2:
        return True
    else:
        return False

def euc_distance(u,v):
    # convert to list
    # get value of max key
    ukeys = sorted(list(u.keys()))
    vkeys = sorted(list(v.keys()))
    maxElem = max(ukeys[-1], vkeys[-1])

    uVec = [0]*(maxElem + 1)
    vVec = [0]*(maxElem + 1)
    
    # populate vectors
    for key, value in u.items():
        uVec[key] = value
    for key, value in v.items():
        vVec[key] = value
    
    # compute dot product
    sum = 0
    for i in range(maxElem+1):
        sum += (uVec[i]-vVec[i])**2

    return float(sum**0.5)

def merge(L1,L2):
    oneIndex, twoIndex = 0,0
    res = []
    while (oneIndex < len(L1) and twoIndex < len(L2)):
        if L1[oneIndex] < L2[twoIndex]:
            res.append(L1[oneIndex])
            oneIndex += 1
        else:
            res.append(L2[twoIndex])
            twoIndex += 1
    # handle remaining elements
    res.extend(L1[oneIndex:])
    res.extend(L2[twoIndex:])
    
    return res
        
    
#print(is_sorted([5,3,1]))
#print(euc_distance({1:4,3:4,5:9}, {11:23, 113:43}))
print(merge([4,8,10],[2,5]))
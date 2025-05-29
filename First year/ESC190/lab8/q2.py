# calculate target sum
denominations = [3,5]
target = 17
def partB(denominations, target):
    optlist = [0]*(target + 1)
    # generate optlist for 0 --> target
    for i in range(1, target+1):
        optlist[i] = 10000000000000 # large dummy value
        for denomination in denominations:
            if i - denomination >= 0: # you can make a coin combination
                optlist[i] = min(optlist[i], optlist[i-denomination]+1)
    return optlist

def partC(denominations, target):
    # get optlist
    optlist = partB(denominations, target)
    optlist.append(10000000000)
    # work backwards to get coins
    coinValues = []
    startingValue = target
    while startingValue > 0:
        minTracker = -1
        for coin in denominations:
            if startingValue - coin >= 0:
                if optlist[startingValue-coin] < optlist[startingValue]:
                    # update minTracker
                    minTracker = coin
        startingValue -= minTracker
        coinValues.append(minTracker)

    return coinValues


# if optlist[target] = inf, coin combination is not possible

def q3(s, wordDict):
    # base case

    # recursive case
    # is word a prefix of s?
    for word in wordDict:
        if word == s[:len(word)] and q3(s[len(word):], wordDict) == True:
            return True
        elif word == s:
            return True

    return False



s2 = "catsandog"
wordDict2 = ["cats", "dog", "sand", "and", "cat"]
# print(partB(denominations, target))


s = ""
wordDict = ["a", "b", "c"]
# Expected Output: True


# print(q3(s,wordDict))
print(partB(denominations,target))
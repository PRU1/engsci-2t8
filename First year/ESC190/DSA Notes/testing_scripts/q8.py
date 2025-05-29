def canBeSegmented(s, wordDict):
    for word in wordDict:
        # if the suffix is a word and the second part of s can be segmented
        if word == s[:len(word)] and canBeSegmented(s[len(word):], wordDict):
            return True
        elif word == s:
            return True

    return False

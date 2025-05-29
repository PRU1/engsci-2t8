# to get to some step i, the cost will be
# - cost [i-1] + cost[i]
# - cost [i-2] + cost[i]
# - cost [i-3] + cost[i]

def dice_combinations(n):
    combos = [1,2,3,4,5,6]
    memo = [float('inf')] * (n+1) 
    memo[0] = 0
    memo[1] = 1
    memo[2] = 1 

    for x in range(3, n+1):
        for roll in combos: 
            if x - roll >= 0:
                memo[x] = min(memo[x-roll]+1, memo[x])

    return memo
def back_tracking(memo, target_value): 
    # approach: if memo[target_value - roll] = memo_list[target_value] - 1 yay! append to list. 

    res = []
    combos = [1,2,3,4,5,6]
    if target_value in combos:
        return target_value
    for roll in combos:
        if memo[target_value-roll] == memo[target_value] - 1:
            return back_tracking(memo, target_value-roll)
    
    return res

val = 13 
print(dice_combinations(val))
print(back_tracking(dice_combinations(val), val))

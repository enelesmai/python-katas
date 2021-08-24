#counts pair of distinct number which the sum is equal to k
def countPairsWithSum(k, a):
    pairs = set()
    for idx, val in enumerate(a):
        for val2 in a[idx+1:]:
            if val + val2 == k:
                pair = [val,val2]
                pair.sort()
                pairs.add(tuple(pair))

    return len(pairs)
    
print(countPairsWithSum(11, [10,4,3,2,5,1,6]))

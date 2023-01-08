
def bsearch(a,n):       #form sorted a find the lower and upper bound
    # [l,mid] [mid+1,r] mid = (l+r) >> 1
    # mid1 = l+r >> 1
    # if (mid1 satisfy):  l = mid1+1      #satify the condition
    # else:       r = mid1


    # #[l,mid-1] [mid,r]  mid = (l+r+1) >> 1
    # mid2 = l+r+1 >> 1
    # if (mid2 satisfy):  l = mid2
    # else:       r = mid2-1


    
        # lower bound
    while l<r:
        mid = l+r >> 1
        if a[mid] >= n: r = mid
        else:           l = mid+1
    if a[mid] == n: lowerbound = mid
    else:           return -1,-1
        # upper bound
    while l<r:
        mid = l+r+1 >> 1
        if a[mid] <= n: l = mid
        else:           r = mid-1
    upperbound = mid
    
    return lowerbound,upperbound

print("hello, world!")
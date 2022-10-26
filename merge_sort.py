

def merge_sort(a):
    def sort(a,aux,lo,hi):
        if hi <= lo: return
        mid = (lo+hi)//2
        sort(a,aux,lo,mid)
        sort(a,aux,mid+1,hi)
        merge(a,aux,lo,mid,hi)

    def merge(a,aux,lo,mid,hi):
        for k in range(lo,hi+1):
            aux[k] = a[k]
        i = lo
        j = mid+1
        for k in range(lo,hi+1):
            if i > mid:
                a[k] = aux[j]
                j += 1
            elif j > hi:
                a[k] = aux[i]
                i += 1
            elif aux[i] < aux[j]:
                a[k] = aux[i]
                i += 1
            else:
                a[k] = aux[j]
                j += 1
    
    aux = [0]*len(a)
    sort(a,aux,0,len(a)-1)


def merge_sort_bottomup(a):
    def merge(a,aux,lo,mid,hi):
        for k in range(lo,hi+1):
            aux[k] = a[k]
        i = lo
        j = mid+1
        for k in range(lo,hi+1):
            if i > mid:
                a[k] = aux[j]
                j += 1
            elif j > hi:
                a[k] = aux[i]
                i += 1
            elif aux[i] < aux[j]:
                a[k] = aux[i]
                i += 1
            else:
                a[k] = aux[j]
                j += 1
    
    def sort(a):
        n = len(a)
        aux = [0]*n
        sz = 1
        while sz < n:
            lo = 0
            while lo < n-sz:
                hi = min(lo+sz+sz-1,n-1)
                mid = lo+sz-1
                merge(a,aux,lo,mid,hi)
                lo += sz+sz
            sz += sz
    sort(a)



a = [2,3,45,1,23,4523,13,55,66,55,33]  #[1, 2, 3, 13, 23, 33, 45, 55, 55, 66, 4523]
# merge_sort(a)
merge_sort_bottomup(a)
print(a)
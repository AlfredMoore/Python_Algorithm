


def quick_sort(a):

    def swap(a,i,j):
        temp = a[i]
        a[i] = a[j]
        a[j] = temp

    def partition(a,lo,hi):
        i = lo
        j = hi
        while i <= j:
            while a[i] <= a[lo]:
                if i == hi: break
                i += 1
            while a[j] >= a[lo]:
                if j == lo: break
                j -= 1
            if i >= j:      break
            swap(a,i,j)
        swap(a,lo,j)
        return j

    def sort(a,lo,hi):
        if hi <= lo:        return
        j = partition(a,lo,hi)
        sort(a,lo,j-1)
        sort(a,j+1,hi)        

    sort(a,0,len(a)-1)


a = [1,2,333,333,333,444,555,666]
quick_sort(a)
print(a)





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
            if i >= j: break
            swap(a,i,j)
        swap(a,lo,j)
        return j

    def sort(a,lo,hi):
        if hi <= lo: return
        median = (lo+hi)//2
        swap(a,lo,median)
        j = partition(a,lo,hi)
        # print(lo,median,hi,"    ",j)
        # print(a)
        sort(a,lo,j-1)
        sort(a,j+1,hi)  



    sort(a,0,len(a)-1)


a = [2,3,45,1,23,4523,13,55,66,55,33]  #[1, 2, 3, 13, 23, 33, 45, 55, 55, 66, 4523]
quick_sort(a)
print(a)


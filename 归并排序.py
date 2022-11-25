def merge(s1,s2,s):
    i = j = 0
    while i+j<len(s):
        if j == len(s2) or (i < len(s1) and s1[i] < s2[j]):
            s[i+j] = s1[i]
            i+=1
        else:
            s[i+j] = s2[j]
            j+=1


def mergeSort(s):
    n = len(s)
    if n < 2:
        return
    mid = n // 2
    s1 = s[:mid]
    s2 = s[mid:]
    mergeSort(s1)
    mergeSort(s2)
    merge(s1,s2,s)

s = [1,7,3,5,4]
mergeSort(s)
print(s)
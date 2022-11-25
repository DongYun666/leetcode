def merge(intervals):
    res = 0
    temp = [0 for _ in range(max(intervals,key=lambda x:x[1])[1]+1)]
    for start,end in intervals:
        temp[start]+=1
        temp[end]-=1
    for i in range(1,len(temp)):
        temp[i]+=temp[i-1]
        if temp[i]!=0:
            res+=1
    return res

if __name__ == '__main__':
    arr = []
    while 1:
      s = input()
      if s != "":
          arr.append(list(map(int, s.split())))
      else:
        break
    var = 0
    var = merge(arr)
    print(var)
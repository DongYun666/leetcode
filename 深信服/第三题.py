from collections import defaultdict

n = int(input())
s = input()
start,end =0,0
f_s,f_end = 0,0
max_length = 0
res = defaultdict(list)
for i in range(1,len(s)):
    if s[i] == '1' and s[i-1]!='1':
        start,end = i,i
        continue
    if s[i]!='1':
        length = end-start+1
        if length>=max_length:
            max_length = length
            f_s = start
            f_end = end
            res[f_s] = [f_end,length]
    else:
        end+=1
temp = []
for r in res.items():
    if r[1][1] == max_length:
        temp.append([r[0],r[1][0]])
ans = 0
for st,en in temp:
    ans+= st+len(s)-en+st*(len(s)-en-1)
print(ans)
# print(f_s+len(s)-f_end+f_s*(len(s)-f_end-1))



#数据字典
data = "@#￥%&"
dict = {
    "o" : "0",
    "y" : "1",
    "e" : "2",
    "a" : "3",
    "s" : "4",
    "0" : "o",
    "1" : "y",
    "2" : "e",
    "3" : "a",
    "4" : "s",
    "." : "."
}

#10进制转换5进制
def f_5(n):
    int_b,float_b = "",""
    int_n = eval(str(n).partition(".")[0])
    float_n = 0
    if str(n).partition(".")[2] != "":
        float_n = eval("0."+str(n).partition(".")[2])
    while True:
        s=int_n//5  # 商
        y=int_n%5  # 余数
        int_b += str(y)
        if s==0:
            break
        int_n=s
    if str(n).partition(".")[2] != "":
        for i in range(5):
            s = float_n*5
            if(s!=0):
                float_b+=str(s).partition(".")[0]
            else:
                break
            float_n = eval("0."+str(s).partition(".")[2])
    temp =  list(int_b[::-1])
    res = []
    for t in temp:
        res.append(dict.get(t))
    return "".join(res)


#5进制转换10进制
def f_10(x):
    s_x= ""
    n = 0
    for i in range(len(x)):
        s_x += dict[x[i]]
    if s_x.partition(".")[2] != "":
        numx = int(s_x.partition(".")[0],5)
        s = s_x.partition(".")[2]
        for i in range(len(s)):
            n += eval(s[i])*(5**(-(i+1)))
    else:
        numx = eval(str(int(s_x.partition(".")[0],5)))
    return numx+n

T = int(input())
res = []
for _ in range(T):
    num = input()
    if num.isdigit():
        res.append(f_5(num))
    else:
        res.append(f_10(num))
for r in res:
    print(r)
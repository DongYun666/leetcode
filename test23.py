import sys

# 输入 abc 求所有的出栈顺序

#检查出栈顺序是否合法
def check(path):
    stack = []
    if len(path) != len(str_):
        return False
    left = 0
    for i in range(len(str_)):
        if str_[i] != path[left]:
            stack.append(str_[i])
        else:
            left += 1
            while stack and stack[-1] == path[left]:
                stack.pop()
                left += 1
    if stack:
        return False
    return True


def all_pop(stack,path,res):
    if not stack:
        # 检查元素出栈顺序是否合法
        if check(path):
            res.append(path)
        return
    for i in range(len(stack)):
        next_stack = stack[:i] + stack[i+1:]
        next_path = path + stack[i]
        all_pop(next_stack,next_path,res)
        
def all_pop_order(stack):
    res = []
    all_pop(stack,"",res)
    return res



if __name__ == '__main__':
    for line in sys.stdin:
        str_ = line.strip()
        resoult = all_pop_order(str_)
        for res in resoult:
            print(res)
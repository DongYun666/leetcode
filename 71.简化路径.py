class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        temp = []
        for w in path:
            if w == "..":
                if len(temp) == 0:
                    continue
                else:
                    temp.pop()
            elif w == "." or w == "":
                continue
            else:
                temp.append(w)
        return "/"+"/".join(temp)



path = "/home//foo/"
print(Solution().simplifyPath(path))
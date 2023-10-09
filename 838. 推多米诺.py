class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        res = ""
        index = 0
        while index < len(dominoes):
            if dominoes[index] == "L" or dominoes[index] == "R":
                res += dominoes[index]
                index += 1
            else: # 如果是"."
                left = index
                while index < len(dominoes) and dominoes[index] == ".":
                    index += 1
                right = index
                if index == len(dominoes):
                    if left != 0 and dominoes[left-1] == "R":
                        res += "R"*(right-left)
                    else:
                        res += "."*(right-left)
                    break
                # 两边向中间坍塌
                if dominoes[index] == "L" and left !=0 and dominoes[left-1] == "R":
                    if (right-left)%2 == 0:
                        res += "R"*((right-left)//2) + "L"*((right-left)//2)
                    else:
                        res += "R"*((right-left)//2) + "."+"L"*((right-left)//2)

                elif dominoes[index] == "L" and left == 0:
                        res += "L"*(right-left)
                elif dominoes[index] == "R" and left != 0 and dominoes[left-1] == "R":
                        res += "R"*(right-left)
                elif dominoes[index] == "R" and left == 0:
                        res += "."*(right-left)
            
        return res
dominoes = ".L.R...LR..L.."
print(Solution().pushDominoes(dominoes))
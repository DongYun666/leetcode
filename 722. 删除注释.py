from typing import List
class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        in_block = False
        new_line = []
        for line in source:
            if not in_block:
                if "/*" in line:
                    if "*/" in line:
                        line = line[:line.index("/*")] + line[line.index("*/")+2:]
                        if line:
                            res.append(line)
                    else:
                        in_block = True
                        new_line.append(line[:line.index("/*")])
                elif "//" in line:
                    line = line[:line.index("//")]
                    if line:
                        res.append(line)
                else:
                    if line:
                        res.append(line)
            else:
                if "*/" in line:
                    in_block = False
                    new_line.append(line[line.index("*/")+2:])
                    temp = "".join(new_line)
                    if temp:
                        res.append(temp)
        return res
    

source = ["/*Test program */", 
            "int main()",
            "{ ",
            "  // variable declaration ",
            "int a, b, c;", 
            "/* This is a test", 
            "   multiline  ", 
            "   comment for ", 
            "   testing */", 
            "a = b + c;", 
            "}"]
# source = ["a/*comment", "line", "more_comment*/b"]
print(Solution().removeComments(source))
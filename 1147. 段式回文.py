class Solution:
    def longestDecomposition(self, text: str) -> int:
        res = 0
        left,right = "",""
        i,j = 0,len(text) - 1
        while i <= j:
            left += text[i]
            right = text[j] + right
            if i == j:
                break
            if left == right:
                left,right = "",""
                res += 2
            i += 1
            j -= 1
        if left != "" or right != "":
            res += 1
        return res

text = "ghiabcdefhelloadamhelloabcdefghi"
text = "merchant"  
text = "antaprezatepzapreanta"
text = "aaa"
print(Solution().longestDecomposition(text))
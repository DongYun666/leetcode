from typing import List
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = []
        
        for i in range(1,len(searchWord)+1):
            res.append([x for x in products if x.startswith(searchWord[:i])][:3])
        return res


products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"
print(Solution().suggestedProducts(products, searchWord))
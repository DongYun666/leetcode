
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        quotient = purchaseAmount // 10  # 使用整除运算符
        remainder = purchaseAmount % 10
        return 100 - 10 * (quotient if remainder < 5 else quotient + 1)
    
purchaseAmount = 9
purchaseAmount = 10
print(Solution().accountBalanceAfterPurchase(purchaseAmount))
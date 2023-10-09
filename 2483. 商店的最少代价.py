class Solution:
    def bestClosingTime(self, customers: str) -> int:
        mincnt = cnt = customers.count("Y")
        res = 0
        for i,ch in enumerate(customers):
            if ch == "N":
                cnt += 1
            else:
                cnt -= 1
                if cnt < mincnt:
                    mincnt = cnt
                    res = i
        return res
    
customers = "YYNY"
# customers = "NNNNN"
customers = "YYYY"
print(Solution().bestClosingTime(customers))


# LSTM + Attention
# https://www.kaggle.com/qqgeogor/keras-lstm-attention-glove840b-lb-0-043

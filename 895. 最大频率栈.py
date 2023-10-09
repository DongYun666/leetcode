from collections import defaultdict


class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)
        self.d_fre = defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.freq[val]+=1
        self.d_fre[self.freq[val]].append(val)
        self.max_freq = max(self.max_freq, self.freq[val])

    def pop(self) -> int:
        val = self.d_fre[self.max_freq].pop()
        self.freq[val] -= 1
        if len(self.d_fre[self.max_freq]) == 0:
            self.max_freq -= 1
        return val

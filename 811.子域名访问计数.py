from typing import List
from collections import Counter, defaultdict


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        # cnt = Counter(cpdomains)
        # print(cnt)
        cnt = defaultdict(int)
        for cpdomain in cpdomains:
            c, ip = cpdomain.split()
            c = int(c)
            ip = ip.split('.')
            for i in range(len(ip)):
                cnt[".".join(ip[i:])]+=c
        res = []
        for ip,count in cnt.items():
            res.append(str(count)+" "+ip)
        return res








cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
print(Solution().subdomainVisits(cpdomains=cpdomains))
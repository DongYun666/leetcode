from typing import List
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        query = [0]
        edges.sort()
        reversed = [0]

        while len(query)!=0:
            temp = query.pop(0)
            for edge in edges:
                start,end = edge
                if start not in restricted and end not in restricted:
                    if start == temp and end not in reversed:
                        query.append(end)
                        reversed.append(end)
                    if end == temp and start not in reversed:
                        query.append(start)
                        reversed.append(start)

        print(reversed)
        return len(reversed)





# n = 7
# edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]]
# restricted = [4,5]

# n = 7
# edges = [[0,1],[0,2],[0,5],[0,4],[3,2],[6,5]]
# restricted = [4,2,1]

n = 10
edges = [[4,1],[1,3],[1,5],[0,5],[3,6],[8,4],[5,7],[6,9],[3,2]]
restricted = [2,7]
print(Solution().reachableNodes(n,edges,restricted))
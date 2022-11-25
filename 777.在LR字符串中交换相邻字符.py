class Solution:
    # def canTransform(self, start: str, end: str) -> bool:
    #     if len(start) != len(end):
    #         return False
    #     i,j,n = 0,0,len(start)
    #     start,end = list(start),list(end)
    #     while i<n-1:
    #         if start[i] == end[j]:
    #             i+=1
    #             j+=1
    #             continue
    #         if start[i] == 'L' and end[j] == 'R' or start[i] == 'R' and end[j] == "L":
    #             return False
    #         start_temp = start[i:i+2]
    #         end_temp = end[j:j+2]
    #         if (start_temp == ['X','L'] or start_temp == ['R','X']) and start_temp[0] == end_temp[1] and start_temp[1] == end_temp[0]:
    #             start[i:i+2] = end_temp
    #             if end_temp == ['X','R']:
    #                 i+=2
    #                 j+=2
    #             elif end_temp == ['L','X']:
    #                 i+=1
    #                 j+=1
    #         else:
    #             return False
    #     return True if i == n-1 and start[n-1] == end[n-1] else False

    def canTransform(self, start: str, end: str) -> bool:
        if len(start) != len(end):
            return False
        start_index,end_index = [],[]
        for i in range(len(start)):
            if start[i] != "X":
                start_index.append(i)
            if end[i] != "X":
                end_index.append(i)
        start = start.replace("X",'')
        end = end.replace("X",'')
        if start != end:
            return False
        for j in range(len(start_index)):
            if (start[j] == "L" and start_index[j] < end_index[j]) or (start[j] == "R" and start_index[j] > end_index[j]):
                return False
        return True






# start = "LXXLXRLXXL"
# end = "XLLXRXLXLX"

start = "RXXLRXRXL"
end = "XRLXXRRLX"

# start = "XXXXXLXXXLXXXX"
# end = "XXLXXXXXXXXLXX"
print(Solution().canTransform(start, end))
class Solution:
    def findCenter(self, e: List[List[int]]) -> int:
        
        return e[0][0] if e[0][0]==e[1][0] or e[0][0]==e[1][1] else e[0][1]
        # seen=set()
        # dic={}
        # seen.add(edges[0][0])
        # seen.add(edges[0][1])
        # for i in range(len(edges)):
        #     dic[edges[i][0]]=edges
        #     if edges[i][0] in seen:
        #         return edges[i][0]
        #     elif edges[i][1] in seen:
        #         return edges[i][1]

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
      
        
        for i in range(len(edges)):
            for j in range(len(edges[i])):
                if edges[i][j]==source and edges[i][j-1]==destination:
                    return True
        return False

    
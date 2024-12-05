class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
      
        if n==0:
            return True
        if n==1:
            return True
        for i in range(len(edges)):
            print(f"{i}: ", end="")
            for j in edges[i]:
                print(j, end=" ")
            print()
                # if edges[i][j]==source and edges[i][j-1]==destination:
                #     return True
        return False

    
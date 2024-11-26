class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        directions=[(1,0), (-1,0), (0,1), (0,-1)]
        count=0
        
        # [[0]], len(grid) = 1, grid[0] = [0], grid[0][0] = 0
        # [[1]], len(grid) = 1, grid[0] = [1], grid[0][0] = 1
        
        if rows==1 and cols==1:
            if grid[0][0]==1:
                return 4
            elif grid[0][0]==0:
                return 0
        
        for i in range(rows):
            
            for j in range(cols):
                if grid[i][j]==1:
                    count+=4
                    for dx, dy in directions:
                        ni, nj=i+dx, j+dy
                        if 0<=ni and ni<rows and 0<=nj and nj<cols:
                            # print('curr', i, j, grid[i][j], 'new', ni, nj, grid[ni][nj])
                        # check if valid
                        # 0  ni  rows
                        # 0  nj  cols
                        # 0, 1, ..., rows - 1
                            if grid[ni][nj]==1:
                                count-=1
                    # print('count', count)
        return count
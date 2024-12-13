class Solution:
    def imageSmoother(self, image: List[List[int]]) -> List[List[int]]:
        rows=len(image) # 3
        cols=len(image[0]) # 
        

        smooth= [[0]*cols for _ in range(rows)]
        # visited[0][9]=True
        # print(visited)
        directions=[(-1,-1), (-1, 0), (-1, 1), (0,-1),(0, 0),(0, 1), (1, -1), (1,0),(1,1) ]
        # for x in array:
            # x = [a, b, c]
            
        # [0] * 1 = [0], ['a'] * 5 = [a, a, a, a, ]
        
        # 
        
        for row in range(rows):
            for col in range(cols):
                count=0
                average=0
                for nx, ny in directions:
                    # nx = -1
                    # ny = -1
                    curr_x = row + nx
                    curr_y = col + ny
                    if 0 <= curr_x < rows and 0 <= curr_y < cols:
                        average+=image[curr_x][curr_y]
                        count+=1
                print('row', row, 'col', col, 'average', average, 'count', count)
                smooth[row][col]=(average//count)
                
                
                # visited[row][col]=True
        return smooth
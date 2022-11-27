class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        
        # first we can use different simbol to mark obstacles .
        # im gonna use x for that
        
        ## same as the unique path problem, now iterate reverse over the grid.
        height = len(obstacleGrid)
        width = len(obstacleGrid[0])
        
        
        
        for r in reversed(range(height)):
            for c in reversed(range(width)):
                if obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = 0
                else:
                    if r == height-1:
                        # this point we need to find if there is a obstacle in bottom line
                        # if we already met a obstacle ,the the value should be 0
                        obstacleGrid[r][c] = 1
                        for i in reversed(range(c,width)):
                            if obstacleGrid[r][i]==0:
                                obstacleGrid[r][c] = 0
                        
                    elif c == width -1 :
                        # this point we need to find if there is a obstacle in left column
                        # if we already met a obstacle ,the the value should be 0 
                        obstacleGrid[r][c] = 1
                        for j in reversed(range(r,height)):
                            if obstacleGrid[j][c]==0:
                                obstacleGrid[r][c] = 0
                        
                    else:
                        obstacleGrid[r][c] = obstacleGrid[r+1][c] + obstacleGrid[r][c+1]
        
        
        
        
        return obstacleGrid[0][0]
        
        
        

obj = Solution()
obstacleGrid = [[0,0,0,0,0],[0,0,0,1,1],[0,1,0,0,0]]
print(obj.uniquePathsWithObstacles(obstacleGrid))
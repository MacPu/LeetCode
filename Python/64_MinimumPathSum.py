__author__ = 'MacPu'

# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.

#思路：动态规划，先求出第一行和第一列各点到[0][0]点的最短路径，（就是那一行那一列相加），
# 然后再求出各个点到[0][0]的最短路径，就是和他上面和左面的较小的值相加。最后就可以求出来最小值

class Solution:
    # @param {integer[][]} grid
    # @return {integer}
    def minPathSum(self, grid):
        row = len(grid)
        col = len(grid[0])
        for i in range(1,row):
            grid[i][0] += grid[i-1][0]
        for i in range(1,col):
            grid[0][i] += grid[0][i-1]

        for i in range(1,row):
            for j in range(1,col):
                grid[i][j] += min(grid[i-1][j],grid[i][j-1])

        return grid[row-1][col-1]

if __name__ == '__main__':
    print "min path sum is %d" % Solution().minPathSum([[2, 7, 11, 15], [1,4,3,5],[3,4,5,1]])

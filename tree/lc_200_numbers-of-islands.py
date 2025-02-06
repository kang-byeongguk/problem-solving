'''
개선사항
1. is_indexs 를 is_bounds로 바꾼다.
m,n과 dx,dy를 통일시킨다.
m+dm, n + dn 식으로
dm 어색하니까 r+dr식으로바꾸자.
dfs for문을 
for dx,dy in [(상),(하),(좌),(우)]
nx,ny=x+dx,y+dy로 바꾸자
'''
# 시간복잡도 O (m*n)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
  

        dx=[0,0,-1,1]
        dy=[1,-1,0,0]

        a=1
        def is_index(m,n):
            if 0<=m<len(grid) and 0<=n<len(grid[0]):
                return True
            return False

        def dfs(m,n):
            if not is_index(m,n):
                return
            if grid[m][n]=='0':
                return 
            
            
            grid[m][n]='0'
            for i in range(4):
                dfs(m+dx[i],n+dy[i])
            
            

        count_islands=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    dfs(i,j)
                    count_islands+=1
        return count_islands

        
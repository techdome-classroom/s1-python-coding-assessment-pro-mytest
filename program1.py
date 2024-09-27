class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        # Helper function to perform DFS on the grid
        def dfs(grid, i, j):
            # Check for the boundaries of the grid and if the cell is water or visited land
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 'W':
                return
            # Mark the current cell as visited by converting 'L' to 'W'
            grid[i][j] = 'W'
            # Explore all 4 directions (up, down, left, right)
            dfs(grid, i - 1, j)  # up
            dfs(grid, i + 1, j)  # down
            dfs(grid, i, j - 1)  # left
            dfs(grid, i, j + 1)  # right

        if not grid:
            return 0
        
        # Initialize the count of islands
        islands = 0

        # Loop through every cell in the grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # If we find a landmass 'L', we start a DFS to explore the whole island
                if grid[i][j] == 'L':
                    islands += 1  # Found a new island
                    dfs(grid, i, j)  # Mark the entire island as visited
                    
        return islands

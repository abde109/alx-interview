def island_perimeter(grid):
    perimeter = 0
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                # Start with 4 sides for each land cell
                perimeter += 4
                
                # Check the left neighbor
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2
                
                # Check the top neighbor
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2
    
    return perimeter

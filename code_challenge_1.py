def find_longest_path(matrix):
    if not matrix:
        return 0
    
    rows, cols = len(matrix), len(matrix[0])    
    directions = [(0,1), (1,0), (0,-1), (-1,0)] # all 4 possible directions

    memo = [[-1] * cols for _ in range(rows)]   #max_len matrix
    next_cell = [[None] * cols for _ in range(rows)]  #best_neighbor matrix
    

    def dfs(row,col):      
        if memo[row][col] != -1:
            return memo[row][col]   #return already computed value
        else:
            next_best = None
            max_length = 1
            
            for dr,dc in directions: # explore all 4 directions
                new_row, new_col = row + dr, col + dc   #move to new cell
                
                if 0 <= new_row < rows and 0 <= new_col < cols and matrix[new_row][new_col] > matrix[row][col] : #check bounds and increasing condition
                    cand = 1 + dfs(new_row,new_col) #recursive call to dfs
                    
                    if cand > max_length:  #we need to find the max length path
                        max_length = cand
                        next_best = (new_row, new_col)

            next_cell[row][col] = next_best 
            memo[row][col] = max_length            #after evaluating all possible directories,store max length, best next cell  
            return memo[row][col]
    max_path = 0
    start_cell = None   
    for r in range(rows):
        for c in range(cols):
            length = dfs(r,c)
            if length > max_path:
                max_path = length
                start_cell = (r,c)
            

    path = []
    r, c = start_cell #start from best starting cell
    while r is not None and c is not None:
        path.append((r, c))
        next_pos = next_cell[r][c]
        if next_pos is not None:
            r,c = next_pos
        else:
            break 
            

    max_path_sequence = path                     
    
    
    return max_path, max_path_sequence


matrix = [[21,22,23,24,25],
          [20,7,8,9,10],
          [19,6,1,2,11],
          [18,5,4,3,12],
          [17,16,15,14,13]]

print(find_longest_path(matrix))
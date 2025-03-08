def count_rooms(grid):
    if not grid:
        return 0
    
    height = len(grid)
    width = len(grid[0])

    visited = [[False for _ in range(width)] for _ in range(height)]

    room_count = 0

    for i in range(height):
        for j in range(width):
            if grid[i][j] == '.' and not visited[i][j]:
                room_count += 1
                
                queue = [(i, j)]
                visited[i][j] = True
                
                while queue:
                    r, c = queue.pop(0)
                    
                    neighbors = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
                    
                    for nr, nc in neighbors:
                        if 0 <= nr < height and 0 <= nc < width:
                            if grid[nr][nc] == '.' and not visited[nr][nc]:
                                queue.append((nr, nc))
                                visited[nr][nc] = True
                                
    return room_count

if __name__ == "__main__":
    grid = ["########",
            "#.#..#.#",
            "#####..#",
            "#...#..#",
            "########"]
    print(count_rooms(grid)) # 4

    grid = ["########",
            "#......#",
            "#.####.#",
            "#......#",
            "########"]
    print(count_rooms(grid)) # 1

    grid = ["########",
            "######.#",
            "##.#####",
            "########",
            "########"]
    print(count_rooms(grid)) # 2
# Päädyin y, x -koordinaatistoon, koska ruudukko on annettu riveittäin.

def analyze_route(grid):
    grid = [list(row) for row in grid]
    
    # Etsitään robotin alkuruutu
    robot_y, robot_x = None, None
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 'R':
                robot_y, robot_x = y, x
                # Merkataan alkuruutu lattiaksi, koska robotti lähtee liikkeelle siitä
                grid[y][x] = '.'
                break
        if robot_y is not None:
            break
    
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    current_dir = 0
    
    visited = set()
    visited.add((robot_y, robot_x))
    
    state_history = set()
    
    height = len(grid)
    width = len(grid[0])
    
    while True:
        next_y = robot_y + directions[current_dir][0]
        next_x = robot_x + directions[current_dir][1]
        
        # Tarkistetaan, olemmeko ruudukon ulkopuolella
        if next_y < 0 or next_y >= height or next_x < 0 or next_x >= width:
            return (len(visited), True)
        
        # Tarkistetaan, onko edessä este
        if grid[next_y][next_x] == '#':
            # Käännytään oikealle
            current_dir = (current_dir + 1) % 4 # % 4 varmistaa, että suunta pysyy välillä 0-3
        else:
            # Liikutaan eteenpäin
            robot_y, robot_x = next_y, next_x
            visited.add((robot_y, robot_x))
        
        # Tarkistetaan nykyinen tila (koordinaatit + suunta)
        current_state = (robot_y, robot_x, current_dir)
        if current_state in state_history:
            return (len(visited), False)
        
        state_history.add(current_state)

if __name__ == "__main__":
    grid1 = [".#......",
             "..#.....",
             ".......#",
             "#.R.....",
             "......#."]
    print(analyze_route(grid1)) # (14, True)

    grid2 = ["........",
             ".##.....",
             ".......#",
             "#.R.....",
             "......#."]
    print(analyze_route(grid2)) # (12, False)
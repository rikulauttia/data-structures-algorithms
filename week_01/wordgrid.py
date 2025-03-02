class WordFinder:
    def set_grid(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if grid else 0
        self.directions = [
            (0, 1), (1, 0), (1, 1), (-1, 1),
            (0, -1), (-1, 0), (-1, -1), (1, -1)
        ]

    def count(self, word):
        found = set()
        word_len = len(word)
        
        def is_valid(r, c):
            return 0 <= r < self.rows and 0 <= c < self.cols
        
        def search(r, c, dr, dc):
            positions = []
            for i in range(word_len):
                nr, nc = r + i * dr, c + i * dc
                if not is_valid(nr, nc) or self.grid[nr][nc] != word[i]:
                    return False
                positions.append((nr, nc))
            found.add(frozenset(positions))
            return True
        
        for r in range(self.rows):
            for c in range(self.cols):
                for dr, dc in self.directions:
                    search(r, c, dr, dc)
        
        return len(found)

if __name__ == "__main__":
    grid = ["TIRATIRA",
            "IRATIRAT",
            "RATIRATI",
            "ATIRATIR"]

    finder = WordFinder()
    finder.set_grid(grid)

    print(finder.count("TIRA")) # 7 
    print(finder.count("TA")) # 13
    print(finder.count("RITARI")) # 3
    print(finder.count("A")) # 8
    print(finder.count("AA")) # 6
    print(finder.count("RAITA")) # 0
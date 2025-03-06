class Contest:
    def __init__(self, names, task_count):
        self.names = names
        self.task_count = task_count
        self.scores = {name: [0] * task_count for name in names}
        self.total_scores = {name: 0 for name in names}
        self.timestamps = {name: float('inf') for name in names}
        self.submit_counter = 0

    def add_submission(self, name, task, score):
        self.submit_counter += 1
        
        task_idx = task - 1
        old_score = self.scores[name][task_idx]
        
        if score > old_score:
            self.scores[name][task_idx] = score
    
            old_total = self.total_scores[name]
            new_total = old_total - old_score + score
            self.total_scores[name] = new_total
            
            if new_total != old_total:
                self.timestamps[name] = self.submit_counter

    def create_scoreboard(self):
        result = []
        
        for name in self.names:
            score = self.total_scores[name]
            result.append((name, score))
        
        def sort_key(item):
            name, score = item
            timestamp = self.timestamps[name]
            
            if score == 0:
                return (-score, name)
            else:
                return (-score, timestamp)
        
        result.sort(key=sort_key)
        return result

if __name__ == "__main__":
    names = ["anna", "pekka", "kalle", "tiina", "eeva"]
    contest = Contest(names, 3)

    contest.add_submission("tiina", 2, 30)
    contest.add_submission("pekka", 1, 40)
    contest.add_submission("tiina", 1, 20)
    contest.add_submission("pekka", 1, 50)
    contest.add_submission("pekka", 2, 0)
    contest.add_submission("eeva", 3, 100)
    contest.add_submission("anna", 1, 0)
    contest.add_submission("eeva", 3, 80)
    contest.add_submission("tiina", 2, 30)

    scoreboard = contest.create_scoreboard()
    print(scoreboard)
    # [('eeva', 100), ('tiina', 50), ('pekka', 50), ('anna', 0), ('kalle', 0)]
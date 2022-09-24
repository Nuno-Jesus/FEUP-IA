import copy

class HillClimbing:
    def __init__(self, first, neighbour, evaluation, it):
        self.solution = first
        self.neighbour_function = neighbour
        self.evaluation_function = evaluation
        self.iterations = it

    def run(self):
        ev = []
        solution = self.solution
        best_sol = []
        best_sol_eval = 0

        it = 0
        while it < self.iterations:
            it += 1

            neighbour = self.neighbour_function(copy.deepcopy(solution))
            evaluation = self.evaluation_function(neighbour)

            if evaluation > self.evaluation_function(solution):
                solution = neighbour
                #it = 0
                if evaluation > best_sol_eval:
                    #all time best
                    best_sol = neighbour
                    best_sol_eval = evaluation

            ev.append(self.evaluation_function(solution))

        return best_sol, ev
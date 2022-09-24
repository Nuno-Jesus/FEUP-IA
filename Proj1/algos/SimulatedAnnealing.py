import math
import copy
import random

class SimulatedAnnealing:
    def __init__(self, first, neighbour, evaluate, it, cooling):
        self.solution = first
        self.neighbour_function = neighbour
        self.evaluation_function = evaluate
        self.iterations = it
        self.cooling_option = cooling
    
    def T_schedule(self, T0, it):
        if(self.cooling_option == 1):
            return T0 * 0.85 ** it
        elif(self.cooling_option == 2):
            return T0 / (1 + 5 * math.log(1 + it))
        elif(self.cooling_option == 3):
            return T0 / (1 + 1.5 * it) 
        else:
            return T0 / (1 + 0.5 * it ** 2) 

    def run(self):
        ev = []

        best_sol = []
        best_sol_eval = 0

        solution = self.solution
        it = 0
        T0 = 1000

        while it < self.iterations:
            T = self.T_schedule(T0, it)
            neighbour = self.neighbour_function(copy.deepcopy(solution))
            evaluation = self.evaluation_function(neighbour)
            delta = float(evaluation - self.evaluation_function(solution))

            it += 1
            
            if delta > 0 or random.random() < math.exp(delta / T):
                solution = neighbour
                if evaluation > best_sol_eval:
                    #all time best
                    best_sol = neighbour
                    best_sol_eval = evaluation

            ev.append(self.evaluation_function(solution))

        return best_sol, ev
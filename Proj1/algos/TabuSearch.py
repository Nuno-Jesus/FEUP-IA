import copy
import random

class TabuSearch:
    def __init__(self, first, neighbour, evaluate, it):
        self.solution = first
        self.neighbour_function = neighbour
        self.evaluation_function = evaluate
        self.iterations = it

    def tabu_tenure(self):
        return random.randint(int(self.iterations / 10), int(self.iterations / 5))

    def neighbourhood_size(self):
        return random.randint(3, 5)

    def tabu_neighbourhood(self, solution, tabus):
        neighbourhood = []
        for i in range(self.neighbourhood_size()):
            neighbour = self.neighbour_function(copy.deepcopy(solution))
            while neighbour in neighbourhood:
                neighbour = self.neighbour_function(copy.deepcopy(solution))
            
            #If the generated neighbour is not in the tabu list, add it
            if str(neighbour) not in tabus and neighbour not in neighbourhood:
                neighbourhood.append(neighbour)

        return neighbourhood
            

    def run(self):
        tabus = {}
        ev = []

        solution = self.solution
        best_sol = self.neighbour_function(copy.deepcopy(solution))
        candidate_solution = best_sol
        ev.append(self.evaluation_function(best_sol))

        it = 0
        while it < self.iterations: 
            # Generates a neighbourhood around the current best solution
            neighbourhood = self.tabu_neighbourhood(best_sol, tabus)
            
            # Searches the neighbourhood for a better solution than the one so far
            for temp_neighbour in neighbourhood:
                evaluation = self.evaluation_function(temp_neighbour)
                #print("Candidate: ", best_sol, evaluation, " Current: ", self.evaluation_function(best_sol))
                if evaluation > self.evaluation_function(candidate_solution):
                    candidate_solution = temp_neighbour

            # Checks if the local optima is greater than the global one
            evaluation = self.evaluation_function(candidate_solution)
            ev.append(evaluation)
            if evaluation > self.evaluation_function(best_sol):
                best_sol = candidate_solution
            
            # Decrements the counters for each tabu
            old_tabus = []
            for sol in tabus:
                tabus[str(sol)] -= 1
                if tabus[str(sol)] == 0:
                    old_tabus.append(str(sol))

            # Removes the null tabus
            for old in old_tabus:
                del tabus[old]

            old_tabus.clear()

            # Adds the new best neighbour of the neighbourhood to the tabu list
            tabus[str(candidate_solution)] = self.tabu_tenure()

            it += 1
            
        return best_sol, ev
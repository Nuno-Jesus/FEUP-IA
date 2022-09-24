from formulation.solution import *
from algos.HillClimbing import HillClimbing
from algos.SimulatedAnnealing import SimulatedAnnealing
from algos.TabuSearch import TabuSearch
from algos.GeneticAlgorithm import GeneticAlgorithm
from utils.utils import *
import copy
import matplotlib.pyplot as plt

def print_menu():
    print("********************************************************************************")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                                 INSTRUCTIONS                                 *")
    print("*                                                                              *")
    print("*  1. Input file's letter without extension( from 'a' to 'c').                 *")
    print("*  2. Choose the cooling algorithm for Simulated Annealing.                    *")
    print("*  3. Choose the size of the population to be used in the genetic algorithm.   *")
    print("*  4. Pick between Tournament and Roulette Selection.                          *")
    print("*  5. Pick the crossover function                                              *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("********************************************************************************")

if __name__ == "__main__":

    print_menu()
    filename = input("File name: ")

    team = read_dataset(filename)
    sol = Solution(team)

    cooling_algorithm = int(input("Select one of the following cooling algorithms: \n1) Exponential multiplicative \n2) Logarithmical multiplicative \n3) Linear multiplicative \n4) Quadratic multiplicative \n"))

    pop_size = int(input("Input the desired population size: "))
    parents_algorithm = int(input("Select one of the following algorithms to select the parents: \n1) tournament selection \n2) roulette_selection\n"))
    crossover_algorithm = int(input("Select one of the following algorithms to select the crossover function: \n1)First half of parent 1 and second half of parent 2 \n2)First half of parent 2 and second half of parent 1 \n3)Randomly choose between 1) and 2)\n"))

    print("Random solution: ", sol.solution)

    it = team.n_members * 30
    HC_algorithm = HillClimbing(copy.deepcopy(sol.solution), sol.neighbour3, sol.evaluate, it)
    SA_algorithm = SimulatedAnnealing(copy.deepcopy(sol.solution), sol.neighbour3, sol.evaluate, it, cooling_algorithm)
    TS_algorithm = TabuSearch(copy.deepcopy(sol.solution), sol.neighbour3, sol.evaluate, it)
    GA_algorithm = GeneticAlgorithm(copy.deepcopy(sol.solution), sol.neighbour3, sol.evaluate, it, sol.team, pop_size, parents_algorithm, crossover_algorithm)
    
    sol1, hill_evals = HC_algorithm.run()
    print("Best value with hill climbing was ", sol1, " with ", max(hill_evals))

    sol2, annealing_evals = SA_algorithm.run()
    print("Best value with simulated annealing was ", sol2, " with ", max(annealing_evals))

    sol3, genetic_evals = GA_algorithm.run()
    print("Best value with genetic algorithm was ", sol3, " with ", max(genetic_evals))

    sol4, tabu_evals = TS_algorithm.run()
    print("Best value with tabu search was ", sol4, " with ", max(tabu_evals))

    plt.plot(hill_evals, 'g', label='Hill Climbing')
    plt.plot(annealing_evals, 'b', label='Simulated Annealing')
    plt.plot(genetic_evals, 'r', label='Genetic Algorithm')
    plt.plot(tabu_evals, 'k', label='Tabu Search')

    plt.title("Dataset " + filename.upper())

    plt.xlabel('iteration')

    plt.ylabel('evaluation')

    plt.legend()

    plt.savefig("output/iterations.png")

    plt.show()

    plt.clf()


    solutions = [sol.evaluate(sol1), sol.evaluate(sol2), sol.evaluate(sol3), sol.evaluate(sol4)]

    labels = ['H.C.', 'S.A.', 'G.A.', 'T.S.']

    plt.bar(labels, solutions)

    plt.title("Dataset " + filename.upper())

    plt.xlabel('algorithms')

    plt.ylabel('best evaluation')

    plt.savefig("output/best_evaluation.png")

    plt.show()



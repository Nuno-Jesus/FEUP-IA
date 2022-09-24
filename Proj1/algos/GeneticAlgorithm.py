import random
import copy
import numpy as np

class GeneticAlgorithm:
    def __init__(self, first, neighbour, evaluate, it, team, pop_size, parents_algo, crossover_algo):
        self.solution = first
        self.neighbour_function = neighbour
        self.evaluation_function = evaluate
        self.iterations = it
        self.team = team
        self.population_size = pop_size
        self.parents_algorithm = parents_algo
        self.crossover_algorithm = crossover_algo

    def run(self):
        ev = []

        population = self.create_initial_population()

        it = 0
        while it < self.iterations:
            it += 1

            population, current_best = self.generate_next_population(population)

            ev.append(current_best - 1000)

        #check the best of the final solution
        fitness = self.evaluate_fitness(population)

        top_fit = max(fitness)  # value of the fittest element
        index = fitness.index(top_fit) # most fit element index
        all_time_best = population[index]   # actual element

        ev.append(top_fit - 1000)

        return all_time_best, ev

    def create_initial_population(self):
        population = []

        for i in range(self.population_size):
            #population.append([random.randint(0,1) for _ in range(self.team.n_projects * self.team.n_members)])
            temp = []
            for _ in range (self.team.n_projects):
                temp.append([random.randint(0,1) for _ in range(self.team.n_members)])
            population.append(temp)

            #population.append([])
            #for j in range(self.team.n_members * self.team.n_projects): # n chromossomes for each project
            #    population[i].append(random.randint(0,1))

        return population

    def evaluate_fitness(self, population):
        fitness = []
        for i in range(len(population)):
            fitness.append(self.evaluation_function(population[i]) + 1000)

        return fitness

    def select_parents(self, fitness, option):

        population_size = len(fitness)

        if(option == 1):
            return self.tournament_selection(fitness, population_size)
        else:
            return self.roulette_selection(fitness, population_size)


    def tournament_selection(self, fitness, population_size):

        #choose elements for tournament
        el1 = random.randrange(population_size)
        el2 = random.randrange(population_size)
        el3 = random.randrange(population_size)
        el4 = random.randrange(population_size)

        if fitness[el1] > fitness[el2]:
            parent1 = el1
        else:
            parent1 = el2

        if fitness[el3] > fitness[el4]:
            parent2 = el3
        else:
            parent2 = el4

        return parent1, parent2 # index of the parents

    def roulette_selection(self, fitness, population_size):

        # Computes the totallity of the population fitness
        population_fitness = sum(fitness)

        # Computes for each chromosome the probability
        chromosome_probabilities = [fitness[chromosome]/population_fitness for chromosome in range (population_size)]

        # Selects two elements of the fitness list based on the computed probabilities
        fit1 = np.random.choice(fitness, p=chromosome_probabilities)
        fit2 = np.random.choice(fitness, p=chromosome_probabilities)

        #finds the index of the parents
        parent1 = fitness.index(fit1)
        parent2 = fitness.index(fit2)

        return parent1, parent2


    #criar outra funçao crossover para combinar os dois pais
    def generate_next_population(self, population):
        total_population = len(population)
        new_population = []


        fitness = self.evaluate_fitness(population)

        top_fit = max(fitness)  # value of the fittest element
        index = fitness.index(top_fit) # most fit element index
        elite = copy.deepcopy(population[index])   # actual element

        new_population.append(elite)


        for i in range (total_population - 1):
            if random.random() < 0.2:
                # randomly selected element passes to next generation
                parent = population[random.randrange(total_population)]
                self.mutation(parent)
                new_population.append(parent)
            else:
                #crossover between 2 parents
                parent1, parent2 = self.select_parents(fitness, self.parents_algorithm)
                # child = population[parent1][:round(self.team.n_projects/2)] + population[parent2][round(self.team.n_projects/2):]
                child = self.select_crossover(population[parent1], population[parent2], self.crossover_algorithm)
                self.mutation(child)
                new_population.append(child)


        return new_population, top_fit

    def select_crossover(self, parent1, parent2, choice):
        if choice == 1:
            return self.crossover1(parent1, parent2)
        elif choice == 2:
            return self.crossover2(parent1, parent2)
        else:
            return self.crossover3(parent1, parent2)


    def crossover1(self, parent1, parent2):
        return parent1[:round(self.team.n_projects/2)] + parent2[round(self.team.n_projects/2):]

    def crossover2(self, parent1, parent2):
        return parent2[:round(self.team.n_projects/2)] + parent1[round(self.team.n_projects/2):]

    def crossover3(self, parent1, parent2):
        if random.choice([True, False]):
            return self.crossover1(parent1, parent2)
        else:
            return self.crossover2(parent1, parent2)

    def mutation(self, chromosome):
        percentage = 0.05
        for i in range(len(chromosome)):
            for j in range (len(chromosome[0])):
                if random.random() < percentage:
                    if(chromosome[i][j] == 1):
                        chromosome[i][j] = 0
                    else:
                        chromosome[i][j] = 1


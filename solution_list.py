from solution import Solution
from dishes_list import DishesList
from restrictions import Limits
import random
import matplotlib.pyplot as plt

class SolutionList(list):

    def __init__(self, dishes_list: DishesList, limits: Limits):
        super().__init__()
        self.dishes_list = dishes_list
        self.limits = limits

    def __str__(self):
        tmp = ""
        for chromosome in self:
            tmp += f"{chromosome}\n"
        return f"{tmp}"

    def calculate_carbs(self):
        total_carbs = 0
        for chromosome in self:
            total_carbs += chromosome.carbs
        return total_carbs
    
    def check(self, parameter):
        x = random.randint(0,99)
        if x < parameter: return True
        else: return False

    def one_point_crossover(self, parent_1: Solution, parent_2: Solution):
        break_point = random.randint(1, len(parent_1.chromosome)-1)
        child = Solution(self.dishes_list, self.limits)
        child.chromosome = parent_1.chromosome[:break_point] + parent_2.chromosome[break_point:]
        child.calculate()
        if child.valid(): return child
        else: return parent_1

    def two_points_crossover(self, parent_1: Solution, parent_2: Solution):
        break_point1 = random.randint(1, len(parent_1.chromosome)-1)
        break_point2 = random.randint(break_point1, len(parent_1.chromosome)-1)
        child = Solution(self.dishes_list, self.limits)
        child.chromosome = parent_1.chromosome[:break_point1] + parent_2.chromosome[break_point1:break_point2] + parent_1.chromosome[break_point2:]
        child.calculate()
        if child.valid(): return child
        else: return parent_1

    def uniform_crossover(self, parent_1: Solution, parent_2: Solution):
        key = []
        for i in range(len(parent_1.chromosome)):
            gen = random.randint(0,1)
            key.append(gen)

        child = Solution(self.dishes_list, self.limits)
        child.chromosome = []
        for i in range(len(key)):
            if key[i] == 1: child.chromosome.append(parent_1.chromosome[i])
            else: child.chromosome.append(parent_2.chromosome[i])
        child.calculate()
        if child.valid(): return child
        else: return parent_1
    
    def tournament_selection(self):
        ticket_1 = random.randint(0, self.limits.size-1)
        ticket_2 = random.randint(0, self.limits.size-1)
        if self[ticket_1].carbs > self[ticket_2].carbs: return self[ticket_1]
        else: return self[ticket_2]

    def roulette_selection(self):
        roulette_list = []
        total_carbs = self.calculate_carbs()
        sum = 0
        for solution in self:
            value = int(1000*solution.carbs/total_carbs)
            sum += value
            roulette_list.append(sum)

        ticket = random.randint(0, 998)
        win = 0
        for i, value in enumerate(roulette_list):
            if ticket < value: 
                win = i
                break
        return self[win]

    def rank_selection(self):
        number_of_ranking = 5
        for i in range(len(self)):
            self.sort(key=lambda x:x.carbs, reverse=True)
        no = random.randint(0, number_of_ranking)
        return self[no]

    def elitist_strategy(self):
        best_solution = Solution(self.dishes_list, self.limits)
        self.rank_selection()
        best_solution = self[0]
        return best_solution

    def init_population(self):
        index = 0
        print("--- generation: 1 ---")
        while True:
            new_chromosome = Solution(self.dishes_list, self.limits)
            new_chromosome.random_solution()
            new_chromosome.calculate()
            if new_chromosome.valid(): 
                index += 1
                self.append(new_chromosome)
                print(f"{index}. {new_chromosome}")
            if len(self) == self.limits.size: break
        carbs = self.calculate_carbs()
        print(f"Carbs: {carbs}\n")
        return carbs

    def create_generation(self):
        new_generation = SolutionList(self.dishes_list, self.limits)

        # --- elitist strategy ---
        child = self.elitist_strategy()
        new_generation.append(child)
        print(f"1. {child}")

        # for i in range(1, self.limits.size): if you use elitist strategy
        for i in range(self.limits.size):

            # --- selection ---
            parent_1 = self.tournament_selection()
            parent_2 = self.tournament_selection()

            #parent_1 = self.rank_selection()
            #parent_2 = self.rank_selection()

            #parent_1 = self.roulette_selection()
            #parent_2 = self.roulette_selection()

            # --- crossover ---
            if self.check(self.limits.crossover_rate): child = self.one_point_crossover(parent_1, parent_2)
            if self.check(self.limits.crossover_rate): child = self.two_points_crossover(parent_1, parent_2)
            #if self.check(self.limits.crossover_rate): child = self.uniform_crossover(parent_1, parent_2)
            else: child = parent_1

            # --- mutation or inversion ---
            #if self.check(self.limits.mutation_rate): child.mutation()
            if self.check(self.limits.mutation_rate): child.inversion()
            new_generation.append(child)
            print(f"{i+1}. {child}")

        self = new_generation
        carbs = self.calculate_carbs()
        print(f"Carbs: {carbs}\n")
        return carbs

    def genetic_algorithm(self):
        carbs_list = []
        carbs = self.init_population()
        carbs_list.append(carbs)
        for generation in range(self.limits.generations-1):
            print(f"--- generation: {generation+2} ---")
            carbs = self.create_generation()
            carbs_list.append(carbs)
        self.print_plot(carbs_list)

    def print_plot(self, carbs_list):
        plt.plot(carbs_list)
        plt.xlabel('Generations')
        plt.ylabel('Carbohydrates')
        plt.title("Values of carbs during the generations")
        plt.show()




            

from dishes_list import DishesList
from restrictions import Limits
import random

class Solution:

    # solution has: chromosome, carbs, kcal, fat, protein, numbers, dishes_list

    def __init__(self, dishes_list: DishesList, limits: Limits):
        self.dishes_list = dishes_list
        self.limits = limits

    def __str__(self):
        tmp = ""
        for number in self.numbers:
            tmp += f" {number}"
        return f"No.{tmp} - {self.kcal} kcal, {self.protein} protein, {self.fat} fat, {self.carbs} carbs"

    def random_solution(self):
        chromosome = []
        for gens in range(len(self.dishes_list)):
            chromosome.append(0)

        meals = []
        for number in range(self.limits.number_of_meals):
            new_meal = random.randint(0, len(self.dishes_list)-1)
            meals.append(new_meal)
            chromosome[new_meal] = 1
        self.chromosome = chromosome

    def calculate(self):
        total_carbs = 0
        total_kcal = 0
        total_fat = 0
        total_protein = 0
        numbers = []
        for i in range(0, len(self.chromosome)):
            if self.chromosome[i] == 1:
                total_carbs += int(self.dishes_list[i].carbs)
                total_kcal += int(self.dishes_list[i].kcal)
                total_fat += int(self.dishes_list[i].fat)
                total_protein += int(self.dishes_list[i].protein)
                numbers.append(self.dishes_list[i].number)
        self.carbs = total_carbs
        self.kcal = total_kcal 
        self.fat = total_fat
        self.protein = total_protein 
        self.numbers = numbers

    def valid(self):
        if self.kcal > self.limits.kcal_max:
            return False
        if self.kcal < self.limits.kcal_min:
            return False
        if self.fat > self.limits.fat_max:
            return False
        if self.fat < self.limits.fat_min:
            return False
        if self.protein < self.limits.protein_min:
            return False
        if self.protein > self.limits.protein_max:
            return False
        else: 
            return True
        
    def mutation(self):
        temp = Solution(self.dishes_list, self.limits)
        temp.chromosome = self.chromosome.copy()
        gen = random.randint(0,len(temp.chromosome)-1)

        if temp.chromosome[gen] == 0: temp.chromosome[gen] = 1
        else: temp.chromosome[gen] = 0
        temp.calculate()
        if temp.valid(): 
            self = temp

    def inversion(self):
        temp = Solution(self.dishes_list, self.limits)
        temp.chromosome = self.chromosome.copy()

        point1 = random.randint(0,len(temp.chromosome)-1)
        point2 = random.randint(point1,len(temp.chromosome)-1)
        tab = temp.chromosome[point1:point2]
        new_tab = []
        for i in range(len(tab) - 1, -1, -1): # start, end, step
            new_tab.append(tab[i])

        new_chromosome = temp.chromosome[:point1] + new_tab + temp.chromosome[point2:]
        temp.chromosome = new_chromosome
        temp.calculate()
        if temp.valid(): self = temp








from dishes_list import DishesList
from solution_list import SolutionList
from restrictions import Limits
import matplotlib.pyplot as plt

# limits
kcal_max = 2100
kcal_min = 1800

fat_min = 40
fat_max = 1000

protein_min = 70
protein_max = 100

# carbs - as more as possible

meals = 3
size = 10

mutation_rate = 80 # percent
crossover_rate = 80 # percent

no_of_generations = 100

limits = Limits(kcal_min, kcal_max, fat_min, fat_max, protein_min, protein_max, meals, size, mutation_rate, crossover_rate, no_of_generations)
data = DishesList()
data.load_data()

solution = SolutionList(data, limits)
solution.genetic_algorithm()

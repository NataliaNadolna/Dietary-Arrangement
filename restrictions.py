class Limits:
    def __init__(self, kcal_min, kcal_max, fat_min, fat_max, protein_min, protein_max, number_of_meals, size, mutation_rate, crossover_rate, generations):
        self.kcal_min = kcal_min
        self.kcal_max = kcal_max
        self.fat_min = fat_min
        self.fat_max = fat_max
        self.protein_min = protein_min
        self.protein_max = protein_max
        self.number_of_meals = number_of_meals
        self.size = size
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.generations = generations
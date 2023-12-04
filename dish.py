class Dish:
    def __init__(self, number, kcal, protein, fat, carbs):
        self.number = number
        self.kcal = kcal
        self.protein = protein
        self.fat = fat
        self.carbs = carbs

    def __str__(self):
        return f"No. {self.number} - {self.kcal} kcal, {self.protein} protein, {self.fat} fat, {self.carbs} carbs"


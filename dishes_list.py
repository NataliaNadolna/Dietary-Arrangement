from dish import Dish

class DishesList(list):
    def __init__(self):
        super().__init__()

    def __str__(self):
        dishes_list = ""
        for i in range(len(self)):
            dishes_list += f"{self[i]}\n"
        return dishes_list

    def load_data(self):
        file = open("_Genetic Algorythm/dishes.txt", "r")
        for i, line in enumerate(file.readlines()):
            new_line = line.strip()
            new_line = new_line.split(" ")
            number, kcal, protein, fat, carbs = new_line[0], new_line[1], new_line[2], new_line[3], new_line[4]
            new_dish = Dish(number, kcal, protein, fat, carbs)
            self.append(new_dish)
            print(f"{i+1}. {new_dish}")
        print("\n")
        file.close
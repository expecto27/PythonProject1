from typing import List
import random

class UniformCrossoverOperator:
    def __init__(self, random_generator: random.Random):
        self.random = random_generator

    def perform_crossover(self, parent_pairs: List[List[int]], population: List[str]) -> List[str]:
        offspring = []

        for pair in parent_pairs:
            if len(pair) != 2:
                raise ValueError("Каждая пара должна содержать ровно два родителя.")

            parent1 = population[pair[0]]
            parent2 = population[pair[1]]

            if len(parent1) != len(parent2):
                raise ValueError("Генотипы родителей должны быть одинаковой длины.")

            print("Выполняется равномерный кроссовер между:")
            print(f"Родитель 1: {parent1}")
            print(f"Родитель 2: {parent2}")

            for j in range(3):
                child_genotype = ""
                for i in range(len(parent1)):
                    from_parent1 = self.random.choice([True, False])
                    gene = parent1[i] if from_parent1 else parent2[i]
                    child_genotype += gene

                offspring.append(child_genotype)
                print(f"Потомок {j + 1}: {child_genotype}")

        return offspring
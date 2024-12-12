from typing import List
import random

class TwoPointCrossover:
    def __init__(self, random_generator: random.Random):
        self.random = random_generator

    def perform_crossover(self, parent_pairs: List[List[int]], population: List[str]) -> List[str]:
        offspring = []

        for pair in parent_pairs:
            parent1 = population[pair[0]]
            parent2 = population[pair[1]]

            point1 = self.random.randint(0, len(parent1) - 1)
            point2 = self.random.randint(0, len(parent1) - 1)

            if point1 > point2:
                point1, point2 = point2, point1

            for i in range(3):
                child = ""

                if i == 0:
                    child = parent1[:point1] + parent2[point1:point2] + parent1[point2:]
                elif i == 1:
                    child = parent2[:point1] + parent1[point1:point2] + parent2[point2:]
                else:
                    new_point1 = self.random.randint(0, len(parent1) - 1)
                    new_point2 = self.random.randint(0, len(parent1) - 1)
                    if new_point1 > new_point2:
                        new_point1, new_point2 = new_point2, new_point1

                    child = parent1[:new_point1] + parent2[new_point1:new_point2] + parent1[new_point2:]

                offspring.append(child)

        return offspring
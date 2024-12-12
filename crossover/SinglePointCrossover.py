from typing import List
import random

class SinglePointCrossover:
    def __init__(self, random_generator: random.Random):
        self.random = random_generator

    def perform_crossover(self, parent_pairs: List[List[int]], population: List[str]) -> List[str]:
        offspring = []

        for pair in parent_pairs:
            parent1 = population[pair[0]]
            parent2 = population[pair[1]]

            for i in range(3):
                crossover_point = self.random.randint(0, len(parent1) - 1)

                child1 = parent1[:crossover_point] + parent2[crossover_point:]
                child2 = parent2[:crossover_point] + parent1[crossover_point:]

                if i == 0:
                    offspring.append(child1)
                elif i == 1:
                    offspring.append(child2)
                else:
                    child3 = parent1[:crossover_point] + parent2[crossover_point:]
                    offspring.append(child3)

        return offspring
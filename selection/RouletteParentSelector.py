from typing import List
import random

from selection.ParentSelector import ParentSelector


class RouletteParentSelector(ParentSelector):
    def __init__(self, random_generator: random.Random):
        self.random = random_generator

    def select_parents(self, population: List[str], fitness_scores: List[float], num_pairs: int) -> List[List[int]]:
        parent_pairs = []
        total_fitness = sum(fitness_scores)

        for _ in range(num_pairs):
            parent1 = self.select_one(fitness_scores, total_fitness)
            parent2 = parent1
            while parent2 == parent1:
                parent2 = self.select_one(fitness_scores, total_fitness)

            parent_pairs.append([parent1, parent2])

        return parent_pairs

    def select_one(self, fitness_scores: List[float], total_fitness: float) -> int:
        r = self.random.random() * total_fitness
        cumulative_sum = 0

        for i, fitness in enumerate(fitness_scores):
            cumulative_sum += fitness
            if cumulative_sum >= r:
                return i

        return len(fitness_scores) - 1
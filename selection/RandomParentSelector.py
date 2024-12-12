from typing import List
import random

from selection.ParentSelector import ParentSelector


class RandomParentSelector(ParentSelector):
    def __init__(self, random_generator: random.Random):
        self.random = random_generator

    def select_parents(self, population: List[str], fitness_scores: List[float], num_pairs: int) -> List[List[int]]:
        parent_pairs = []

        for _ in range(num_pairs):
            parent1 = self.random.randint(0, len(population) - 1)
            parent2 = parent1
            while parent2 == parent1:
                parent2 = self.random.randint(0, len(population) - 1)

            parent_pairs.append([parent1, parent2])

        return parent_pairs
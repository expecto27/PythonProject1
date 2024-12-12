from typing import List
import random

from selection.ParentSelector import ParentSelector


class RankParentSelector(ParentSelector):
    def __init__(self, random_generator: random.Random):
        self.random = random_generator

    def select_parents(self, population: List[str], fitness_scores: List[float], num_pairs: int) -> List[List[int]]:
        parent_pairs = []
        ranked_indices = self.rank_population(fitness_scores)

        for _ in range(num_pairs):
            parent1 = ranked_indices[self.random.randint(0, len(ranked_indices) - 1)]
            parent2 = parent1
            while parent2 == parent1:
                parent2 = ranked_indices[self.random.randint(0, len(ranked_indices) - 1)]

            parent_pairs.append([parent1, parent2])

        return parent_pairs

    def rank_population(self, fitness_scores: List[float]) -> List[int]:
        indices = list(range(len(fitness_scores)))
        indices.sort(key=lambda i: fitness_scores[i], reverse=True)
        return indices
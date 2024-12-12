from typing import List
import random

from selection.ParentSelector import ParentSelector


class TournamentParentSelector(ParentSelector):
    def __init__(self, random_generator: random.Random, tournament_size: int):
        self.random = random_generator
        self.tournament_size = tournament_size

    def select_parents(self, population: List[str], fitness_scores: List[float], num_pairs: int) -> List[List[int]]:
        parent_pairs = []

        for _ in range(num_pairs):
            parent1 = self.select_one(population, fitness_scores)
            parent2 = parent1
            while parent2 == parent1:
                parent2 = self.select_one(population, fitness_scores)

            parent_pairs.append([parent1, parent2])

        return parent_pairs

    def select_one(self, population: List[str], fitness_scores: List[float]) -> int:
        best_index = -1
        best_fitness = -1

        for _ in range(self.tournament_size):
            random_index = self.random.randint(0, len(population) - 1)
            if fitness_scores[random_index] > best_fitness:
                best_fitness = fitness_scores[random_index]
                best_index = random_index

        return best_index
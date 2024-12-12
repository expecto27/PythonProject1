from typing import List
import random

from entity import Pack


class RandomWithControl:
    def __init__(self, random_generator: random.Random):
        self.random = random_generator

    def generate_population(self, population: List[str], items: List[Pack], population_size: int, max_weight: int):
        for _ in range(population_size):
            chromosome = ['0'] * len(items)
            current_weight = 0

            for gene_index in range(len(items)):
                random_index = self.random.randint(0, len(items) - 1)
                item = items[random_index]

                if not item.used and (current_weight + item.weight <= max_weight):
                    current_weight += item.weight
                    chromosome[random_index] = '1'
                    item.used = True

            self.reset_items_state(items)
            population.append(''.join(chromosome))

    def reset_items_state(self, items: List[Pack]):
        for item in items:
            item.used = False
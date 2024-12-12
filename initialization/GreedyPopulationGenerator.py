from typing import List
import random

from entity import Pack


class GreedyPopulationGenerator:
    def __init__(self, random_generator: random.Random):
        self.random = random_generator

    def generate_population(self, population: List[str], items: List[Pack], population_size: int, max_weight: int):
        for _ in range(population_size):
            chromosome = ['0'] * len(items)
            current_weight = 0

            for gene_index in range(len(items)):
                selected_index = self.ruletka_index(items)
                if selected_index != -1:
                    item = items[selected_index]

                    if (current_weight + item.weight <= max_weight) and chromosome[selected_index] == '0':
                        current_weight += item.weight
                        chromosome[selected_index] = '1'
                        item.used = True

            self.reset_items_state(items)
            population.append(''.join(chromosome))

    def ruletka_index(self, items: List[Pack]) -> int:
        P = self.random.random()
        sum_fract = 0
        total_fraction = self.calculate_total_fraction(items)

        for i, item in enumerate(items):
            if not item.used:
                sum_fract += item.value_per_weight / total_fraction
                if P <= sum_fract:
                    return i
        return -1

    def calculate_total_fraction(self, items: List[Pack]) -> float:
        total_fraction = 0
        for item in items:
            if not item.used:
                total_fraction += item.value_per_weight
        return total_fraction

    def reset_items_state(self, items: List[Pack]):
        for item in items:
            item.used = False
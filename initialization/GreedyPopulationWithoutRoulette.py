from typing import List

from entity.Pack import Pack


class GreedyPopulationWithoutRoulette:
    def generate_population(self, population: List[str], items: List[Pack], population_size: int, max_weight: int):
        for _ in range(population_size):
            items.sort(key=lambda item: item.value_per_weight, reverse=True)

            chromosome = ['0'] * len(items)
            current_weight = 0

            for gene_index, item in enumerate(items):
                if not item.used and (current_weight + item.weight <= max_weight):
                    current_weight += item.weight
                    chromosome[gene_index] = '1'
                    item.used = True

            self.reset_items_state(items)
            population.append(''.join(chromosome))

    def reset_items_state(self, items: List[Pack]):
        for item in items:
            item.used = False
from typing import List
import random

class GenotypeModificationHandler:
    def __init__(self, random_generator: random.Random):
        self.random = random_generator

    def handle_constraints(self, population: List[str], max_weight: int, weights: List[int]) -> List[str]:
        for i in range(len(population)):
            genes = list(population[i])
            total_weight = 0

            for j in range(len(genes)):
                if genes[j] == '1':
                    total_weight += weights[j]

            while total_weight > max_weight:
                random_gene_index = self.random.randint(0, len(genes) - 1)
                if genes[random_gene_index] == '1':
                    genes[random_gene_index] = '0'
                    total_weight -= weights[random_gene_index]

            population[i] = ''.join(genes)

        return population
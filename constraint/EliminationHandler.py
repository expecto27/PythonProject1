from typing import List

class EliminationHandler:
    def handle_constraints(self, population: List[str], max_weight: int, weights: List[int]) -> List[str]:
        valid_population = []

        for chromosome in population:
            total_weight = 0
            genes = list(chromosome)
            for i, gene in enumerate(genes):
                if gene == '1':
                    total_weight += weights[i]

            if total_weight <= max_weight:
                valid_population.append(chromosome)

        return valid_population
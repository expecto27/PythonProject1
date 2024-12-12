from typing import List

class EncodingWithOperatorsHandler:
    def handle_constraints(self, population: List[str], max_weight: int, weights: List[int]) -> List[str]:
        valid_population = []

        for chromosome in population:
            genes = list(chromosome)
            total_weight = 0

            for i, gene in enumerate(genes):
                if gene == '1':
                    total_weight += weights[i]
                    if total_weight > max_weight:
                        break

            if total_weight <= max_weight:
                valid_population.append(chromosome)
            else:
                for i in range(len(genes) - 1, -1, -1):
                    if genes[i] == '1':
                        genes[i] = '0'
                        total_weight -= weights[i]
                        if total_weight <= max_weight:
                            break

                if total_weight <= max_weight:
                    valid_population.append(''.join(genes))

        return valid_population
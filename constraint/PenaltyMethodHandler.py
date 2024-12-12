from typing import List

from entity import Pack


class PenaltyMethodHandler:
    PENALTY_PER_KG = 50

    def __init__(self, packs: List[Pack]):
        self.packs = packs

    def handle_constraints(self, population: List[str], max_weight: int, weights: List[int]) -> List[str]:
        valid_population = []

        for chromosome in population:
            genes = list(chromosome)
            total_weight = 0
            total_value = 0

            for j, gene in enumerate(genes):
                if gene == '1':
                    total_weight += weights[j]
                    total_value += self.packs[j].value

            if total_weight > max_weight:
                excess_weight = total_weight - max_weight
                penalty = excess_weight * self.PENALTY_PER_KG
                total_value -= penalty

                total_value = max(total_value, 0)

                print(f"Хромосома {chromosome} превышает вес на {excess_weight} кг! Применен штраф: {penalty}, новая ценность: {total_value}")

            if total_value > 0:
                valid_population.append(chromosome)

        return valid_population
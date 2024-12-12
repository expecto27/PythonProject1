from typing import List
import random

class InversionMutationOperator:
    def __init__(self, random_generator: random.Random):
        self.random = random_generator

    def mutate(self, offspring: List[str], mutation_rate: float):
        for i in range(len(offspring)):
            if self.random.random() < mutation_rate:
                genotype = offspring[i]
                length = len(genotype)

                if length < 2:
                    continue

                point1 = self.random.randint(0, length - 2)
                point2 = point1 + self.random.randint(1, length - point1)

                mutated_genotype = list(genotype)
                for j in range(point1, point2):
                    mutated_genotype[j] = '1' if mutated_genotype[j] == '0' else '0'

                offspring[i] = ''.join(mutated_genotype)

                print(f"\033[32mИнверсионная мутация: Хромосома {i + 1} изменена, гены [{point1}-{point2 - 1}] инвертированы\033[0m")
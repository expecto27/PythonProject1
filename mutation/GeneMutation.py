from typing import List
import random

class GeneMutation:
    def __init__(self, random_generator: random.Random):
        self.random = random_generator

    def mutate(self, offspring: List[str], mutation_rate: float):
        for i in range(len(offspring)):
            if self.random.random() < mutation_rate:
                genes = list(offspring[i])
                mutation_index = self.random.randint(0, len(genes) - 1)
                genes[mutation_index] = '1' if genes[mutation_index] == '0' else '0'
                offspring[i] = ''.join(genes)
                print(f"\033[33mМутация: Хромосома {i + 1}, изменён ген {mutation_index}\033[0m")
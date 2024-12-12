from typing import List
import random

class ChromosomeMutation:
    def __init__(self, random_generator: random.Random):
        self.random = random_generator

    def mutate(self, offspring: List[str], mutation_rate: float):
        for i in range(len(offspring)):
            if self.random.random() < mutation_rate:
                genes = list(offspring[i])

                for j in range(len(genes)):
                    genes[j] = '1' if genes[j] == '0' else '0'

                offspring[i] = ''.join(genes)
                print(f"\033[33mХромосомная мутация: Хромосома {i + 1} инвертирована\033[0m")
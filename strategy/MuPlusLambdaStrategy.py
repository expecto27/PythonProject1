from typing import List

class MuPlusLambdaStrategy:
    def form_next_generation(self, population: List[str], offspring: List[str]) -> List[str]:
        next_generation = population.copy()
        next_generation.extend(offspring)
        return next_generation
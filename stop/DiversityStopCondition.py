from typing import List

class DiversityStopCondition:
    def __init__(self, min_diversity: float):
        self.min_diversity = min_diversity

    def should_stop(self, current_generation: int, fitness_evaluations: int, population: List[str]) -> bool:
        unique_chromosomes = set(population)
        diversity = len(unique_chromosomes) / len(population)
        return diversity <= self.min_diversity
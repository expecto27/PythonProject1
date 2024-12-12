from typing import List

class FitnessEvaluationStopCondition:
    def __init__(self, max_fitness_evaluations: int):
        self.max_fitness_evaluations = max_fitness_evaluations

    def should_stop(self, current_generation: int, fitness_evaluations: int, population: List[str]) -> bool:
        return fitness_evaluations >= self.max_fitness_evaluations
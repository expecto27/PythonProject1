from typing import List

class GenerationStopCondition:
    def __init__(self, max_generations: int):
        self.max_generations = max_generations

    def should_stop(self, current_generation: int, fitness_evaluations: int, population: List[str]) -> bool:
        return current_generation >= self.max_generations
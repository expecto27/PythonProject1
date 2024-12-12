from typing import List, Tuple
import random
from entity.Pack import Pack

from constraint.EliminationHandler import EliminationHandler
from constraint.EncodingWithOperatorsHandler import EncodingWithOperatorsHandler
from constraint.GenotypeModificationHandler import GenotypeModificationHandler
from constraint.PenaltyMethodHandler import PenaltyMethodHandler
from crossover.SinglePointCrossover import SinglePointCrossover
from crossover.TwoPointCrossover import TwoPointCrossover
from crossover.UniformCrossoverOperator import UniformCrossoverOperator
from initialization.GreedyPopulationGenerator import GreedyPopulationGenerator
from initialization.GreedyPopulationWithoutRoulette import GreedyPopulationWithoutRoulette
from initialization.RandomWithControl import RandomWithControl
from mutation.ChromosomeMutation import ChromosomeMutation
from mutation.GeneMutation import GeneMutation
from mutation.InversionMutationOperator import InversionMutationOperator
from selection import ParentSelector
from selection.RandomParentSelector import RandomParentSelector
from selection.RouletteParentSelector import RouletteParentSelector
from selection.TournamentParentSelector import TournamentParentSelector
from stop.DiversityStopCondition import DiversityStopCondition
from stop.FitnessEvaluationStopCondition import FitnessEvaluationStopCondition
from stop.GenerationStopCondition import GenerationStopCondition
from strategy.MuLambdaStrategy import MuLambdaStrategy
from strategy.MuPlusLambdaStrategy import MuPlusLambdaStrategy


def main():
    print("Введите кол во особей в популяции : ")
    population_size = int(input())
    max_weight = 100
    num_parent_pairs = population_size // 2
    population = []
    packs = create_packs()
    random_generator = random.Random()
    mutation_rate = 0.0

    print("Выберите условие остановки:")
    print("1 - По числу поколений")
    print("2 - По числу вычислений приспособленности")
    print("3 - По разнообразию")
    stop_condition_choice = int(input())
    stop_condition = None
    if stop_condition_choice == 1:
        print("Введите максимальное число поколений:")
        max_generations = int(input())
        stop_condition = GenerationStopCondition(max_generations)
    elif stop_condition_choice == 2:
        print("Введите максимальное число вычислений приспособленности:")
        max_fitness_evaluations = int(input())
        stop_condition = FitnessEvaluationStopCondition(max_fitness_evaluations)
    elif stop_condition_choice == 3:
        print("Введите минимальное разнообразие (0-1):")
        min_diversity = float(input())
        stop_condition = DiversityStopCondition(min_diversity)
    else:
        stop_condition = GenerationStopCondition(100)

    print("Выберите метод генерации популяции:")
    print("1 - Жадный с рулеткой")
    print("2 - Жадный без рулетки")
    print("3 - Случайный с контролем")
    generator_choice = int(input())
    generator = None
    if generator_choice == 1:
        generator = GreedyPopulationGenerator(random_generator)
    elif generator_choice == 2:
        generator = GreedyPopulationWithoutRoulette()
    else:
        generator = RandomWithControl(random_generator)

    generator.generate_population(population, packs, population_size, max_weight)
    if generator_choice == 1:
        constraint_handler = GenotypeModificationHandler(random_generator)
        population = constraint_handler.handle_constraints(population, max_weight, extract_weights(packs))

    print("Выберите метод отбора родителей:")
    print("1 - Случайный")
    print("2 - Турнирный")
    print("3 - Пропорциональный (рулетка)")
    selection_choice = int(input())
    parent_selector = None
    if selection_choice == 1:
        parent_selector = RandomParentSelector(random_generator)
    elif selection_choice == 2:
        print("Введите размер турнира:")
        tournament_size = int(input())
        parent_selector = TournamentParentSelector(random_generator, tournament_size)
    elif selection_choice == 3:
        parent_selector = RouletteParentSelector(random_generator)
    else:
        parent_selector = RandomParentSelector(random_generator)

    print("Выберите метод кроссовера:")
    print("1 - Одноточечный")
    print("2 - Двухточечный")
    print("3 - Универсальный")
    crossover_choice = int(input())
    crossover_operator = None
    if crossover_choice == 1:
        crossover_operator = SinglePointCrossover(random_generator)
    elif crossover_choice == 2:
        crossover_operator = TwoPointCrossover(random_generator)
    elif crossover_choice == 3:
        crossover_operator = UniformCrossoverOperator(random_generator)
    else:
        raise ValueError("Некорректный выбор метода кроссовера")

    print("Выберите метод мутации:")
    print("1 - Генная мутация")
    print("2 - Хромосомная мутация")
    print("3 - Инверсионная мутация")
    mutation_choice = int(input())
    print("Введите вероятность мутации Например (0.1) для 10%")
    mutation_rate = float(input())
    mutation_operator = None
    if mutation_choice == 1:
        mutation_operator = GeneMutation(random_generator)
    elif mutation_choice == 2:
        mutation_operator = ChromosomeMutation(random_generator)
    elif mutation_choice == 3:
        mutation_operator = InversionMutationOperator(random_generator)
    else:
        raise ValueError("Некорректный выбор метода мутации")

    print("Выберите метод обработки ограничений:")
    print("1 - Элиминация")
    print("2 - Метод штрафов")
    print("3 - Кодировка + операторы")
    print("4 - Модификация генотипа")
    constraint_choice = int(input())
    constraint_handler = None
    if constraint_choice == 1:
        constraint_handler = EliminationHandler()
    elif constraint_choice == 2:
        constraint_handler = PenaltyMethodHandler(packs)
    elif constraint_choice == 3:
        constraint_handler = EncodingWithOperatorsHandler()
    elif constraint_choice == 4:
        constraint_handler = GenotypeModificationHandler(random_generator)
    else:
        constraint_handler = EliminationHandler()

    print("Выберите стратегию формирования следующего поколения:")
    print("1 - μ+λ")
    print("2 - μ,λ")
    strategy_choice = int(input())
    strategy = None
    if strategy_choice == 1:
        strategy = MuPlusLambdaStrategy()
    elif strategy_choice == 2:
        strategy = MuLambdaStrategy()
    else:
        print("Некорректный выбор! По умолчанию используется стратегия μ+λ.")
        strategy = MuPlusLambdaStrategy()

    population = constraint_handler.handle_constraints(population, max_weight, extract_weights(packs))

    current_generation = 0
    fitness_evaluations = 0

    best_overall_individual = None
    best_overall_weight = 0
    best_overall_value = 0

    while not stop_condition.should_stop(current_generation, fitness_evaluations, population):
        print(f"\033[31mПоколение {current_generation}:\033[0m")

        print("\033[32mРодители:\033[0m")
        print_formatted_population(population, packs)

        fitness_scores = calculate_fitness(population, packs)

        parent_pairs = parent_selector.select_parents(population, fitness_scores, num_parent_pairs)
        offspring = crossover_operator.perform_crossover(parent_pairs, population)

        mutation_operator.mutate(offspring, mutation_rate)

        weights = extract_weights(packs)
        offspring = constraint_handler.handle_constraints(offspring, max_weight, weights)

        print("\033[34mДети:\033[0m")
        print_formatted_population(offspring, packs)

        next_generation = strategy.form_next_generation(population, offspring)
        population = select_next_generation(next_generation, packs, population_size, parent_selector)

        print("\033[31mНовое поколение:\033[0m")
        print_formatted_population(population, packs)

        best_individual = find_best_individual(population, packs)
        best_data = get_chromosome_data(best_individual, packs)
        print(f"\033[32mЛучшая особь в поколении: {best_individual}  вес - {best_data[0]}, ценность - {best_data[1]}\033[0m")

        if best_overall_individual is None or best_data[1] > best_overall_value:
            best_overall_individual = best_individual
            best_overall_weight = best_data[0]
            best_overall_value = best_data[1]

        current_generation += 1
        fitness_evaluations += len(population)

    print("\033[31mЛучшая особь за все поколения:\033[0m")
    print(f"\033[32m{best_overall_individual}  вес - {best_overall_weight}, ценность - {best_overall_value}\033[0m")

def get_chromosome_data(chromosome: str, packs: List[Pack]) -> Tuple[int, int]:
    total_weight = 0
    total_value = 0
    genes = list(chromosome)
    for i in range(len(genes)):
        if genes[i] == '1':
            total_weight += packs[i].weight
            total_value += packs[i].value
    return total_weight, total_value

def find_best_individual(population: List[str], packs: List[Pack]) -> str:
    return max(population, key=lambda ind: calculate_fitness([ind], packs)[0])

def select_next_generation(population: List[str], packs: List[Pack], population_size: int, parent_selector: ParentSelector) -> List[str]:
    fitness_scores = calculate_fitness(population, packs)
    selected_pairs = parent_selector.select_parents(population, fitness_scores, population_size // 2)

    selected_generation = []
    for pair in selected_pairs:
        selected_generation.append(population[pair[0]])
        if len(selected_generation) < population_size:
            selected_generation.append(population[pair[1]])

    if len(selected_generation) > population_size:
        selected_generation = selected_generation[:population_size]

    return selected_generation

def create_packs() -> List[Pack]:
    packs = [
        Pack(24, 29),
        Pack(29, 30),
        Pack(6, 12),
        Pack(11, 10),
        Pack(20, 22),
        Pack(3, 4),
        Pack(15, 16),
        Pack(3, 22),
        Pack(15, 8),
        Pack(21, 16),
        Pack(4, 6),
        Pack(16, 16),
        Pack(24, 20),
        Pack(29, 16),
        Pack(24, 10)
    ]
    return packs

def calculate_fitness(population: List[str], packs: List[Pack]) -> List[float]:
    fitness_scores = []
    for chromosome in population:
        fitness = 0
        genes = list(chromosome)
        for i in range(len(genes)):
            if genes[i] == '1':
                fitness += packs[i].value_per_weight
        fitness_scores.append(fitness)
    return fitness_scores

def print_formatted_population(population: List[str], packs: List[Pack]):
    for i in range(len(population)):
        chromosome = population[i]
        total_weight = 0
        total_value = 0
        genes = list(chromosome)
        for j in range(len(genes)):
            if genes[j] == '1':
                total_weight += packs[j].weight
                total_value += packs[j].value
        print(f"{i + 1})  {chromosome}  вес - {total_weight}  ценность - {total_value}")

def print_parent_pairs(parent_pairs: List[List[int]], population: List[str], packs: List[Pack]):
    pair_number = 1
    for pair in parent_pairs:
        print(f"Пара {pair_number}:")
        pair_number += 1
        print_parent_details(pair[0], population, packs)
        print_parent_details(pair[1], population, packs)

def print_parent_details(parent_index: int, population: List[str], packs: List[Pack]):
    chromosome = population[parent_index]
    total_weight = 0
    total_value = 0
    genes = list(chromosome)
    for i in range(len(genes)):
        if genes[i] == '1':
            total_weight += packs[i].weight
            total_value += packs[i].value
    print(f"  {chromosome}  вес - {total_weight}  ценность - {total_value}")

def extract_weights(packs: List[Pack]) -> List[int]:
    weights = []
    for pack in packs:
        weights.append(pack.weight)
    return weights

if __name__ == "__main__":
    main()
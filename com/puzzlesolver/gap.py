
from com.puzzlesolver.mutation_class import MutationClass
from com.puzzlesolver.selection import Selection
from com.puzzlesolver.cross_over import Crossover
from com.puzzlesolver.generate_best_mutation import GenerateBestMutation


class Gap:
    def __init__(self):
        print("This is Artificial Intelligent Puzzle Solver, \nBekir Duran")

    def run(self):
        best_list = Selection.create_population(20)
        cross_list = Crossover.crossover(best_list)

        mut = MutationClass(cross_list)
        mutation_list = mut.mutate()

        best = GenerateBestMutation(mutation_list)
        best.find_best()



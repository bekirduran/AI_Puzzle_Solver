import numpy as np

from com.puzzlesolver.fitness import Fitness


# this class generates a random population as much as the number of iteration entered
from com.puzzlesolver.puzzle_image import PuzzleImage


class Selection:
    @staticmethod
    def create_population(iter):
        img = PuzzleImage()
        list = []
        for _ in range(iter):
            x1 = img.shuffled_image()
            list.append(x1)
        list.sort(key=Fitness.fitness)
        best = list[0:2]
        return best

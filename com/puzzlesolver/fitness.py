import numpy as np


# This class calculating fitness value according to given array
from com.puzzlesolver.puzzle_image import PuzzleImage

img = PuzzleImage()
m1 = img.original_image()


class Fitness:

    @staticmethod
    def fitness(y):
        error = np.mean(m1 != y)
        return error

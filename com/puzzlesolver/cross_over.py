import numpy as np


# This class generating new list item given first of list item row and second of list item row
class Crossover:

    @staticmethod
    def crossover(best):
        row_begin_index = 0
        row_half = 2

        cross_list = []
        for i in range(len(best) - 1):
            first_part1 = best[i][row_begin_index:row_half, :]
            first_part2 = best[i + 1][row_half:, :]

            cross_list.append(np.concatenate((first_part1, first_part2)))

            second_part1 = best[i][row_half:, :]
            second_part2 = best[i + 1][row_begin_index:row_half, :]

            cross_list.append(np.concatenate((second_part2, second_part1)))
        return cross_list

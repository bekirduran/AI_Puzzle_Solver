import numpy as np

from com.puzzlesolver.puzzle_image import PuzzleImage


F = PuzzleImage()
f = F.original_image()
# This function return replica element of the Picture
def detect_same_value(M):
    array_first_index = 1
    array_second_index = M.shape[0]
    M_array = M.reshape(array_first_index, array_second_index , M.shape[1],M.shape[2])

    result = []
    for i in range((len(M_array[0]) - 1)):
        for j in range(i + 1, (len(M_array[0]))):
            if (M_array[0][i] == M_array[0][j]).all():
                result.append(M_array[0][j])
    return result


# This function return missing element of the Picture
def detect_deficient_value(F, M):
    array_first_index = 1
    array_second_index = M.shape[0]

    M_array = M.reshape(array_first_index, array_second_index ,  M.shape[1],M.shape[2])
    M_array_mean = []
    for m in M_array[0]:
        M_array_mean.append(np.mean(m))

    Final_array = F.reshape(array_first_index, array_second_index , M.shape[1],M.shape[2])

    f = Final_array[0]
    result = []

    for m in f:
        mean = np.mean(m)
        if mean not in M_array_mean:
            result.append(m)
    return result


# This method using replacing the replica values with missing values.
def replace_value(M, Missing, Replica):

    replica_means = []
    for i in Replica:
        replica_means.append(np.mean(i))
    missing_means = []
    for i in Missing:
        missing_means.append(np.mean(i))

    M_means = []
    for m in M:
        M_means.append(np.mean(m))

    missing_index = 0

    for item in replica_means:
        if item in M_means:
            i = np.where(M_means == item)[0]
            M[i[0]] = Missing[missing_index]
            missing_index += 1
    return M


# This method combining the detect_deficient_value, replace_value and replace_value. Finally creating new clear matrix
def mutation(cross_list):

    m1 = f
    new_cross_list = []
    for i in cross_list:
        replica_nums = detect_same_value(i)
        missing_nums = detect_deficient_value(m1, i)
        new_value = replace_value(i, missing_nums, replica_nums)
        new_cross_list.append(new_value)
    return new_cross_list


class MutationClass:

    def __init__(self, cross_list):
        self.cross_list = cross_list

    def mutate(self):
        return mutation(self.cross_list)

import random
import numpy as np
from skimage.util import montage
import matplotlib.image as mpimg
from matplotlib.pyplot import cm

from com.puzzlesolver.fitness import Fitness
#fig = plt.figure(figsize=(5,5))
#plt.imshow(mon,cmap=plt.cm.gray)

iteration = 0
# This function swapping array with random generating indexes
def mutation_swap(item):
    global  iteration
    first_item = np.copy(item)
    rate = Fitness.fitness(first_item)

    array_first_index = 1
    array_second_index = item.shape[0]

    M_array = item.reshape(array_first_index, array_second_index, item.shape[1],item.shape[2])

    first_index = random.randint(0, 24)
    second_index = random.randint(0, 24)

    temp = np.copy(M_array[0][first_index])
    M_array[0][first_index] = M_array[0][second_index]
    M_array[0][second_index] = temp

    new_rate = Fitness.fitness(M_array[0])

    if new_rate < rate:
        iteration += 1
        print("********************")
        print(f"Iteration: {iteration} and rate: {new_rate}")
        mon = montage(M_array[0])
        #Save image
        mpimg.imsave(rf'Generation/sample_{iteration}.jpg',mon,cmap=cm.gray)
        return M_array[0]
    else:
        return first_item


# This function try to find fit best array
def find_best(mutation_list):
    generation_number = 0
    fistIndex = 0
    mutation_list.sort(key=Fitness.fitness)

    result = mutation_list[fistIndex]
    rate = Fitness.fitness(result)
    while rate > 0.0:
        generation_number += 1
        result = mutation_swap(result)
        rate = Fitness.fitness(result)
    print(f"Generation number: {generation_number} ")


class GenerateBestMutation:

    def __init__(self, mutation_list):
        self.mutation_list = mutation_list

    def find_best(self):
        find_best(self.mutation_list)
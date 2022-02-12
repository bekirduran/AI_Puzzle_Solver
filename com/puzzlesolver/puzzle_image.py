import numpy as np
from skimage.io import imread
from skimage.transform import resize
from skimage.util.shape import view_as_blocks

path = "test_image.png"


class PuzzleImage:

    # puzzle_montage = montage(puzzle_blocks)

    def original_image(self):
        puzzle = imread(path, as_gray=True)
        puzzle = resize(puzzle, (400, 400))
        puzzle_shape = (80, 80)
        puzzle_blocks_orig = view_as_blocks(puzzle, block_shape=puzzle_shape)
        puzzle_blocks = puzzle_blocks_orig
        puzzle_blocks = puzzle_blocks.reshape((-1,) + puzzle_shape)

        return puzzle_blocks

    def shuffled_image(self):
        image = self.original_image()
        np.random.shuffle(image)
        return image

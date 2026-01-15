import numpy as np

def generate_heightmap(width=8, height=8, scale=1, noise_function=None):
  heightmap = np.zeros((height, width))
  for y in range(height):
    for x in range(width):
      heightmap[y][x] = noise_function(scale*(x / width), scale*(y / height))
  return heightmap
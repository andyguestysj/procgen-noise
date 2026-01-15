import math
from project.core.utils.miscfuncs import octave_noise
def island_mask(x, y, size):
  # x, y should be normalised to [-1,1]
  dist = math.sqrt(x * x + y * y)
  return max(0, 1 - dist)

# combine mask with noise
def generate_island(width, height, noise_fn):
  result = []
  for y in range(height):
    row = []
    for x in range(width):
      nx = (x / (width - 1)) * 2 - 1  # Normalize to [-1, 1]
      ny = (y / (height - 1)) * 2 - 1
      value = octave_noise(nx, ny, noise_fn)
      masked = value * island_mask(nx, ny, 1.0)
      row.append(f"{masked:.2f}")
    result.append(row)
  return result

def generate_terrain(width, height, noise_fn):
  result = []
  for y in range(height):
    row = []
    for x in range(width):
      nx = (x / (width - 1)) * 2 - 1  # Normalize to [-1, 1]
      ny = (y / (height - 1)) * 2 - 1
      value = octave_noise(nx, ny, noise_fn)
      row.append(f"{value:.2f}")
    result.append(row)
  return result


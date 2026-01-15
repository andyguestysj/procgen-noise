
import math
import random

from project.core.utils.miscfuncs import fade, lerp, grad

class PerlinNoise2D:
  def __init__(self, seed=0) :
    random.seed(seed)
    # Permutation table
    self.p = [i for i in range (256)]
    random.shuffle(self.p)
    self.p += self.p # Repeat to avoid overflow
    
  def noise (self, x, y):
    # Find unit grid cell containing point
    X= int (math.floor (x)) & 255
    Y = int (math.floor (y)) & 255
  
    # Relative coordinates within cell
    xf = x - math.floor(x)
    yf = y - math.floor(y)
  
    # Hash coordinates of the corners
    aa = self.p[self.p[X] + Y]
    ab = self.p[self.p[X] + + 1]
    ba = self.p[self.p[X + 1] + Y]
    bb = self.p[self.p[X +1] + Y +1]
    
    # Compute fade curves
    u = fade (xf)
    v = fade (yf)
    
    # Blend results from corners  
    x1 = lerp(grad(aa, xf, yf), grad(ba, xf - 1, yf), u)
    x2 = lerp(grad(ab, xf, yf - 1), grad(bb, xf - 1, yf -1), u)

    return (lerp(x1, x2, v) + 1) / 2 # Normalize to [0,1]
  
# Example usage: create a small noise map
if __name__ == "__main__" : # Test

  width, height = 8, 8  
  noise = PerlinNoise2D(seed=42)
  for y in range (height) :
    row = [f"{noise.noise (x * 0.2, y * 0.2):.2f}" for x in range(width)]
    print (" ".join(row) )
    
  print("------------------")
  
  for y in range (height) :
    row = [f"{noise.noise (x * 0.5, y * 0.5):.2f}" for x in range(width)]
    print (" ".join(row) )
    
    
    
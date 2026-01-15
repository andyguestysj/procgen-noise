import random
from core.utils.miscfuncs import normalize

def midpoint_displacement_1D(size, seed=0, disp=1.0, roughness=0.5, left=0.0, right=0.0):
  
  if size < 2:
    raise ValueError("Size must be at least 2")
  
  n=1
  while (2**n)+1 < size:
    n += 1
  size = (2**n) + 1
  
  rnd = random.Random(seed)
  h = [0.0] * size
  h[0] = float(left)
  h[-1] = float(right)
  
  step = size - 1
  scale = float(disp)
  
  while step > 1:
    half_step = step // 2
    
    for i in range(0, size - 1, step):
      mid = i + half_step
      avg = (h[i] + h[i + step]) * 0.5
      h[mid] = avg + (rnd.uniform(-scale, scale))
    scale *= float(roughness)
    step = half_step
    
  return normalize(h)

def diamond_square(size, seed=0, disp=1.0, roughness=0.5):
  
  n=0
  while (2**n) < size:
    n += 1
  size = (2**n)+1
  
  rnd = random.Random(seed)
  grid = [[0.0 for _ in range(size)] for _ in range(size)]
  
  grid[0][0] = rnd.uniform(-disp, disp)
  grid[0][size-1] = rnd.uniform(-disp, disp)
  grid[size-1][0] = rnd.uniform(-disp, disp)
  grid[size-1][size-1] = rnd.uniform(-disp, disp)
  
  step = size-1
  scale = float(disp)

  while step > 1:
    half_step = step // 2
    
    for y in range(0, n - 1, step):
      for x in range(0, n - 1, step):
        avg = (grid[y][x] + grid[y + step][x] + grid[y][x + step] + grid[y + step][x + step]) * 0.25
        grid[y + half_step][x + half_step] = avg + rnd.uniform(-scale, scale)
    
    for y in range(0, size, half_step):
      for x in range((y + half_step) % step, size, step):
        s = []
        if y - half_step >= 0:
          s.append(grid[y - half_step][x])
        if y + half_step < size:
          s.append(grid[y + half_step][x])
        if x - half_step >= 0:
          s.append(grid[y][x - half_step])
        if x + half_step < size:
          s.append(grid[y][x + half_step])
        
        avg = sum(s) / len(s)
        grid[y][x] = avg + rnd.uniform(-scale, scale)
    
    scale *= roughness
    step = half_step
  
  return grid
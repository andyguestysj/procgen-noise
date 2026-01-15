import math
import random

def fade (t):
  # Fade function for smooth interpolation
  return t * t * t * (t * (t * 6 - 15) + 10)

def lerp(a, b, t):
  # Linear interpolation
  return a + t * (b - a)

def grad(hash, x, y) :
  # Convert hash to gradient direction
  h = hash & 3
  u = x if h < 2 else y
  v = y if h < 2 else x
  
  return (u if (h & 1) == 0 else -u) + (v if (h & 2) == 0 else -v)

def octave_noise(x, y, noise_fn, octaves=4, persistence=0.5, lacunarity=2.0):
  value = 0
  frequency = 1
  amplitude = 1
  max_amplitude = 0  # Used for normalizing result to [0,1]
  
  for _ in range(octaves):
      value  += noise_fn(x * frequency, y * frequency) * amplitude
      max_amplitude += amplitude
      amplitude *= persistence
      frequency *= lacunarity
  
  return value / max_amplitude  
  
def normalize(vals):
  min_val = min(vals)
  max_val = max(vals)
  range_val = max_val - min_val
  if range_val == 0:
      return [0.0 for _ in vals]
  return [(v - min_val) / range_val for v in vals]

def normalize_2D(grid):
  lo = min(min(row) for row in grid)
  hi = max(max(row) for row in grid)
  rng = hi - lo
  if rng == 0:
      return [[0.0 for _ in row] for row in grid] 
  return [[(val - lo) / rng for val in row] for row in grid]

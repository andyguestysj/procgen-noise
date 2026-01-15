from core.utils import perlin2d
from core.utils.midpoint_disp import diamond_square
from core.utils.surfaceplot3D import generate_3D_surfaceplot
from core.utils.heightmap2d import generate_2D_heightmap
from core.utils.genHM import generate_heightmap
from opensimplex import OpenSimplex
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, FloatSlider, IntSlider
class Game:
  def __init__(self):
      pass
  
  def run(self):
    #noise = perlin2d.PerlinNoise2D(seed=42).noise
    #noise = OpenSimplex(seed=42).noise2
    #island = generate_island(50, 50, noise.noise)
    #land = generate_terrain(50, 50, noise.noise)    
    #osland = simplex(seed=42, width=50, height=50)
    
    #heightmap = generate_heightmap(64, 64, 1, noise)
    
    # generate_2D_heightmap(island)
    #generate_3D_surfaceplot(heightmap)
        
    #heights = midpoint_displacement_1D(size=33, seed=7, disp=1.0, roughness=0.55, left=0.2, right=0.2)
    #print("Sample heights: ", [round(v,2) for v in heights[:12]])
    
    hm = diamond_square(size=30, seed=42, disp=0.5, roughness=0.55)
    #print("Sample heights: ", [round(v,2) for v in hm[len(hm)//2][:12]])
    generate_3D_surfaceplot(hm)
    #generate_2D_heightmap(hm)
    
    
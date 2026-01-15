import numpy as np
import matplotlib.pyplot as plt

def generate_2D_heightmap(data):
  heightmap = np.array(data, dtype=float)
  plt.imshow(heightmap, cmap='terrain')
  plt.colorbar(label='Height')
  plt.title('2D Heightmap')
  plt.xlabel('X-axis')
  plt.ylabel('Y-axis')
  plt.show() 

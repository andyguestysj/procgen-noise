import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

def generate_3D_surfaceplot(data):
  Z = np.array(data)

  rows, cols = Z.shape
  X, Y = np.meshgrid(range(cols), range(rows))

  fig = plt.figure()
  ax = fig.add_subplot(111, projection="3d")

  ax.plot_surface(X, Y, Z, cmap="terrain")

  ax.set_title("Height Map as 3D Surface")
  ax.set_xlabel("X")
  ax.set_ylabel("Y")
  ax.set_zlabel("Height")

  plt.show() 
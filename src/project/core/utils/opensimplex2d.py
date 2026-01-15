from opensimplex import OpenSimplex

def simplex(seed=42, width=8, height=8):
  seed = 42
  noise = OpenSimplex(seed)
  
  result = []
  for y in range(height):
    row = []
    for x in range(width):
      value = noise.noise2(x * 0.2, y * 0.2)
      normalized = (value + 1) / 2  # Normalize to [0, 1]
      row.append(f"{normalized:.2f}")
    result.append(row)
  
  return result
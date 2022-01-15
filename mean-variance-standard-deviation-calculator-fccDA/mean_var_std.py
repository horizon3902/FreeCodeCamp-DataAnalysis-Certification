import numpy as np

def calculate(l):
  
  if len(l) != 9:
    raise ValueError("List must contain nine numbers.")
  
  l = np.reshape(np.array(l),(3,3))
  
  calculations = {
    'mean': [np.mean(l, axis=0).tolist(), np.mean(l, axis=1).tolist(), np.mean(l.flatten()).tolist()],
    'variance': [np.var(l, axis=0).tolist(), np.var(l, axis=1).tolist(), np.var(l.flatten()).tolist()],
    'standard deviation': [np.std(l, axis=0).tolist(), np.std(l, axis=1).tolist(), np.std(l.flatten()).tolist()],
    'max': [np.max(l, axis=0).tolist(), np.max(l, axis=1).tolist(), np.max(l.flatten()).tolist()],
    'min': [np.min(l, axis=0).tolist(), np.min(l, axis=1).tolist(), np.min(l.flatten()).tolist()],
    'sum': [np.sum(l, axis=0).tolist(), np.sum(l, axis=1).tolist(), np.sum(l.flatten()).tolist()]
  }
  
  return calculations
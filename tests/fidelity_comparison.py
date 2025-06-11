import json
import numpy as np
with open('kernels/kernel_simple.json') as f:
    k1 = np.array(json.load(f))
with open('kernels/kernel_simple.json') as f:
    k2 = np.array(json.load(f))
numerator = np.trace(k1 @ k2.T)
denominator = np.sqrt(np.trace(k1 @ k1.T) * np.trace(k2 @ k2.T))
fidelity = numerator / denominator
print(f"Kernel similarity (fidelity-style): {fidelity:.4f}")

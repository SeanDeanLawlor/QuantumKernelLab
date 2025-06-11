from qiskit.utils import QuantumInstance
from qiskit import Aer
from qiskit_machine_learning.kernels import QuantumKernel
from qiskit.circuit.library import TwoLocal
import numpy as np
import json
import os

# Input features (example)
X = np.random.rand(10, 2)

# Variational feature map
feature_map = TwoLocal(rotation_blocks='ry', entanglement_blocks='cz', reps=2)

# Backend
backend = Aer.get_backend('aer_simulator_statevector')
qi = QuantumInstance(backend)

# Quantum kernel
kernel = QuantumKernel(feature_map=feature_map, quantum_instance=qi)
matrix = kernel.evaluate(x_vec=X)

# Export
os.makedirs("kernels", exist_ok=True)
with open("kernels/kernel_simple.json", "w") as f:
    json.dump(matrix.tolist(), f, indent=2)

print("✅ Exported kernel to kernels/kernel_simple.json")

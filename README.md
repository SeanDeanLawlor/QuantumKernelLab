# 🧠 QuantumKernelLab

**QuantumKernelLab** is a Qiskit-based Python project for generating, analyzing, and exporting quantum kernel matrices derived from variational quantum algorithms.

## 🔍 Features

- Generate quantum kernels using Qiskit algorithms (e.g., QAOA, VQE)
- Visualize and export kernels in JSON format
- Companion backend to [SandBox](https://github.com/SeanDeanLawlor/SandBox) for live Unity-based visualization
- Hypothesis testing: fidelity, noise sensitivity, and delta comparisons

## 🧪 Algorithms Supported

- **QAOA** (Quantum Approximate Optimization Algorithm)
- **VQE** (Variational Quantum Eigensolver)
- **Custom TwoLocal ansätze**

## 🧩 Structure

```
QuantumKernelLab/
├── generate_kernels.py           # Main entry point
├── kernels/                      # Output kernel JSONs
├── circuits/                     # Custom circuit definitions
├── tests/                        # Analysis scripts (e.g., fidelity)
└── docs/                         # (Empty for now)
```

## 📦 How to Use

```bash
pip install qiskit qiskit-machine-learning
python generate_kernels.py
```

Then load the generated `kernel_simple.json` into SandBox for visual comparison and noise simulation.

from qiskit.circuit.library import QAOAAnsatz
from qiskit_optimization.applications import Maxcut
graph_edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
maxcut = Maxcut(graph_edges)
qp = maxcut.to_quadratic_program()
qaoa = QAOAAnsatz(num_qubits=4, reps=1)
print(qaoa)

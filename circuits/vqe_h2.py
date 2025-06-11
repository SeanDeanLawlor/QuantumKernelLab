from qiskit_nature.second_q.drivers import PySCFDriver
from qiskit_nature.second_q.hamiltonians import ElectronicStructureProblem
from qiskit_nature.second_q.mappers import JordanWignerMapper
from qiskit.algorithms.minimum_eigensolvers import VQE
from qiskit.algorithms.optimizers import COBYLA
from qiskit.circuit.library import TwoLocal
from qiskit.utils import QuantumInstance
from qiskit import Aer

driver = PySCFDriver(atom='H .0 .0 .0; H .0 .0 0.74', basis='sto3g')
es_problem = ElectronicStructureProblem(driver)
second_q_op = es_problem.second_q_ops()[0]
mapper = JordanWignerMapper()
qubit_op = mapper.map(second_q_op)
ansatz = TwoLocal(rotation_blocks='ry', entanglement_blocks='cz', reps=1)
optimizer = COBYLA(maxiter=100)
qi = QuantumInstance(Aer.get_backend('aer_simulator_statevector'))
vqe = VQE(ansatz=ansatz, optimizer=optimizer, quantum_instance=qi)
result = vqe.compute_minimum_eigenvalue(qubit_op)
print(f"Computed ground state energy: {result.eigenvalue.real:.4f}")

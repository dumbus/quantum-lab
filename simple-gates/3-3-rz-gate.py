import matplotlib.pyplot as plt
from numpy import pi

from qiskit import *
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector, plot_histogram

from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit_aer import AerSimulator

SHOTS = 2000

q_reg = QuantumRegister(size=1, name='q_reg')
c_reg = ClassicalRegister(size=1, name='c_reg')
qc = QuantumCircuit(q_reg, c_reg)

# Set q_reg[0] to Superposition
qc.h(q_reg[0])

# Draw state of Qubits on Bloch Sphere before experiment
state = Statevector(qc)
plot = plot_bloch_multivector(state, title='Initital State', title_pad=-3)
plot.show()

# Apply Rx gate to q_reg[0]
qc.rz(pi/2, q_reg[0])

# Draw state of Qubits on Bloch Sphere after Rx-gate
state = Statevector(qc)
plot = plot_bloch_multivector(state, title='State after rotation around Z-axis', title_pad=-3)
plot.show()

# Show circuit
qc.measure(q_reg, c_reg)
qc.draw(output="mpl")
plt.show()

# ======================= Ideal Simulation =======================
def ideal_rz_distribution(shots):
  return {'0': shots // 2, '1': shots // 2}

ideal_counts = ideal_rz_distribution(SHOTS)
plot_histogram(ideal_counts, title='Qubits State (ideal simulation)', figsize=(8, 7))

# ======================= Local Simulation =======================
service = QiskitRuntimeService()
backend = service.get_backend('ibm_kyoto')
backend_sim = AerSimulator.from_backend(backend)
result = backend_sim.run(qc, shots=SHOTS).result()
counts = result.get_counts(qc)
plot_histogram(counts, title='Qubits State', figsize=(8, 7))
plt.show()
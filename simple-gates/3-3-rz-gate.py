import matplotlib.pyplot as plt
from numpy import pi

from qiskit import *
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector, plot_histogram
from qiskit.providers.fake_provider import GenericBackendV2

from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit_aer import AerSimulator

SHOTS = 2000
REG_SIZE = 1

q_reg = QuantumRegister(size=REG_SIZE, name='q_reg')
c_reg = ClassicalRegister(size=REG_SIZE, name='c_reg')
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

# ======================= Local Simulation (Real QC backend copy) =======================
# service = QiskitRuntimeService()
# backend = service.get_backend('ibm_kyoto')
# backend_sim = AerSimulator.from_backend(backend)
# simulation_result = backend_sim.run(qc, shots=SHOTS).result()
# simulation_counts = result.get_counts()

# ======================= Local Simulation (Generic backend) =======================
backend_local = GenericBackendV2(num_qubits = REG_SIZE * 2)
simulation_result = backend_local.run(qc, shots=SHOTS).result()
simulation_counts = simulation_result.get_counts()

plot_histogram(simulation_counts, title='Qubits State (realistic simulation)', figsize=(8, 7))
plt.show()
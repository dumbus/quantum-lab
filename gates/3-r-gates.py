import matplotlib.pyplot as plt
from numpy import pi

from qiskit import *
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector

from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit_aer import AerSimulator

SHOTS = 2000

q_reg = QuantumRegister(size=3, name='q_reg')
c_reg = ClassicalRegister(size=3, name='c_reg')
qc = QuantumCircuit(q_reg, c_reg)

# Draw state of Qubits on Bloch Sphere before experiment
state = Statevector(qc)
plot = plot_bloch_multivector(state, title='Initital State', title_pad=-3)
plot.show()

# Apply Rx gate to q_reg[0]
qc.rx(pi/2, q_reg[0])
# Apply Ry gate to q_reg[1]
qc.ry(pi/2, q_reg[1])
# Apply Rz gate to q_reg[2]
qc.rz(pi/2, q_reg[2])

# Draw state of Qubits on Bloch Sphere after Z-gate
state = Statevector(qc)
plot = plot_bloch_multivector(state, title='State after rotation', title_pad=-3)
plot.show()

# Show circuit
qc.measure(q_reg, c_reg)
qc.draw(output="mpl")
plt.show()

# ======================= Local Simulation =======================
# service = QiskitRuntimeService()
# backend = service.get_backend('ibm_kyoto')
# backend_sim = AerSimulator.from_backend(backend)
# result = backend_sim.run(qc, shots=SHOTS).result()
# counts = result.get_counts(qc)
# print(counts)
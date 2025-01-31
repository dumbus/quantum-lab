import matplotlib.pyplot as plt
from numpy import pi

from qiskit import *
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector, plot_histogram

from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit_aer import AerSimulator

SHOTS = 2000

q_reg = QuantumRegister(size=4, name='q_reg')
c_reg = ClassicalRegister(size=4, name='c_reg')
qc = QuantumCircuit(q_reg, c_reg)

qc.x(q_reg[2])
qc.x(q_reg[3])

# Draw state of Qubits on Bloch Sphere before experiment
state = Statevector(qc)
plot = plot_bloch_multivector(state, title='Initital State', title_pad=-3)
plot.show()

# Apply CRx-Gate with controlled qubit |0>
qc.crx(pi/2, q_reg[0], q_reg[1])

# Apply CRx-Gate with controlled qubit |1>
qc.crx(pi/2, q_reg[2], q_reg[3])

# Draw state of Qubits on Bloch Sphere after Rx-gate
state = Statevector(qc)
plot = plot_bloch_multivector(state, title='State after CRx-Gates', title_pad=-3)
plot.show()

qc.measure(q_reg, c_reg)
qc.draw(output="mpl")
plt.show()

# ======================= Local Simulation =======================
service = QiskitRuntimeService()
backend = service.get_backend('ibm_kyoto')
backend_sim = AerSimulator.from_backend(backend)
transpiled_circuit = transpile(qc, backend_sim)
result = backend_sim.run(transpiled_circuit, shots=SHOTS).result()
counts = result.get_counts()
plot_histogram(counts, title='Qubits State', figsize=(8, 7))
plt.show()
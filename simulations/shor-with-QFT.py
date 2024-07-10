import matplotlib.pyplot as plt
from numpy import pi

from qiskit import *
from qiskit.visualization import plot_histogram

from qiskit.circuit.library import QFT

from qiskit.providers.basic_provider import BasicSimulator
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit_aer import AerSimulator

SHOTS = 2000
REG_MAX = 3
REG_SIZE = REG_MAX + 1

q_reg_x = QuantumRegister(size=4, name='x')
q_reg_y = QuantumRegister(size=4, name='y')
c_reg = ClassicalRegister(size=4, name='c')
qc = QuantumCircuit(q_reg_x, q_reg_y, c_reg)

qc.h(q_reg_x[0])
qc.h(q_reg_x[1])
qc.h(q_reg_x[2])
qc.h(q_reg_x[3])

# Block 1
qc.x(q_reg_y[3])

# Block 2
qc.cx(q_reg_x[REG_MAX], q_reg_y[2])
qc.cx(q_reg_x[REG_MAX], q_reg_y[1])

# Block 3
qc.ccx(q_reg_x[REG_MAX - 1], q_reg_y[0], q_reg_y[2])
qc.ccx(q_reg_x[REG_MAX - 1], q_reg_y[2], q_reg_y[0])
qc.ccx(q_reg_x[REG_MAX - 1], q_reg_y[0], q_reg_y[2])

qc.ccx(q_reg_x[REG_MAX - 1], q_reg_y[1], q_reg_y[3])
qc.ccx(q_reg_x[REG_MAX - 1], q_reg_y[3], q_reg_y[1])
qc.ccx(q_reg_x[REG_MAX - 1], q_reg_y[1], q_reg_y[3])

qc.barrier()
qc.measure(q_reg_y, c_reg)

# Apply Quantum Fourier Transform to qubits of q_reg
qft_circuit = QFT(REG_SIZE, do_swaps=False, inverse=False)
qc.append(qft_circuit, q_reg_x)

QFT(REG_SIZE, do_swaps=False, inverse=False).decompose().draw(output="mpl")

qc.measure(q_reg_x, c_reg)
qc.draw(output="mpl")
plt.show()

# ======================= Local Simulation =======================
# service = QiskitRuntimeService()
# backend = service.get_backend('ibm_kyoto')
# backend_sim = AerSimulator.from_backend(backend)
# transpiled_circuit = transpile(qc, backend_sim)
# result = backend_sim.run(transpiled_circuit, shots=SHOTS).result()
# counts = result.get_counts()
# plot_histogram(counts, title='Конечное состояние регистра после симуляции', figsize=(8, 7))
# plt.show()
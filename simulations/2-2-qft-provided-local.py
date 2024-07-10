import matplotlib.pyplot as plt

from qiskit import *
from qiskit.circuit.library import QFT

from qiskit.providers.basic_provider import BasicSimulator
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit_aer import AerSimulator

REG_SIZE = 5
SHOTS = 1000

# initialize quantum register
q_reg = QuantumRegister(size=REG_SIZE, name='q_reg')

# initialize classical register
c_reg = ClassicalRegister(size=REG_SIZE, name='c_reg')

# initialize quantum curcuit with quantum register
qc = QuantumCircuit(q_reg, c_reg)

# Apply H gate to all qubits of q_reg
qc.h(q_reg)

# Apply Quantum Fourier Transform to qubits of q_reg
qft_circ = QFT(REG_SIZE, do_swaps=False, inverse=False)
qc.append(qft_circ, q_reg)

# Measure all qubits of q_reg to c_reg
qc.measure(q_reg, c_reg)

qc.draw(output="mpl")
plt.show()

# ======================= Local Simulation =======================
# get a real backend from the runtime service
service = QiskitRuntimeService()
backend = service.get_backend('ibm_kyoto')

# generate a simulator that mimics the real quantum system with the latest calibration results
backend_sim = AerSimulator.from_backend(backend)

# Transpile the ideal circuit to a circuit that can be directly executed by the backend
transpiled_circuit = transpile(qc, backend_sim)
 
# Run the transpiled circuit using the simulated backend
job = backend_sim.run(transpiled_circuit)
counts = job.result().get_counts()

print(counts)

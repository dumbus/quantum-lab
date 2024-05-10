import matplotlib.pyplot as plt

from qiskit import *

from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit_aer import AerSimulator

SHOTS = 2000

# initialize quantum register
q_reg = QuantumRegister(size=2, name='q_reg')

# initialize classical register
c_reg = ClassicalRegister(size=2, name='c_reg')

# initialize quantum curcuit with quantum register
qc = QuantumCircuit(q_reg, c_reg)

# Apply h gate to all qubits of q_reg
qc.h(q_reg)

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
 
# Run the transpiled circuit using the simulated backend
result = backend_sim.run(qc, shots=SHOTS).result()
counts = result.get_counts()

print(counts)
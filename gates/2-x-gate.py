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

# Apply x gate to first qubit of q_reg
qc.x(q_reg[0])

# Apply x gate to second qubit twice
qc.x(q_reg[1])
qc.x(q_reg[1])

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
import matplotlib.pyplot as plt

from qiskit import *
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector

from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit_aer import AerSimulator

SHOTS = 2000

# initialize quantum register
q_reg = QuantumRegister(size=1, name='q_reg')

# initialize classical register
c_reg = ClassicalRegister(size=1, name='c_reg')

# initialize quantum curcuit with quantum register
qc = QuantumCircuit(q_reg, c_reg)

# Draw state of Qubits on Bloch Sphere before experiment
state = Statevector(qc)
plot = plot_bloch_multivector(state, title='Initital State', title_pad=-3)
plot.show()

# Apply h gate to all qubits of q_reg
qc.h(q_reg)

# Draw state of Qubits on Bloch Sphere after Rx-gate
state = Statevector(qc)
plot = plot_bloch_multivector(state, title='State after H-Gate', title_pad=-3)
plot.show()

# Measure all qubits of q_reg to c_reg and draw circuit
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
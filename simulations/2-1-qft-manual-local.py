import matplotlib.pyplot as plt
from numpy import pi

from qiskit import *

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
# Measure all qubits of q_reg to c_reg
# qc.measure(q_reg, c_reg)

def qft_rotations(circuit, n):
    if n == 0:
        return circuit
    n -= 1
    circuit.h(n)
    for qubit in range(n):
        circuit.cp(pi/2**(n-qubit), qubit, n)
    qft_rotations(circuit, n)

def swap_registers(circuit, n):
    for qubit in range(n//2):
        circuit.swap(qubit, n-qubit-1)
    return circuit

def qft(circuit, n):
    """QFT on the first n qubits in circuit"""
    qft_rotations(circuit, n)
    swap_registers(circuit, n)
    return circuit

# Apply QFT to qubits of q_reg
qft(qc, REG_SIZE)

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

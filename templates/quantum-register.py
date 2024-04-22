import matplotlib.pyplot as plt
from qiskit import *

QUANTUM_REG_SIZE = 8

values = []

# initialize quantum register
q_reg = QuantumRegister(size=QUANTUM_REG_SIZE, name='q_reg')

# initialize classical register
c_reg = ClassicalRegister(size=1, name='c_reg')

# initialize quantum curcuit with quantum register
qc = QuantumCircuit(q_reg, c_reg)

# Apply H gate to all qubits of q_reg
# Measure all qubits of q_reg
for qubit_number in range(QUANTUM_REG_SIZE):
    qc.h(q_reg[qubit_number])
    qc.measure(q_reg[qubit_number], c_reg[0])

# print curcuit
qc.draw(output="mpl")
plt.show()
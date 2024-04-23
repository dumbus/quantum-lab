import matplotlib.pyplot as plt

from qiskit import *

REG_SIZE = 5

# initialize quantum register
q_reg = QuantumRegister(size=REG_SIZE, name='q_reg')

# initialize classical register
c_reg = ClassicalRegister(size=REG_SIZE, name='c_reg')

# initialize quantum curcuit with quantum register
qc = QuantumCircuit(q_reg, c_reg)

# Apply H gate to all qubits of q_reg
qc.h(q_reg)
# Measure all qubits of q_reg to c_reg
qc.measure(q_reg, c_reg)

# print curcuit
qc.draw(output="mpl")
plt.show()

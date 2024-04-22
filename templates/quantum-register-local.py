import matplotlib.pyplot as plt
from qiskit import *
from qiskit.providers.basic_provider import BasicSimulator

REG_SIZE = 2

# initialize quantum register
q_reg = QuantumRegister(size=REG_SIZE, name='q_reg')

# initialize classical register
c_reg = ClassicalRegister(size=REG_SIZE, name='c_reg')

# initialize quantum curcuit with quantum register
qc = QuantumCircuit(q_reg, c_reg)

# Apply H gate to all qubits of q_reg
# Measure all qubits of q_reg
for qubit_number in range(REG_SIZE):
    qc.h(q_reg[qubit_number])
    qc.measure(q_reg[qubit_number], c_reg[qubit_number])

# print curcuit
qc.draw(output="mpl")
plt.show()

# ======================= Local Simulation =======================
backend = BasicSimulator()
result = backend.run(qc).result()

bit_strings = result.get_counts()
print(bit_strings)
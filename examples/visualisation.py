# Bell state

import matplotlib.pyplot as plt

from qiskit import QuantumCircuit
 
# Create a new circuit with two qubits
qc = QuantumCircuit(2)
 
# Add a Hadamard gate to qubit 0
qc.h(0)
 
# Perform a controlled-X gate on qubit 1, controlled by qubit 0
qc.cx(0, 1)
 
# Return a drawing of the circuit using MatPlotLib (output="mpl")
qc.draw(output="mpl")
plt.show()

# Return a text drawing of the curcuit
# print(qc)
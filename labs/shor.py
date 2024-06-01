import matplotlib.pyplot as plt
from numpy import pi

from qiskit import *
from qiskit.visualization import plot_histogram
from qiskit.circuit.library import QFT

SHOTS = 2000
REG_MAX = 3
REG_SIZE = REG_MAX + 1

q_reg_x = QuantumRegister(size=4, name='x')
q_reg_y = QuantumRegister(size=4, name='y')
c_reg = ClassicalRegister(size=4, name='c')
qc = QuantumCircuit(q_reg_x, q_reg_y, c_reg)

# Генерация схемы для студента
student_id = int(input("Номер варианта: "))

if (student_id == 0):
  qc.h(q_reg_x[0])
  qc.h(q_reg_x[1])
  qc.h(q_reg_x[2])
  qc.h(q_reg_x[3])

  qc.barrier()

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

  qft_circuit = QFT(REG_SIZE, do_swaps=False, inverse=False)
  qc.append(qft_circuit, q_reg_x)
  qc.barrier()

  qc.measure(q_reg_x, c_reg)

elif (student_id >= 1 and student_id <= 10):
  qc.h(q_reg_x[0])
  qc.h(q_reg_x[1])
  qc.h(q_reg_x[2])
  qc.h(q_reg_x[3])

  qc.barrier()

  # Block 1
  qc.x(q_reg_y[3])

  # Block 2
  qc.cx(q_reg_x[REG_MAX], q_reg_y[1])
  qc.cx(q_reg_x[REG_MAX], q_reg_y[0])

  # Block 3
  qc.ccx(q_reg_x[REG_MAX - 1], q_reg_y[0], q_reg_y[2])
  qc.ccx(q_reg_x[REG_MAX - 1], q_reg_y[2], q_reg_y[0])
  qc.ccx(q_reg_x[REG_MAX - 1], q_reg_y[0], q_reg_y[2])

  qc.ccx(q_reg_x[REG_MAX - 1], q_reg_y[1], q_reg_y[3])
  qc.ccx(q_reg_x[REG_MAX - 1], q_reg_y[3], q_reg_y[1])
  qc.ccx(q_reg_x[REG_MAX - 1], q_reg_y[1], q_reg_y[3])

  qc.barrier()
  qc.measure(q_reg_y, c_reg)

  qft_circuit = QFT(REG_SIZE, do_swaps=False, inverse=False)
  qc.append(qft_circuit, q_reg_x)
  qc.barrier()

  qc.measure(q_reg_x, c_reg)

elif (student_id >= 11 and student_id <= 20):
  qc.h(q_reg_x[0])
  qc.h(q_reg_x[1])
  qc.h(q_reg_x[2])
  qc.h(q_reg_x[3])

  qc.barrier()

  # Block 1
  qc.x(q_reg_y[3])

  # Block 2
  qc.cx(q_reg_x[REG_MAX], q_reg_y[3])
  qc.cx(q_reg_x[REG_MAX], q_reg_y[2])

  # Block 3
  qc.ccx(q_reg_x[REG_MAX - 1], q_reg_y[0], q_reg_y[2])
  qc.ccx(q_reg_x[REG_MAX - 1], q_reg_y[2], q_reg_y[0])
  qc.ccx(q_reg_x[REG_MAX - 1], q_reg_y[0], q_reg_y[2])

  qc.ccx(q_reg_x[REG_MAX - 1], q_reg_y[1], q_reg_y[3])
  qc.ccx(q_reg_x[REG_MAX - 1], q_reg_y[3], q_reg_y[1])
  qc.ccx(q_reg_x[REG_MAX - 1], q_reg_y[1], q_reg_y[3])

  qc.barrier()
  qc.measure(q_reg_y, c_reg)

  qft_circuit = QFT(REG_SIZE, do_swaps=False, inverse=False)
  qc.append(qft_circuit, q_reg_x)
  qc.barrier()

  qc.measure(q_reg_x, c_reg)

elif (student_id >= 21 and student_id <= 30):
  qc.h(q_reg_x[0])
  qc.h(q_reg_x[1])
  qc.h(q_reg_x[2])
  qc.h(q_reg_x[3])

  qc.barrier()

  # Block 1
  qc.x(q_reg_y[3])

  # Block 2-1
  qc.cx(q_reg_x[REG_MAX], q_reg_y[3])
  qc.cx(q_reg_x[REG_MAX], q_reg_y[2])

  # Block 2-2
  qc.ccx(q_reg_x[REG_MAX], q_reg_y[0], q_reg_y[2])
  qc.ccx(q_reg_x[REG_MAX], q_reg_y[2], q_reg_y[0])
  qc.ccx(q_reg_x[REG_MAX], q_reg_y[0], q_reg_y[2])

  qc.ccx(q_reg_x[REG_MAX], q_reg_y[1], q_reg_y[3])
  qc.ccx(q_reg_x[REG_MAX], q_reg_y[3], q_reg_y[1])
  qc.ccx(q_reg_x[REG_MAX], q_reg_y[1], q_reg_y[3])

  qc.barrier()

  # Block 3
  qc.ccx(q_reg_x[REG_MAX - 1], q_reg_y[0], q_reg_y[2])
  qc.ccx(q_reg_x[REG_MAX - 1], q_reg_y[2], q_reg_y[0])
  qc.ccx(q_reg_x[REG_MAX - 1], q_reg_y[0], q_reg_y[2])

  qc.ccx(q_reg_x[REG_MAX - 1], q_reg_y[1], q_reg_y[3])
  qc.ccx(q_reg_x[REG_MAX - 1], q_reg_y[3], q_reg_y[1])
  qc.ccx(q_reg_x[REG_MAX - 1], q_reg_y[1], q_reg_y[3])

  qc.barrier()
  qc.measure(q_reg_y, c_reg)

  qft_circuit = QFT(REG_SIZE, do_swaps=False, inverse=False)
  qc.append(qft_circuit, q_reg_x)
  qc.barrier()

  qc.measure(q_reg_x, c_reg)

# Визуализация схемы QFT
# QFT(REG_SIZE, do_swaps=False, inverse=False).decompose().draw(output="mpl")

# Визуализация схемы
qc.draw(output="mpl")
plt.show()

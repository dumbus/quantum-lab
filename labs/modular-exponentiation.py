import matplotlib.pyplot as plt

from qiskit import *
from qiskit.visualization import plot_histogram
from qiskit.providers.fake_provider import GenericBackendV2

SHOTS = 2000

student_id = int(input("Номер варианта: "))

if (student_id == 0):
  q_reg_x = QuantumRegister(size=2, name='x')
  q_reg_y = QuantumRegister(size=4, name='y')
  c_reg = ClassicalRegister(size=4, name='c')
  qc = QuantumCircuit(q_reg_x, q_reg_y, c_reg)

  NUM_QUBITS = 10

  qc.h(q_reg_x[0])
  qc.h(q_reg_x[1])

  # Block 1
  qc.x(q_reg_y[3])

  qc.barrier()

  # Block 2
  qc.cx(q_reg_x[1], q_reg_y[2])
  qc.cx(q_reg_x[1], q_reg_y[1])

  qc.barrier()

  # Block 3
  qc.ccx(q_reg_x[0], q_reg_y[0], q_reg_y[2])
  qc.ccx(q_reg_x[0], q_reg_y[2], q_reg_y[0])
  qc.ccx(q_reg_x[0], q_reg_y[0], q_reg_y[2])

  qc.ccx(q_reg_x[0], q_reg_y[1], q_reg_y[3])
  qc.ccx(q_reg_x[0], q_reg_y[3], q_reg_y[1])
  qc.ccx(q_reg_x[0], q_reg_y[1], q_reg_y[3])

  qc.barrier()
  qc.measure(q_reg_y, c_reg)

  # Визуализация схемы
  qc.draw(output="mpl")
  plt.show()

elif (student_id >= 1 and student_id <= 5):
  ### N = 15, a = 13 ###
  q_reg_x = QuantumRegister(size=2, name='x')
  q_reg_y = QuantumRegister(size=4, name='y')
  c_reg = ClassicalRegister(size=4, name='c')
  qc = QuantumCircuit(q_reg_x, q_reg_y, c_reg)

  NUM_QUBITS = 10

  qc.h(q_reg_x[0])
  qc.h(q_reg_x[1])

  # Block 1
  qc.x(q_reg_y[3])

  qc.barrier()

  # Block 2
  qc.cx(q_reg_x[1], q_reg_y[1])
  qc.cx(q_reg_x[1], q_reg_y[0])

  qc.barrier()

  # Block 3
  qc.ccx(q_reg_x[0], q_reg_y[0], q_reg_y[2])
  qc.ccx(q_reg_x[0], q_reg_y[2], q_reg_y[0])
  qc.ccx(q_reg_x[0], q_reg_y[0], q_reg_y[2])

  qc.ccx(q_reg_x[0], q_reg_y[1], q_reg_y[3])
  qc.ccx(q_reg_x[0], q_reg_y[3], q_reg_y[1])
  qc.ccx(q_reg_x[0], q_reg_y[1], q_reg_y[3])

  qc.barrier()
  qc.measure(q_reg_y, c_reg)

elif (student_id >= 6 and student_id <= 10):
  ### N = 51, a = 16 ###
  q_reg_x = QuantumRegister(size=1, name='x')
  q_reg_y = QuantumRegister(size=6, name='y')
  c_reg = ClassicalRegister(size=6, name='c')
  qc = QuantumCircuit(q_reg_x, q_reg_y, c_reg)

  NUM_QUBITS = 13

  qc.h(q_reg_x[0])

  # Block 1
  qc.x(q_reg_y[5])

  qc.barrier()

  # Block 2
  qc.cx(q_reg_x[0], q_reg_y[5])
  qc.cx(q_reg_x[0], q_reg_y[1])

  qc.barrier()
  qc.measure(q_reg_y, c_reg)

elif (student_id >= 11 and student_id <= 15):
  ### N = 15, a = 2 ###
  q_reg_x = QuantumRegister(size=2, name='x')
  q_reg_y = QuantumRegister(size=4, name='y')
  c_reg = ClassicalRegister(size=4, name='c')
  qc = QuantumCircuit(q_reg_x, q_reg_y, c_reg)

  NUM_QUBITS = 10

  qc.h(q_reg_x[0])
  qc.h(q_reg_x[1])

  # Block 1
  qc.x(q_reg_y[3])

  qc.barrier()

  # Block 2
  qc.cx(q_reg_x[1], q_reg_y[3])
  qc.cx(q_reg_x[1], q_reg_y[2])

  qc.barrier()

  # Block 3
  qc.ccx(q_reg_x[0], q_reg_y[0], q_reg_y[2])
  qc.ccx(q_reg_x[0], q_reg_y[2], q_reg_y[0])
  qc.ccx(q_reg_x[0], q_reg_y[0], q_reg_y[2])

  qc.ccx(q_reg_x[0], q_reg_y[1], q_reg_y[3])
  qc.ccx(q_reg_x[0], q_reg_y[3], q_reg_y[1])
  qc.ccx(q_reg_x[0], q_reg_y[1], q_reg_y[3])

  qc.barrier()
  qc.measure(q_reg_y, c_reg)

elif (student_id >= 16 and student_id <= 20):
  ### N = 51, a = 35 ###
  q_reg_x = QuantumRegister(size=1, name='x')
  q_reg_y = QuantumRegister(size=6, name='y')
  c_reg = ClassicalRegister(size=6, name='c')
  qc = QuantumCircuit(q_reg_x, q_reg_y, c_reg)

  NUM_QUBITS = 13

  qc.h(q_reg_x[0])

  # Block 1
  qc.x(q_reg_y[5])

  qc.barrier()

  # Block 2
  qc.cx(q_reg_x[0], q_reg_y[4])
  qc.cx(q_reg_x[0], q_reg_y[0])

  qc.barrier()
  qc.measure(q_reg_y, c_reg)

elif (student_id >= 21 and student_id <= 25):
  ### N = 15, a = 8 ###
  qc.h(q_reg_x[0])
  qc.h(q_reg_x[1])

  # Block 1
  qc.x(q_reg_y[3])

  qc.barrier()

  # Block 2-1
  qc.cx(q_reg_x[1], q_reg_y[3])
  qc.cx(q_reg_x[1], q_reg_y[2])

  qc.barrier()

  # Block 2-2
  qc.ccx(q_reg_x[1], q_reg_y[0], q_reg_y[2])
  qc.ccx(q_reg_x[1], q_reg_y[2], q_reg_y[0])
  qc.ccx(q_reg_x[1], q_reg_y[0], q_reg_y[2])

  qc.ccx(q_reg_x[1], q_reg_y[1], q_reg_y[3])
  qc.ccx(q_reg_x[1], q_reg_y[3], q_reg_y[1])
  qc.ccx(q_reg_x[1], q_reg_y[1], q_reg_y[3])

  qc.barrier()

  # Block 3
  qc.ccx(q_reg_x[0], q_reg_y[0], q_reg_y[2])
  qc.ccx(q_reg_x[0], q_reg_y[2], q_reg_y[0])
  qc.ccx(q_reg_x[0], q_reg_y[0], q_reg_y[2])

  qc.ccx(q_reg_x[0], q_reg_y[1], q_reg_y[3])
  qc.ccx(q_reg_x[0], q_reg_y[3], q_reg_y[1])
  qc.ccx(q_reg_x[0], q_reg_y[1], q_reg_y[3])

  qc.barrier()
  qc.measure(q_reg_y, c_reg)

elif (student_id >= 26 and student_id <= 30):
  # N = 51, a = 50
  q_reg_x = QuantumRegister(size=1, name='x')
  q_reg_y = QuantumRegister(size=6, name='y')
  c_reg = ClassicalRegister(size=6, name='c')
  qc = QuantumCircuit(q_reg_x, q_reg_y, c_reg)

  NUM_QUBITS = 13

  qc.h(q_reg_x[0])

  # Block 1
  qc.x(q_reg_y[5])

  qc.barrier()

  # Block 2
  qc.cx(q_reg_x[0], q_reg_y[5])
  qc.cx(q_reg_x[0], q_reg_y[4])
  qc.cx(q_reg_x[0], q_reg_y[1])
  qc.cx(q_reg_x[0], q_reg_y[0])

  qc.barrier()
  qc.measure(q_reg_y, c_reg)

# Визуализация схемы
# qc.draw(output="mpl")
# plt.show()

# Используем симулятор для выполнения схемы
backend_local = GenericBackendV2(num_qubits = NUM_QUBITS)
simulation_result = backend_local.run(qc, shots=1000).result()
simulation_counts = simulation_result.get_counts()

# Получаем результаты измерений и визуализируем их
plot_histogram(simulation_counts, title='Конечное состояние регистра после симуляции', figsize=(8, 8))
plt.show()
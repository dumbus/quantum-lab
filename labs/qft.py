import matplotlib.pyplot as plt
from numpy import pi

from qiskit import *
from qiskit.visualization import plot_histogram
from qiskit.circuit.library import QFT

student_id = int(input("Номер варианта: "))

if (student_id == 0):
  REG_MAX = 3
  REG_SIZE = REG_MAX + 1

  q_reg_x = QuantumRegister(size=REG_SIZE, name='x')
  q_reg_y = QuantumRegister(size=REG_SIZE, name='y')
  c_reg = ClassicalRegister(size=REG_SIZE, name='c')
  qc = QuantumCircuit(q_reg_x, q_reg_y, c_reg)

  print("Рассматриваемая функция: f(x)=7^x mod 15")
  qc_title = "Квантовая схема для определения периода r функции f(x)=7^x mod 15"
  qc_qft_title = f"Квантовая схема квантового преобразования Фурье для функции f(x)=7^x mod 15"

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

  # Визуализация схемы
  qc.draw(output="mpl")
  plt.title(qc_title)
  plt.show()

elif (student_id >= 1 and student_id <= 5):
  REG_MAX = 3
  REG_SIZE = REG_MAX + 1

  q_reg_x = QuantumRegister(size=REG_SIZE, name='x')
  q_reg_y = QuantumRegister(size=REG_SIZE, name='y')
  c_reg = ClassicalRegister(size=REG_SIZE, name='c')
  qc = QuantumCircuit(q_reg_x, q_reg_y, c_reg)

  print("Рассматриваемая функция: f(x)=13^x mod 15")
  qc_qft_title = f"Квантовая схема квантового преобразования Фурье для функции f(x)=13^x mod 15"

elif (student_id >= 6 and student_id <= 10):
  REG_MAX = 5
  REG_SIZE = REG_MAX + 1

  q_reg_x = QuantumRegister(size=REG_SIZE, name='x')
  q_reg_y = QuantumRegister(size=REG_SIZE, name='y')
  c_reg = ClassicalRegister(size=REG_SIZE, name='c')
  qc = QuantumCircuit(q_reg_x, q_reg_y, c_reg)

  print("Рассматриваемая функция: f(x)=16^x mod 51")
  qc_qft_title = f"Квантовая схема квантового преобразования Фурье для функции f(x)=16^x mod 51"

elif (student_id >= 11 and student_id <= 15):
  REG_MAX = 3
  REG_SIZE = REG_MAX + 1

  q_reg_x = QuantumRegister(size=REG_SIZE, name='x')
  q_reg_y = QuantumRegister(size=REG_SIZE, name='y')
  c_reg = ClassicalRegister(size=REG_SIZE, name='c')
  qc = QuantumCircuit(q_reg_x, q_reg_y, c_reg)

  print("Рассматриваемая функция: f(x)=2^x mod 15")
  qc_qft_title = f"Квантовая схема квантового преобразования Фурье для функции f(x)=2^x mod 15"

elif (student_id >= 16 and student_id <= 20):
  REG_MAX = 5
  REG_SIZE = REG_MAX + 1

  q_reg_x = QuantumRegister(size=REG_SIZE, name='x')
  q_reg_y = QuantumRegister(size=REG_SIZE, name='y')
  c_reg = ClassicalRegister(size=REG_SIZE, name='c')
  qc = QuantumCircuit(q_reg_x, q_reg_y, c_reg)

  print("Рассматриваемая функция: f(x)=35^x mod 51")
  qc_qft_title = f"Квантовая схема квантового преобразования Фурье для функции f(x)=35^x mod 51"

elif (student_id >= 21 and student_id <= 25):
  REG_MAX = 3
  REG_SIZE = REG_MAX + 1

  q_reg_x = QuantumRegister(size=REG_SIZE, name='x')
  q_reg_y = QuantumRegister(size=REG_SIZE, name='y')
  c_reg = ClassicalRegister(size=REG_SIZE, name='c')
  qc = QuantumCircuit(q_reg_x, q_reg_y, c_reg)

  print("Рассматриваемая функция: f(x)=8^x mod 15")
  qc_qft_title = f"Квантовая схема квантового преобразования Фурье для функции f(x)=8^x mod 15"

elif (student_id >= 26 and student_id <= 30):
  REG_MAX = 5
  REG_SIZE = REG_MAX + 1

  q_reg_x = QuantumRegister(size=REG_SIZE, name='x')
  q_reg_y = QuantumRegister(size=REG_SIZE, name='y')
  c_reg = ClassicalRegister(size=REG_SIZE, name='c')
  qc = QuantumCircuit(q_reg_x, q_reg_y, c_reg)

  print("Рассматриваемая функция: f(x)=50^x mod 51")
  qc_qft_title = f"Квантовая схема квантового преобразования Фурье для функции f(x)=50^x mod 51"

# Визуализация схемы QFT
QFT(REG_SIZE, do_swaps=False, inverse=False).decompose().draw(output="mpl")
plt.title(qc_qft_title)
plt.show()

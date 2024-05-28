import random
import matplotlib.pyplot as plt

from qiskit import *
from qiskit.visualization import plot_histogram
from qiskit.providers.fake_provider import GenericBackendV2

def generate_assignment(student_id):
  random.seed(student_id)  # Используем номер студента как seed при генерации варианта

  num_qubits = random.randint(5, 6)  # Количество кубитов регистра от 5 до 6
  h_position = random.randint(0, num_qubits - 1)  # Позиция для гейта Адамара

  num_cnot_gates = random.randint(10, 12)  # Количество CNOT гейтов от 10 до 12
  cnot_positions = []
  for _ in range(num_cnot_gates):
    control = random.randint(0, num_qubits - 1)
    target = random.randint(0, num_qubits - 1)
    while target == control:
      target = random.randint(0, num_qubits - 1)
    cnot_positions.append(('cx', control, target))
  
  num_x_gates = random.randint(10, 12)  # Количество X гейтов от 10 до 12
  x_positions = [random.randint(0, num_qubits - 1) for _ in range(num_x_gates)]

  # Создаем список операций, объединяющий все X и CNOT гейты
  operations = [('x', pos) for pos in x_positions] + cnot_positions

  # Перемешиваем операции, чтобы получить случайный порядок
  random.shuffle(operations)

  return num_qubits, h_position, operations

# Создание и отображение схемы
def create_and_show_circuit(student_id, num_qubits, h_position, operations):
  q_reg = QuantumRegister(size=num_qubits, name='q')
  c_reg = ClassicalRegister(size=num_qubits, name='c')
  qc = QuantumCircuit(q_reg, c_reg)

  # Применяем гейт Hadamard
  qc.h(h_position)

  # Применяем гейты X и CNOT в случайном порядке
  for operation in operations:
    if operation[0] == 'x':
      qc.x(operation[1])
    elif operation[0] == 'cx':
      qc.cx(operation[1], operation[2])

  qc.barrier(q_reg)
  qc.measure(q_reg, c_reg)

  custom_circuit_image = custom_cnot_color(qc)
  plt.show()

  return qc

# Функция для кастомизации цвета CNOT-гейтов
def custom_cnot_color(circuit):
  style = {
    'name': 'custom',
    'displaycolor': {
      'cx': '#249147'  # Зеленый цвет для CNOT-гейтов
    }
  }
  return circuit.draw(output='mpl', style=style)

# Генерация задания для студента
student_id = int(input("Номер варианта: "))
num_qubits, h_position, operations = generate_assignment(student_id)
qc = create_and_show_circuit(student_id, num_qubits, h_position, operations)

# Используем симулятор для выполнения схемы
backend_local = GenericBackendV2(num_qubits = num_qubits)
simulation_result = backend_local.run(qc, shots=1000).result()
simulation_counts = simulation_result.get_counts()

# Получаем результаты измерений и визуализируем их
plot_histogram(simulation_counts, title='Конечное состояние регистра после симуляции', figsize=(8, 8))
plt.show()

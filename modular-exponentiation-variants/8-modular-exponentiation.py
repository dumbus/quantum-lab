import matplotlib.pyplot as plt

from qiskit import *
from qiskit.visualization import plot_histogram
from qiskit.providers.fake_provider import GenericBackendV2

SHOTS = 2000

REG_MAX = 3
REG_SIZE = REG_MAX + 1

q_reg_x = QuantumRegister(size=2, name='x')
q_reg_y = QuantumRegister(size=4, name='y')
c_reg = ClassicalRegister(size=4, name='c')
qc = QuantumCircuit(q_reg_x, q_reg_y, c_reg)

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
qc.draw(output="mpl")
plt.show()

# Используем симулятор для выполнения схемы
backend_local = GenericBackendV2(num_qubits = 6)
simulation_result = backend_local.run(qc, shots=SHOTS).result()
simulation_counts = simulation_result.get_counts()

# Получаем результаты измерений и визуализируем их
plot_histogram(simulation_counts, title='Конечное состояние регистра после симуляции', figsize=(8, 8))
plt.show()

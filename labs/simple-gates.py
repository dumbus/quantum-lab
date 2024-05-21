import sys
import locale
import matplotlib.pyplot as plt

from qiskit import *
from qiskit.visualization import plot_histogram
from qiskit.providers.fake_provider import GenericBackendV2

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
sys.stdout.reconfigure(encoding='utf-8')

SHOTS = 1000

y = int(input("Введите вычисленное число y: "))

binary_у = bin(y)[2:]
reg_size = len(binary_у)
positions = [i for i, bit in enumerate(reversed(binary_у)) if bit == '1']

q_reg = QuantumRegister(size=reg_size, name='Кубит ')
c_reg = ClassicalRegister(size=reg_size, name='Классический регистр')
qc = QuantumCircuit(q_reg, c_reg)

for pos in positions:
  qc.x(q_reg[pos])

qc.barrier(q_reg)
qc.measure(q_reg, c_reg)

# ========================= Draw circuit =========================
# qc.draw(output="mpl")
# plt.show()

# ======================= Local Simulation (Generic backend) =======================
backend_local = GenericBackendV2(num_qubits = reg_size * 2)
simulation_result = backend_local.run(qc, shots=SHOTS).result()
simulation_counts = simulation_result.get_counts()

plot_histogram(simulation_counts, title='Конечное состояние регистра после симуляции', figsize=(8, 7))
plt.show()

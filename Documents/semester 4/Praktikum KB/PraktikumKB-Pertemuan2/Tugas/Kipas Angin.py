import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt  

suhu = ctrl.Antecedent(np.arange(0, 41, 1), 'suhu')
kelembapan = ctrl.Antecedent(np.arange(0, 101, 1), 'kelembapan')
kipas = ctrl.Consequent(np.arange(0, 101, 1), 'kipas')

suhu['dingin'] = fuzz.trimf(suhu.universe, [0, 0, 20])
suhu['normal'] = fuzz.trimf(suhu.universe, [15, 25, 30])
suhu['panas'] = fuzz.trimf(suhu.universe, [25, 40, 40])

kelembapan['kering'] = fuzz.trimf(kelembapan.universe, [0, 0, 40])
kelembapan['normal'] = fuzz.trimf(kelembapan.universe, [30, 50, 70])
kelembapan['lembap'] = fuzz.trimf(kelembapan.universe, [60, 100, 100])

kipas['lambat'] = fuzz.trimf(kipas.universe, [0, 0, 40])
kipas['sedang'] = fuzz.trimf(kipas.universe, [30, 50, 70])
kipas['cepat'] = fuzz.trimf(kipas.universe, [60, 100, 100])

rule1 = ctrl.Rule(suhu['dingin'] & kelembapan['kering'], kipas['lambat'])
rule2 = ctrl.Rule(suhu['normal'] & kelembapan['normal'], kipas['sedang'])
rule3 = ctrl.Rule(suhu['panas'] & kelembapan['lembap'], kipas['cepat'])
rule4 = ctrl.Rule(suhu['panas'] & kelembapan['kering'], kipas['sedang'])
rule5 = ctrl.Rule(suhu['dingin'] & kelembapan['lembap'], kipas['sedang'])

kipas_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
simulasi = ctrl.ControlSystemSimulation(kipas_ctrl)

suhu_input = float(input("Masukkan suhu (0-40): "))
kelembapan_input = float(input("Masukkan kelembapan (0-100): "))

simulasi.input['suhu'] = suhu_input
simulasi.input['kelembapan'] = kelembapan_input

simulasi.compute()

hasil = simulasi.output['kipas']
print("\n=== HASIL ===")
print("Kecepatan Kipas:", hasil)

suhu.view()
kelembapan.view()
kipas.view(sim=simulasi)

plt.show()

input("Tekan Enter untuk keluar...")
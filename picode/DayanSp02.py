# Dayan's SPo2 Calculation File

#function interfaces below:
# def calculate_SPO2(IR, RED, lc_ir, hc_ir, lc_red, hc_red, fs=50, order=5, pk_min=1, pk_max=-1):
# def calc_hr_and_spo2(ir_data, red_data):

import PPG_algorithms as ppg
import hrcalc
import pandas as pd
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

ppgir = pd.read_csv(dir_path+"/ppgir_data.csv")
ppgred = pd.read_csv(dir_path+"/ppgred_data.csv")

#hrcalc

hr, hrvalid, spo2, spo2valid = hrcalc.calc_hr_and_spo2(ppgir[:500].values, ppgred[:500].values)

# ppgalgorithms
# spo2new = ppg.calculate_SPO2(
#     ppgir[:100], ppgred[:100], 20.00, 2.5, 20.00, 2.5, fs=100, order=1)
# print(ppgir)
# print(ppgred)
print(spo2)
print(spo2valid)
# print(spo2new)

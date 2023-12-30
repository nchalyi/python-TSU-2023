# Эта программа строит графики полного сечения рассеяния реакции в зависимости от энергии налетающей
# на мишень частицы. Сравниваются эксериментальные данные и данные некоторого моделирования.
# В качестве примера рассмотрено сечение реакции рождения альфа частицы при 
# налетании фотонов на мишень из меди толщиной 2см.

import matplotlib.pyplot as plt
from math import log

# Material information for calculations of crossection
# material = Copper
density=8.96 # g/cm^3 (material density)
u=1.66e-24 # (atomic mass unit)
At=29 # atomic mass mumber
x=2 # cm (target thickness)
evt=100000

# Cross section calculation functon
def Sigma(A):
    cross_cm=-((At*u)/(density*x))*log(1-A/evt) # crossection in cm^2
    cross_mb=cross_cm/(1e-27) # crossection in millibarns (mb)
    return cross_mb

# Import EXFOR (experimental) data:
expData=open("final_project/EXFOR-Cu.data","r")
expEn=[]
expS=[]
expErr=[]
for line in expData:
    reg=line.split()
    expEn.append(float(reg[0])) # photon energy
    expS.append(float(reg[1])) # crossection
    # expErr.append(float(reg[2])) # errors, if they're different
expData.close()

# Import modeling data and export output file with calculations
modelData=open("final_project/model-Cu.data","r")
outData=open("final_project/output-Cu.data","w")
modEn=[]
modCross=[]

for line in modelData:
    list=line.split()
    n=int(list[1]) # number of created alpha particles
    cross=Sigma(n)
    outData.write(f'{list[0]} \t {n} \t {round(cross,5)}\n') # write to file for other studies
    modEn.append(float(list[0])) # photon energy
    modCross.append(cross) # number of alphas

modelData.close()
outData.close()

# Plot using matplotlib.pyplot
plt.figure(figsize=(10, 5))
plt.plot(modEn, modCross, marker='.', linestyle='--', color = 'black', label='Model')
plt.plot(expEn, expS, marker='+', linestyle='-', color = 'blue', label='Experiment')
# plt.plot(expEn, expS, fmt='+', yerr=expErr, label='Experiment') # plotting with errorbars, if they're available

plt.title('Total cross section for reaction $Cu(\gamma,\\alpha )$')
plt.xlabel('$E_\gamma$, MeV')
plt.ylabel('$\sigma$, mb')
plt.grid(True)  
plt.legend()
plt.show()

# Данная модель нуждается в доработке, но для этой программы это значения не имеет.
# Моделирование проводилось на Geant4 (https://geant4.org/), поскольку работаю я в ТГУ именно в нём.
# Источник экспериментальных данных: https://www-nds.iaea.org/exfor/servlet/X4sGetSubent?reqx=38870&subID=220894002&plus=1
import numpy as np
from gpa import GPA
from gre import GRE 
from predikat import Predikat

status = ""
u_status = np.empty(9, dtype=object)
z_status = ["excellent", "good", "fair", "verygood", "good", "poor", "fair", "poor", "poor"]

def hitung_u(gpa, gre):
    u_status[0] = min(gpa.high(), gre.high())
    u_status[1] = min(gpa.medium(), gre.high())
    u_status[2] = min(gpa.low(), gre.high())
    u_status[3] = min(gpa.high(), gre.medium())
    u_status[4] = min(gpa.medium(), gre.medium())
    u_status[5] = min(gpa.low(), gre.medium())
    u_status[6] = min(gpa.high(), gre.low())
    u_status[7] = min(gpa.medium(), gre.low())
    u_status[8] = min(gpa.low(), gre.low())

def max_method_hitung_z():
    global status
    max_val = 0
    for i in range(len(u_status)):
        if max_val < u_status[i]:
            max_val = u_status[i]
            status = z_status[i]

    return max_val

#Centroid Method
def hitung_centroid_crisp():
  count = 0
  divider = 0

  global status
  for i in range(len(round_u_values)):
    if(round_u_values[i] > 0):
      divider += u_status[i]
      if(i == 0): count += (round_u_values[i] * 95)
      elif(i == 1): count += (round_u_values[i] * 90)
      elif(i == 3 or i == 4): count += (round_u_values[i] * 80)
      elif(i == 2 or i == 6) : count+= (round_u_values[i] * 70)
      else : count += (round_u_values[i] * 65)

  return count / divider



def hitung_value_centroid(predikat):
    value = 0
    decision = ""

    if value < predikat.excellent():
        value = predikat.excellent()
        decision = "excellent"
    if value < predikat.very_good():
        value = predikat.very_good()
        decision = "very good"
    if value < predikat.good():
        value = predikat.good()
        decision = "good"
    if value < predikat.fair():
        value = predikat.fair()
        decision = "fair"
    if value < predikat.poor():
        value = predikat.poor()
        decision = "poor"

    return decision



def bulatkan_nilai(nilai, precision):
    return round(nilai / precision) * precision

def round_u_status(u_status, precision):
    rounded_values = []
    for value in u_status:
        rounded_value = round(value / precision) * precision
        rounded_values.append(rounded_value)

    return rounded_values

input_gpa = float(input("Masukkan GPA: "))
input_gre = int(input("Masukkan GRE: "))
gpa = GPA(input_gpa)
gre = GRE(input_gre)

hitung_u(gpa, gre)

round_u_values = round_u_status(u_status, 0.25)

for index, value in enumerate(round_u_values):
    print(f"u_ke-{index}, Value: {value}")

max_val = bulatkan_nilai(max_method_hitung_z(), 0.25)
print("Max Method:")
print("Bobot:", max_val, "\ndengan predikat:", status)

bobot = max_method_hitung_z()
predikat = Predikat(value)
crisp_index = hitung_centroid_crisp()
predikat_centroid = Predikat(crisp_index)

print("\nCentroid Method:")
print("Crisp Decision Index:", crisp_index)
print("dengan predikat:", hitung_value_centroid(predikat_centroid))


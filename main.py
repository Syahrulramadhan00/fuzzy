import numpy as np
from gpa import GPA
from gre import GRE 
from predikat import Predikat

status = ""
u_status = np.empty(9, dtype=object)
z_status = ["Excellent", "Good", "Fair", "VeryGood", "Good", "Poor", "Fair", "Poor", "Poor"]

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

def centroid_method_hitung_z(round_u_status):
    predikat_centers = [65, 70, 80, 90, 95]

    if len(predikat_centers) != len(round_u_status):
        print("Error: Number of predikat_centers does not match number of round_u_status")
        return None

    numerator = 0
    denominator = 0

    for i, value in enumerate(round_u_status):
        center = predikat_centers[i]
        weight = value / 100  

        numerator += weight * center
        denominator += weight  

    if denominator == 0:
        return 0
    else:
        crisp_index = numerator / denominator
        return crisp_index

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

crisp_index = centroid_method_hitung_z(round_u_values)
print("\nCentroid Method:")
print("Crisp Decision Index:", crisp_index)

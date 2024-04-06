import numpy as np
import math
from gpa import GPA
from gre import GRE 
from predikat import Predikat

status = ""
u_status = np.empty(9, dtype=object)
z_status = ["Excellent","Good", "Fair","VeryGood","Good","Poor","Fair","Poor","Poor"]

def hitung_u():
    u_status[0] = min(gpa.high(),gre.high())
    u_status[1] = min(gpa.medium(),gre.high())
    u_status[2] = min(gpa.low(),gre.high())
    u_status[3] = min(gpa.high(),gre.medium())
    u_status[4] = min(gpa.medium(),gre.medium())
    u_status[5] = min(gpa.low(),gre.medium())
    u_status[6] = min(gpa.high(),gre.low())
    u_status[7] = min(gpa.medium(),gre.low())
    u_status[8] = min(gpa.low(),gre.low())

def max_method_hitung_z():
  global status
  max = 0
  for i in range(len(u_status)):
    if(max < u_status[i]):
      max = u_status[i]
      status = z_status[i]

  return max  


# def centroid_method_hitung_z():
#     global status

input_gpa = float(input("Masukkan GPA: "))
input_gre = int(input("Masukkan GRE: "))
gpa = GPA(input_gpa)
gre = GRE(input_gre)

hitung_u()

for index, value in enumerate(u_status):
    print(f"u_ke- {index}, Value: {value}")

bobot_max_method = max_method_hitung_z()

print("Max Method:\n" "Bobot: ",bobot_max_method, "\ndengan predikat: ",status) 
import random

print("---------------------------------")
print("----- LANZAMIENTO DE UN DADO ----")
print("---------------------------------")

# input

# processing
d = random(1,6)

if (d==1):
    rta =  "UNO"
elif (d==2):
    rta = "DOS"
elif (d==3):
    rta = "TRES"
elif (d==4):
    rta = "CUATRO"
elif (d==5):
    rta = "CINCO"
elif (d==6):
    rta = "SEIS"
else:
    rta = "No es la cara de un dado"

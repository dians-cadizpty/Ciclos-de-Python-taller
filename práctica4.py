suma=0
for i in range (3):
    nota=float(input("Ingrse su nota:"))
    suma+=nota

promedio = suma / 3
print("Tu promedio es:", promedio)
 
if promedio >= 3:
    print("Aprobaste")
else:
    print("Reprobaste")

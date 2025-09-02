n_pacientes = int(input("Ingrese el numero de pacientes: "))

hombres_alto = hombres_normal = hombres_bajo = 0
mujeres_alto = mujeres_normal = mujeres_bajo = 0

for i in range(n_pacientes):
    print(f"\nPaciente {i + 1}:")
    nivel_hemoglobina = float(input("Ingrese el nivel de su hemoglobina: "))
    genero = int(input("Ingrese su género (1 para masculino, 2 para femenino): "))

    if genero == 1:
        if nivel_hemoglobina < 12.2:
            hombres_bajo += 1
        elif nivel_hemoglobina >=12.2 and nivel_hemoglobina<=16.6:
            hombres_normal += 1
        else:
            hombres_alto += 1
    elif genero == 2:
        if nivel_hemoglobina < 12.6:
            mujeres_bajo += 1
        elif nivel_hemoglobina >=12.6 and nivel_hemoglobina<=15.0:
            mujeres_normal += 1
        else: 
            mujeres_alto += 1
    else:
        print("No es posible generar la alerta")

print(f"{hombres_bajo},{hombres_normal},{hombres_bajo},{mujeres_bajo},{mujeres_normal},{mujeres_bajo}")
print(f"Hombres: {hombres_bajo},{hombres_normal},{hombres_bajo}")
print(f"Mujeres: {mujeres_bajo},{mujeres_normal},{mujeres_bajo}")        
print(f"Hombres con hemoglobina baja: {hombres_bajo}")
print(f"Hombres con hemoglobina normal: {hombres_normal}")
print(f"Hombres con hemoglobina alta: {hombres_alto}")
print(f"Mujeres con hemoglobina baja: {mujeres_bajo}")
print(f"Mujeres con hemoglobina normal: {mujeres_normal}")
print(f"Mujeres con hemoglobina alta: {mujeres_alto}")
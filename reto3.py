n_pacientes = int(input("Ingrese el numero de pacientes: "))
hombre_alto = hombre_normal = hombre_bajo = 0
mujer_alto = mujer_normal = mujer_bajo = 0
suma_hombre = 0
suma_mujer = 0
promedio_hombre = 0
promedio_mujer = 0
for i in range(n_pacientes):
    print(f"\nPaciente {i + 1}:")
    nivel_hemoglobina = float(input("Ingrese el nivel de su hemoglobina: "))
    genero = int(input("Ingrese su género (1 para masculino, 2 para femenino): "))
    while genero != 1 and genero !=2:
        print("Genero no valido, intente de nuevo")
        genero = int(input("Ingrese su género (1 para masculino, 2 para femenino): "))
    if genero == 1:
        if nivel_hemoglobina < 12.2:
            hombre_bajo += 1
            diagnostico = "bajo"
        elif nivel_hemoglobina >= 12.2 and nivel_hemoglobina <= 16.6:
            hombre_normal += 1
            diagnostico = "normal"
        else:
            hombre_alto += 1
            diagnostico = "alto"
    else:
        if nivel_hemoglobina < 12.6:
            mujer_bajo += 1
            diagnostico = "bajo"
        elif nivel_hemoglobina >= 12.6 and nivel_hemoglobina <=15:
            mujer_normal += 1
            diagnostico = "normal"
        else:
            mujer_alto += 1
            diagnostico = "alto"
    if genero == 1:
        suma_hombre += nivel_hemoglobina
    else:
        suma_mujer += nivel_hemoglobina

promedio_hombre = round(suma_hombre / (hombre_alto + hombre_normal + hombre_bajo),2)
if promedio_hombre < 12.2:
    alerta = "bajo"
elif promedio_hombre >= 12.2 and promedio_hombre <= 16.6:
    alerta = "normal" 
else:
    alerta = "alto"
    
promedio_mujer = round(suma_mujer / (mujer_alto + mujer_normal + mujer_bajo),2)
if promedio_mujer < 12.6:
    alerta = "bajo"
elif promedio_mujer >= 12.6 and promedio_mujer <= 15:
    alerta = "normal"
else:
    alerta = "alto"
print(f"Promedio de hemoglobina en hombres: {promedio_hombre}, {alerta}")
print(f"Promedio de hemoglobina en mujeres: {promedio_mujer}, {alerta}")
print(f"Nivel de hemoglobina alta: {hombre_alto}, {mujer_alto}")
print(f"Nivel de hemoglobina bajo: {hombre_bajo}, {mujer_bajo}")
print(f"Nivel de hemoglobina normal: {hombre_normal}, {mujer_normal}")
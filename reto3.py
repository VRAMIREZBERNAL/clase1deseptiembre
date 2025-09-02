n_pacientes = int(input("Ingrese el numero de pacientes: "))
hombre_alto = hombre_normal = hombre_bajo = 0
mujer_alto = mujer_normal = mujer_bajo = 0
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
    print(f"{nivel_hemoglobina}, {diagnostico}")
    
print(f"Nivel de hemoglobina alta: {hombre_alto}, {mujer_alto}")
print(f"Nivel de hemoglobina bajo: {hombre_bajo}, {mujer_bajo}")
print(f"Nivel de hemoglobina normal: {hombre_normal}, {mujer_normal}")
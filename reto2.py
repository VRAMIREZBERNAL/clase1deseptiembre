n_pacientes = int(input("Ingrese el numero de pacientes: "))
nivel_hemoglobina = float(input("Ingrese el nivel de su hemoglobina: "))
genero = int(input("Ingrese su género (1 para masculino, 2 para femenino): "))
datos_pacientes = [2, n_pacientes]
for i in range(n_pacientes):
    if genero == 1:
        if nivel_hemoglobina < 12.2:
            print("Su nivel de hemoglobina es bajo.")
        if 12.2 <= nivel_hemoglobina <= 16.6:
            print("Su nivel de hemoglobina es normal.")
        if nivel_hemoglobina > 16.6:
            print("Su nivel de hemoglobina es alto.")
    elif genero == 2:
        if nivel_hemoglobina < 12.6:
            print("Su nivel de hemoglobina es bajo.")
        if 12.6 <= nivel_hemoglobina <= 15.0:
            print("Su nivel de hemoglobina es normal.")
        if nivel_hemoglobina > 15.0: 
            print("Su nivel de hemoglobina es alto.")
    else:
        print("No es posible generar la alerta")
    
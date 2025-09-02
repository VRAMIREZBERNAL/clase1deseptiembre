nivel_hemoglobina = float(input("Ingrese el nivel de su hemoglobina: "))
genero = int(input("Ingrese su género (1 para masculino, 2 para femenino): "))
if genero == 1:
    if nivel_hemoglobina < 12.2:
        print("Su nivel de hemoglobina es bajo.")
    if nivel_hemoglobina >=12.2 and nivel_hemoglobina<=16.6:
        print("Su nivel de hemoglobina es normal.")
    if nivel_hemoglobina > 16.6:
        print("Su nivel de hemoglobina es alto.")
elif genero == 2:
    if nivel_hemoglobina < 12.6:
        print("Su nivel de hemoglobina es bajo.")
    if nivel_hemoglobina >=12.6 and nivel_hemoglobina<=15.0:
        print("Su nivel de hemoglobina es normal.")
    if nivel_hemoglobina > 15.0: 
        print("Su nivel de hemoglobina es alto.")
else:
    print("No es posible generar la alerta")

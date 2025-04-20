try:
    puerto = int(input("Ingrese un número de puerto: "))

    if 0 <= puerto <= 1023:
        print("Puerto bien conocido (0 – 1023).")
    elif 1024 <= puerto <= 49151:
        print("Puerto registrado (1024 – 49151).")
    elif 49152 <= puerto <= 65535:
        print("Puerto dinámico o privado (49152 – 65535).")
    else:
        print("El número ingresado no corresponde a un puerto válido.")
except ValueError:
    print("Por favor, ingrese un número válido.")

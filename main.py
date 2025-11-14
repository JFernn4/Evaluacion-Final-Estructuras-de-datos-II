import os
def menu():
    mensaje = ""
    while True:
        limpiar()
        print("ENVÍO Y VERIFICACIÓN DE MENSAJES\n")
        print("\nSecuencia sugerida: seguir los pasos en orden. (del 1 al 8)\n")
        print("[1] Ingresar mensaje")
        print("[2] Calcular hash FNV-1")
        print("[3] Comprmimir mensaje")
        print("[4] Firmar hash") #firmar con la clave privada RSA
        print("[5] Simular envio")
        print("[6] Descomprimir y verificar firma") #clave publica
        print("[7] Verificar mensaje")
        print("[8] Salir")

        opcion = input("Ingrese una opcion (1-8): ")

        if opcion == "1":
            limpiar()
            print(f"Mensaje actual: {mensaje}\n")
            mensaje = input("Ingrese un mensaje: ")
            input("\nPresione 'Enter' para continuar.")
        elif opcion == "2":
            limpiar()
            print(f"Mensaje actual: {mensaje}\n")
            input("\nPresione 'Enter' para continuar.")
        elif opcion == "3":
            limpiar()
            print(f"Mensaje actual: {mensaje}\n")
            input("\nPresione 'Enter' para continuar.")
        elif opcion == "4":
            limpiar()
            print(f"Mensaje actual: {mensaje}\n")
            input("\nPresione 'Enter' para continuar.")
        elif opcion == "5":
            limpiar()
            print(f"Mensaje actual: {mensaje}\n")
            input("\nPresione 'Enter' para continuar.")
        elif opcion == "6":
            limpiar()
            print(f"Mensaje actual: {mensaje}\n")
            input("\nPresione'Enter' para continuar.")
        elif opcion == "7":
            limpiar()
            print(f"Mensaje actual: {mensaje}\n")
            input("\nPresione 'Enter' para continuar.")
        elif opcion == "8":
            limpiar()
            print(f"Saliendo...")
            break          
        else: 
            print("\n Ingrese una opcion valida.\n")
    
def limpiar():
    os.system('cls')

menu()
import os
import heapq
import rsa

def fnv1_hash(text):
    FNV_prime = 16777619
    offset_basis = 2166136261

    hash_value = offset_basis
    for char in text.encode("utf-8"):
        hash_value *= FNV_prime
        hash_value ^= char
        hash_value &= 0xffffffff  # Mantener 32 bits

    return hash_value

def comprimir_rle(text):
    if not text:
        return ""

    resultado = []
    conteo = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            conteo += 1
        else:
            resultado.append(text[i - 1] + str(conteo))
            conteo = 1

    resultado.append(text[-1] + str(conteo))
    return "".join(resultado)

def generar_claves():
        public_key, private_key = rsa.newkeys(512)

        with open("clave_publica.pem", "wb") as f:
            f.write(public_key.save_pkcs1("PEM"))
        with open("clave_privada.pem", "wb") as f:
            f.write(private_key.save_pkcs1("PEM"))
        return public_key, private_key

def firmar_mensaje(mensaje):

    with open("archivo_mensaje.bin","wb") as f:
        f.write(mensaje)
    with open("clave_privada.pem", "rb") as f:
        private_key = rsa.PrivateKey.load_pkcs1(f.read())

    with open("archivo_mensaje", "rb") as f:
        mensaje_ = f.read()

    firma = rsa.sign(mensaje_, private_key, "SHA-256")

    with open("firma.bin", "wb") as f:
                f.write(firma)


def menu():
    mensaje = ""
    hash =""
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
            print("\nHASH FNV-1")
            print(f"\nHash generado: {fnv1_hash(mensaje)}")
            hash = fnv1_hash(mensaje)
            input("\nPresione 'Enter' para continuar.")
        elif opcion == "3":
            limpiar()
            print(f"Mensaje actual: {mensaje}\n")
            print("\nCOMPRESIÓN RLE\n")
            rle_comprimido = comprimir_rle(mensaje)

            print("Tamaño original:", len(mensaje), "caracteres")
            print("Tamaño comprimido:", len(rle_comprimido), "caracteres")
            input("\nPresione 'Enter' para continuar.")
        elif opcion == "4":
            limpiar()
            print(f"Mensaje actual: {mensaje}\n")
            print(f"Hash actual: {hash}")
            print("\nFIRMAR HASH CON CLAVE PRIVADA\n")
            clave_publica, clave_privada = generar_claves()
            print(f"Clave publica: {clave_publica}")
            print(f"Clave privada{clave_privada}")
            firmar_mensaje(mensaje)

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
import random
import time
import os
from colorama import init, Fore, Style

def generar_numero(digitos):
    return ''.join(str(random.randint(0, 9)) for _ in range(digitos))

def generar_fecha_expiracion():
    mes = random.randint(1, 12)
    año = random.randint(25, 27)
    return "{:02d}-{:02d}".format(mes, año)

def generar_cvv():
    return str(random.randint(100, 999))

def solicitar_contraseña():
    # Solicitar la contraseña al usuario
    contraseña = input(Fore.YELLOW + "Por favor, ingrese la contraseña para acceder al generador de tarjetas: ")
    print(Style.RESET_ALL)
    return contraseña

def verificar_contraseña(contraseña):
    # Verificar si la contraseña es correcta
    return contraseña == "032008"

def personalizar_terminal():
    # Limpiar la terminal
    os.system('clear' if os.name == 'posix' else 'cls')

    # Inicializar colorama para habilitar el soporte de colores ANSI en la terminal
    init()

    # Solicitar la contraseña
    while True:
        contraseña_ingresada = solicitar_contraseña()
        if verificar_contraseña(contraseña_ingresada):
            break
        else:
            print(Fore.RED + "Contraseña incorrecta. Por favor, inténtelo de nuevo.")
            print(Style.RESET_ALL)

    # Animación de bienvenida
    print(Fore.GREEN + "=== Generador de Tarjetas ===")
    print(Style.RESET_ALL)
    print(Fore.YELLOW + "Bienvenido al mundo de los generadores de tarjetas!")
    print(Style.RESET_ALL)
    print(Fore.YELLOW + "Por favor, ingrese su nombre a continuación:")
    print(Style.RESET_ALL)

def saludo(nombre):
    print(Fore.GREEN + "Felicidades por unirte a este mundo de generadores de tarjetas, " + nombre + "!")
    print(Style.RESET_ALL)

def generar_tarjeta():
    personalizar_terminal()

    usuario = input(Fore.CYAN + "Nombre: " + Style.RESET_ALL)

    if usuario.lower() == 'incognito':
        nombre = "Incógnito"
    else:
        nombre = usuario

    saludo(nombre)

    seis_digitos = input(Fore.CYAN + "BIN: ")
    print(Style.RESET_ALL)
    while len(seis_digitos) != 6 or not seis_digitos.isdigit():
        seis_digitos = input(Fore.RED + "Por favor, ingrese exactamente 6 dígitos: ")
        print(Style.RESET_ALL)

    mes = input(Fore.CYAN + "Mes de expiración: ")
    print(Style.RESET_ALL)
    año = input(Fore.CYAN + "Año de expiración: ")
    print(Style.RESET_ALL)
    cvv = input(Fore.CYAN + "CVV: ")
    print(Style.RESET_ALL)

    cantidad = int(input(Fore.CYAN + "¿Cuántas tarjetas desea generar? "))
    print(Style.RESET_ALL)
    print("\nGenerando {} tarjetas:".format(cantidad))

    # Animación de carga mejorada
    animaciones_carga = ["⣾⣽⣻⢿⡿⣟⣯⣷", "▉▊▋▌▍▎▏▎▍▌▋▊▉", "■□□□□□□□□□", "◢◣◤◥", "▁▂▃▄▅▆▇█▇▆▅▄▃▁"]
    for _ in range(15):
        for animacion in animaciones_carga:
            print('\r' + Fore.YELLOW + "Generando tarjetas " + animacion, end='', flush=True)
            time.sleep(0.05)

    print('\r' + Fore.GREEN + "¡Tarjetas generadas con éxito!" + Style.RESET_ALL)

    for _ in range(cantidad):
        if not mes:
            fecha_expiracion = generar_fecha_expiracion()
        else:
            fecha_expiracion = "{:02d}-{}".format(int(mes), random.randint(25, 27))

        if not cvv:
            cvv_generado = generar_cvv()
        else:
            cvv_generado = cvv

        numero_completo = seis_digitos + generar_numero(10)
        print("\n" + "-"*40)
        print("Número de tarjeta:", numero_completo)
        print("Fecha de expiración:", fecha_expiracion)
        print("CVV:", cvv_generado)
        print("-"*40)

if __name__ == "__main__":
    generar_tarjeta()
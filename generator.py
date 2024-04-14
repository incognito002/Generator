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
    # Animación de carga para la solicitud de contraseña
    print(Fore.GREEN + "Iniciando..." + Style.RESET_ALL)
    for _ in range(20):
        print('\r' + Fore.GREEN + "Iniciando " + "." * (_ % 4), end='', flush=True)
        time.sleep(0.1)

    # Limpiar la terminal
    os.system('clear' if os.name == 'posix' else 'cls')

    # Solicitar la contraseña al usuario en un cuadro con colores
    print(Fore.BLUE + "+" + "-" * 38 + "+")
    print("|" + Fore.YELLOW + "           Ingrese la contraseña          " + Fore.BLUE + "|")
    print("+" + "-" * 38 + "+" + Style.RESET_ALL)
    contraseña = input(Fore.CYAN + "Contraseña: ")
    print(Style.RESET_ALL)
    return contraseña

def verificar_contraseña(contraseña):
    # Verificar si la contraseña es correcta
    return contraseña == "032008"

def limpiar_terminal():
    # Limpiar la terminal
    os.system('clear' if os.name == 'posix' else 'cls')

def personalizar_terminal():
    # Limpiar la terminal
    os.system('clear' if os.name == 'posix' else 'cls')

    # Resto del código...
    while True:
        contraseña_ingresada = solicitar_contraseña()
        if verificar_contraseña(contraseña_ingresada):
            break
        else:
            print(Fore.RED + "Contraseña incorrecta. Por favor, inténtelo de nuevo.")
            print(Style.RESET_ALL)

    # Limpiar la terminal después de ingresar la contraseña correcta
    os.system('clear' if os.name == 'posix' else 'cls')
    print(Fore.BLUE + "+" + "-" * 38 + "+")
    print("|" + Fore.CYAN + "         Generator-CS         " + Fore.BLUE + "|")
    print("+" + "-" * 38 + "+" + Style.RESET_ALL)
    print()

    # Animación de bienvenida con borde de colores
    mensaje_bienvenida = [
        "=== Generador de Tarjetas ===",
        "Bienvenido al mundo de los generadores de tarjetas!",
        "Por favor, ingrese su nombre a continuación:"
    ]
    color_borde = Fore.CYAN
    color_texto = Fore.YELLOW
    longitud_maxima = max(len(linea) for linea in mensaje_bienvenida)
    print(color_borde + "+" + "-" * (longitud_maxima + 2) + "+" + Style.RESET_ALL)
    for linea in mensaje_bienvenida:
        print(color_borde + "| " + color_texto + linea.ljust(longitud_maxima) + " " * (longitud_maxima - len(linea)) + " " + color_borde + "|" + Style.RESET_ALL)
    print(color_borde + "+" + "-" * (longitud_maxima + 2) + "+" + Style.RESET_ALL)

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

    cantidad = int(input(Fore.CYAN + "Número de tarjetas a generar: "))
    print(Style.RESET_ALL)
    print("\nGenerando {} tarjetas:".format(cantidad))

    # Animación de carga mejorada
    animaciones_carga = ["⣾⣽⣻⢿⡿⣟⣯⣷", "▉▊▋▌▍▎▏▎▍▌▋▊▉", "■□□□□□□□□□", "◢◣◤◥", "▁▂▃▄▅▆▇█▇▆▅▄▃▁"]
    for _ in range(15):
        for animacion in animaciones_carga:
            print('\r' + Fore.YELLOW + "Generando tarjetas " + animacion, end='', flush=True)
            time.sleep(0.05)

    tarjetas = []
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
        tarjetas.append((numero_completo, fecha_expiracion, cvv_generado))

    # Limpiar la terminal después de generar las tarjetas
    limpiar_terminal()

    # Mostrar el mensaje simplificado de éxito
    print(Fore.GREEN + "Las tarjetas se han generado con éxito." + Style.RESET_ALL)

    # Mostrar las tarjetas generadas
    for tarjeta in tarjetas:
        print("\n" + "="*40)
        print(Fore.CYAN + "Número de tarjeta:", tarjeta[0])
        print("Fecha de expiración:", tarjeta[1])
        print("CVV:", tarjeta[2])
        print("="*40)

    # Ofrecer opciones al usuario
    while True:
        opcion = input("\n¿Qué desea hacer?\n1- Volver al inicio\n2- Salir\nOpción: ")
        if opcion == '1':
            generar_tarjeta()
        elif opcion == '2':
            print("¡Hasta luego!")
            break
        else:
            print(Fore.RED + "Opción no válida. Por favor, elija una opción válida." + Style.RESET_ALL)

if __name__ == "__main__":
    generar_tarjeta()
          

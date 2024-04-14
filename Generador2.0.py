import random
import time
import os
import datetime
from colorama import init, Fore, Style
from faker import Faker

def solicitar_credenciales(intentos):
    for intento in range(intentos):
        # Solicitar las credenciales al usuario
        print(Fore.BLUE + "+" + "-" * 38 + "+")
        print("|" + Fore.MAGENTA + "       🌟 Bienvenido a GENERATOR-CS 🌟       " + Fore.BLUE + "|")
        print("+" + "-" * 38 + "+" + Style.RESET_ALL)
        usuario = input(Fore.CYAN + "Usuario: " + Style.RESET_ALL)
        contraseña = input(Fore.CYAN + "Contraseña: " + Style.RESET_ALL)
        if verificar_credenciales(usuario, contraseña):
            return usuario
        else:
            print(Fore.RED + "Credenciales incorrectas. Intento {} de {}".format(intento + 1, intentos) + Style.RESET_ALL)
    return None

def verificar_credenciales(usuario, contraseña):
    # Verificar si las credenciales son correctas
    return usuario == "ck400" and contraseña == "032008"

def limpiar_terminal():
    # Limpiar la terminal
    os.system('clear' if os.name == 'posix' else 'cls')

def personalizar_terminal():
    # Mostrar el nombre de la herramienta en un cuadro grande
    print(Fore.BLUE + "+" + "-" * 50 + "+")
    print("|" + Fore.MAGENTA + "             🌟 GENERATOR-CS 🌟             " + Fore.BLUE + "|")
    print("+" + "-" * 50 + "+" + Style.RESET_ALL)
    print()

    # Animación de bienvenida con borde de colores
    mensaje_bienvenida = [
        "=== Generador de Tarjetas ===",
        "Bienvenido al mundo de los generadores de tarjetas!",
        "Para que los valores aparezcan en aleatorio simplemente presione enter",
        "Por favor, ingrese sus credenciales a continuación:"
    ]
    color_borde = Fore.BLUE
    color_texto = Fore.MAGENTA
    longitud_maxima = max(len(linea) for linea in mensaje_bienvenida)
    print(color_borde + "+" + "-" * (longitud_maxima + 2) + "+" + Style.RESET_ALL)
    for linea in mensaje_bienvenida:
        print(color_borde + "| " + color_texto + linea.ljust(longitud_maxima) + " " * (longitud_maxima - len(linea)) + " " + color_borde + "|" + Style.RESET_ALL)
    print(color_borde + "+" + "-" * (longitud_maxima + 2) + "+" + Style.RESET_ALL)

def saludo(nombre):
    print(Fore.GREEN + "Felicidades por unirte a este mundo de generadores de tarjetas, " + Fore.YELLOW + nombre + Fore.GREEN + "!" + Style.RESET_ALL)

def generar_tarjeta():
    # Solicitar las credenciales con 5 intentos
    usuario = solicitar_credenciales(5)
    if usuario is None:
        print(Fore.RED + "Has excedido el número máximo de intentos. ¡Adiós!")
        return

    # Limpiar la terminal después de ingresar las credenciales correctas
    limpiar_terminal()

    # Personalizar la terminal
    personalizar_terminal()

    # Generar nombre aleatorio
    fake = Faker()
    nombre = fake.name()

    saludo(nombre)

    # Solicitar el BIN
    seis_digitos = input(Fore.MAGENTA + "BIN: ")
    print(Style.RESET_ALL)
    while len(seis_digitos) != 6 or not seis_digitos.isdigit():
        seis_digitos = input(Fore.RED + "Por favor, ingrese exactamente 6 dígitos: ")
        print(Style.RESET_ALL)

    # Solicitar el mes de expiración
    mes = input(Fore.MAGENTA + "Mes de expiración (MM): ")
    print(Style.RESET_ALL)

    # Solicitar el año de expiración
    año = input(Fore.MAGENTA + "Año de expiración (YY): ")
    print(Style.RESET_ALL)

    # Generar CVV aleatorio
    cvv = str(random.randint(0, 999)).zfill(3)

    # Solicitar cantidad de tarjetas a generar
    cantidad = int(input(Fore.MAGENTA + "Número de tarjetas a generar: "))
    print(Style.RESET_ALL)
    print("\nGenerando tarjetas:")
    animacion_barras(5)

    # Generar tarjetas
    tarjetas = []
    for _ in range(cantidad):
        tarjeta = gen_card(seis_digitos, mes, año, cvv)
        tarjetas.append(tarjeta)

    # Limpiar la terminal después de generar las tarjetas
    limpiar_terminal()

    # Mostrar el mensaje de éxito y las tarjetas generadas
    print(Fore.GREEN + "Las tarjetas se han generado con éxito." + Style.RESET_ALL)
    for tarjeta in tarjetas:
        print("\n" + "=" * 40)
        print(Fore.MAGENTA + "Nombre:", nombre)
        print("Número de tarjeta:", tarjeta.split('|')[0])
        print("Fecha de expiración:", tarjeta.split('|')[1], "/", tarjeta.split('|')[2])
        print("CVV:", tarjeta.split('|')[3])
        print("Tipo de tarjeta:", tarjeta.split('|')[4])
        print("=" * 40)

def animacion_barras(iteraciones):
    for _ in range(iteraciones):
        time.sleep(0.2)
        print(Fore.MAGENTA + "=" * 40, end="\r")
        time.sleep(0.2)
        print(Fore.MAGENTA + "-" * 40, end="\r")
        time.sleep(0.2)
    print(Style.RESET_ALL)

def gen_card(bin, exp_m, exp_y, cvv):
    # Generar una tarjeta
    card_number = bin
    for _ in range(15 - len(bin)):
        digit = random.randint(0, 9)
        card_number += str(digit)
    digits = [int(x) for x in card_number]
    for i in range(0, 16, 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    total = sum(digits)
    check_digit = (10 - (total % 10)) % 10
    card_number += str(check_digit)

    if exp_m == "":
        exp_m = str(random.randint(1, 12)).zfill(2)
    else:
        exp_m = exp_m.zfill(2)

    if exp_y == "":
        current_year = datetime.datetime.now().year
        random_offset = random.randint(1, 5)
        exp_y = current_year + random_offset
    elif int(exp_y) >= 10 and int(exp_y) <= 99:
        exp_y = "20" + exp_y

    if cvv == "":
        cvv = str(random.randint(0, 999)).zfill(3)
    else:
        cvv = cvv.zfill(3)

    # Generar tarjeta Visa, Mastercard, American Express u otro tipo de manera aleatoria
    card_type = random.choice(["Visa", "Mastercard", "American Express", "Otro"])
    return f"{card_number}|{exp_m}|{exp_y}|{cvv}|{card_type}"

if __name__ == "__main__":
    generar_tarjeta()

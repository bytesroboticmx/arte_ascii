#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
 Programa: matematicas_discretas.py
 Descripción: Muestra el texto "Matemáticas Discretas" en Arte ASCII con
              múltiples estilos tipográficos, colores ANSI y decoraciones
              temáticas de matemáticas discretas.
 Requisitos: Python 3.6+ (No requiere librerías externas / Dependencias cero)
 Uso:
     python3 matematicas_discretas.py
     python3 matematicas_discretas.py --estilo bloques --color arcoiris
     python3 matematicas_discretas.py --estilo todos
=============================================================================
"""

import sys
import os
import argparse

# ---------------------------------------------------------------------------
# Definición de Banners en Arte ASCII
# ---------------------------------------------------------------------------

# Estilo 1: Estándar (FIGlet Standard, optimizado para terminales estándar de 80 columnas)
BANNER_ESTANDAR = (
    r"""
 __  __    _  _____ _____ __  __    _  _____ ___ ____    _    ____  
|  \/  |  / \|_   _| ____|  \/  |  / \|_   _|_ _/ ___|  / \  / ___| 
| |\/| | / _ \ | | |  _| | |\/| | / _ \ | |  | | |     / _ \ \___ \ 
| |  | |/ ___ \| | | |___| |  | |/ ___ \| |  | | |___ / ___ \ ___) |
|_|  |_/_/   \_\_| |_____|_|  |_/_/   \_\_| |___\____/_/   \_\____/ 

       ____   ___  ____   ____ ____  _____ _____  _    ____  
      |  _ \ |_ _|/ ___| / ___|  _ \| ____|_   _|/ \  / ___| 
      | | | | | | \___ \| |   | |_) |  _|   | | / _ \ \___ \ 
      | |_| | | |  ___) | |___|  _ <| |___  | |/ ___ \ ___) |
      |____/ |___||____/ \____|_| \_\_____| |_/_/   \_\____/ 
"""
).strip("\n")

# Estilo 2: Bloques / 3D Shadow (Caracteres Unicode de bloque, gran impacto visual)
BANNER_BLOQUES = (
    r"""
███╗   ███╗  █████╗  ████████╗ ███████╗ ███╗   ███╗  █████╗  ████████╗ ██╗  ██████╗   █████╗  ███████╗
████╗ ████║ ██╔══██╗ ╚══██╔══╝ ██╔════╝ ████╗ ████║ ██╔══██╗ ╚══██╔══╝ ██║ ██╔════╝  ██╔══██╗ ██╔════╝
██╔████╔██║ ███████║    ██║    █████╗   ██╔████╔██║ ███████║    ██║    ██║ ██║       ███████║ ███████╗
██║╚██╔╝██║ ██╔══██║    ██║    ██╔══╝   ██║╚██╔╝██║ ██╔══██║    ██║    ██║ ██║       ██╔══██║ ╚════██║
██║ ╚═╝ ██║ ██║  ██║    ██║    ███████╗ ██║ ╚═╝ ██║ ██║  ██║    ██║    ██║ ╚██████╗  ██║  ██║ ███████║
╚═╝     ╚═╝ ╚═╝  ╚═╝    ╚═╝    ╚══════╝ ╚═╝     ╚═╝ ╚═╝  ╚═╝    ╚═╝    ╚═╝  ╚═════╝  ╚═╝  ╚═╝ ╚══════╝

             ██████╗  ██╗ ███████╗  ██████╗  ██████╗  ███████╗ ████████╗  █████╗  ███████╗
             ██╔══██╗ ██║ ██╔════╝ ██╔════╝  ██╔══██╗ ██╔════╝ ╚══██╔══╝ ██╔══██╗ ██╔════╝
             ██║  ██║ ██║ ███████╗ ██║       ██████╔╝ █████╗      ██║    ███████║ ███████╗
             ██║  ██║ ██║ ╚════██║ ██║       ██╔══██╗ ██╔══╝      ██║    ██╔══██║ ╚════██║
             ██████╔╝ ██║ ███████║ ╚██████╗  ██║  ██║ ███████╗    ██║    ██║  ██║ ███████║
             ╚═════╝  ╚═╝ ╚══════╝  ╚═════╝  ╚═╝  ╚═╝ ╚══════╝    ╚═╝    ╚═╝  ╚═╝ ╚══════╝
"""
).strip("\n")

# Estilo 3: Inclinado (Slant, tipografía cursiva moderna)
BANNER_INCLINADO = (
    r"""
    __  ___    ___     ______    ______    __  ___    ___     ______    ____   ______    ___      _____
   /  |/  /   /   |   /_  __/   / ____/   /  |/  /   /   |   /_  __/   /  _/  / ____/   /   |    / ___/
  / /|_/ /   / /| |    / /     / __/     / /|_/ /   / /| |    / /      / /   / /       / /| |    \__ \ 
 / /  / /   / ___ |   / /     / /___    / /  / /   / ___ |   / /     _/ /   / /___    / ___ |   ___/ / 
/_/  /_/   /_/  |_|  /_/     /_____/   /_/  /_/   /_/  |_|  /_/     /___/   \____/   /_/  |_|  /____/  

                 ____     ____   _____   ______    ____     ______  ______    ___      _____
                / __ \   /  _/  / ___/  / ____/   / __ \   / ____/ /_  __/   /   |    / ___/
               / / / /   / /    \__ \  / /       / /_/ /  / __/     / /     / /| |    \__ \ 
              / /_/ /  _/ /    ___/ / / /___    / _, _/  / /___    / /     / ___ |   ___/ / 
             /_____/  /___/   /____/  \____/   /_/ |_|  /_____/   /_/     /_/  |_|  /____/  
"""
).strip("\n")

# Estilo 4: Simple / Compacto (Ideal para scripts y logs pequeños)
BANNER_SIMPLE = (
    r"""
  __  __    _  _____ _____ __  __    _  _____ ___ ____    _    ____  
 |  \/  |  / \|_   _| ____|  \/  |  / \|_   _|_ _/ ___|  / \  / ___| 
 | |\/| | / _ \ | | |  _| | |\/| | / _ \ | |  | | |     / _ \ \___ \ 
 | |  | |/ ___ \| | | |___| |  | |/ ___ \| |  | | |___ / ___ \ ___) |
 |_|  |_/_/   \_\_| |_____|_|  |_/_/   \_\_| |___\____/_/   \_\____/ 
  ____  ___ ____   ____ ____  _____ _____  _    ____  
 |  _ \_ _/ ___| / ___|  _ \| ____|_   _|/ \  / ___| 
 | | | | |\___ \| |   | |_) |  _|   | | / _ \ \___ \ 
 | |_| | | ___) | |___|  _ <| |___  | |/ ___ \ ___) |
 |____/___|____/ \____|_| \_\_____| |_/_/   \_\____/ 
"""
).strip("\n")

ESTILOS_DISPONIBLES = {
    "estandar": BANNER_ESTANDAR,
    "bloques": BANNER_BLOQUES,
    "inclinado": BANNER_INCLINADO,
    "simple": BANNER_SIMPLE
}

# ---------------------------------------------------------------------------
# Configuración de Colores y Formatos ANSI
# ---------------------------------------------------------------------------

COLORES_ANSI = {
    "cian": "\033[96m",
    "azul": "\033[94m",
    "verde": "\033[92m",
    "magenta": "\033[95m",
    "amarillo": "\033[93m",
    "rojo": "\033[91m",
    "blanco": "\033[97m",
    "reset": "\033[0m",
    "negrita": "\033[1m",
    "tenue": "\033[90m"
}

PALETA_ARCOIRIS = [
    "\033[91m",  # Rojo
    "\033[93m",  # Amarillo
    "\033[92m",  # Verde
    "\033[96m",  # Cian
    "\033[94m",  # Azul
    "\033[95m"   # Magenta
]

SIMBOLO_DISCRETO = "∀x ∈ U  •  ∃y P(x, y)  •  A ∩ B ⊆ A ∪ B  •  G = (V, E)  •  p ⟹ q"

def soporta_colores() -> bool:
    """Verifica si la terminal actual admite secuencias de escape ANSI."""
    if "NO_COLOR" in os.environ:
        return False
    return hasattr(sys.stdout, "isatty") and sys.stdout.isatty()

# ---------------------------------------------------------------------------
# Funciones de Renderizado
# ---------------------------------------------------------------------------

def generar_banner(estilo="estandar", decoracion=True, usar_color=True, color="cian") -> str:
    """
    Genera el texto de 'Matemáticas Discretas' formateado con el estilo y color elegidos.
    
    :param estilo: 'estandar', 'bloques', 'inclinado' o 'simple'
    :param decoracion: True para incluir marco y fórmulas matemáticas
    :param usar_color: True para colorear la salida con ANSI
    :param color: Nombre del color o 'arcoiris'
    :return: Cadena con el arte ASCII listo para imprimir
    """
    if estilo not in ESTILOS_DISPONIBLES:
        raise ValueError(f"Estilo desconocido '{estilo}'. Disponibles: {list(ESTILOS_DISPONIBLES.keys())}")

    texto_base = ESTILOS_DISPONIBLES[estilo]
    lineas = texto_base.split("\n")
    ancho_contenido = max(len(l) for l in lineas)

    # Preparación de colores
    c_reset = COLORES_ANSI["reset"] if usar_color else ""
    c_marco = COLORES_ANSI["tenue"] if usar_color else ""
    c_simb = COLORES_ANSI["amarillo"] if usar_color else ""

    def obtener_color_linea(idx: int, total: int) -> str:
        if not usar_color or color == "ninguno":
            return ""
        if color == "arcoiris":
            return PALETA_ARCOIRIS[idx % len(PALETA_ARCOIRIS)]
        return COLORES_ANSI.get(color, COLORES_ANSI["cian"])

    salida = []

    if decoracion:
        ancho_marco = max(ancho_contenido, len(SIMBOLO_DISCRETO))
        borde_superior = f"{c_marco}┌─{'─' * ancho_marco}─┐{c_reset}"
        borde_divisor  = f"{c_marco}├─{'─' * ancho_marco}─┤{c_reset}"
        borde_inferior = f"{c_marco}└─{'─' * ancho_marco}─┘{c_reset}"

        salida.append(borde_superior)

        for i, linea in enumerate(lineas):
            color_l = obtener_color_linea(i, len(lineas))
            linea_pad = linea.ljust(ancho_marco)
            salida.append(f"{c_marco}│{c_reset} {color_l}{linea_pad}{c_reset} {c_marco}│{c_reset}")

        salida.append(borde_divisor)
        subtitulo_pad = SIMBOLO_DISCRETO.center(ancho_marco)
        salida.append(f"{c_marco}│{c_reset} {c_simb}{subtitulo_pad}{c_reset} {c_marco}│{c_reset}")
        salida.append(borde_inferior)
    else:
        for i, linea in enumerate(lineas):
            color_l = obtener_color_linea(i, len(lineas))
            salida.append(f"{color_l}{linea}{c_reset}")

    return "\n".join(salida)

def mostrar_banner(estilo="estandar", decoracion=True, usar_color=None, color="cian"):
    """Imprime el banner en la consola con las opciones especificadas."""
    if usar_color is None:
        usar_color = soporta_colores()

    if estilo == "todos":
        for idx, nom_estilo in enumerate(["estandar", "bloques", "inclinado", "simple"]):
            etiqueta = f"--- [ Estilo: {nom_estilo.upper()} ] ---"
            print(f"\n{COLORES_ANSI['negrita']}{etiqueta}{COLORES_ANSI['reset']}\n")
            print(generar_banner(estilo=nom_estilo, decoracion=decoracion, usar_color=usar_color, color=color))
    else:
        print(generar_banner(estilo=estilo, decoracion=decoracion, usar_color=usar_color, color=color))

# ---------------------------------------------------------------------------
# Entrada Principal (CLI)
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Muestra el texto 'Matemáticas Discretas' en Arte ASCII."
    )
    parser.add_argument(
        "-e", "--estilo",
        choices=["estandar", "bloques", "inclinado", "simple", "todos"],
        default="estandar",
        help="Estilo tipográfico del arte ASCII (por defecto: estandar)"
    )
    parser.add_argument(
        "-c", "--color",
        choices=["cian", "azul", "verde", "magenta", "amarillo", "rojo", "arcoiris", "ninguno"],
        default="cian",
        help="Color del texto (por defecto: cian)"
    )
    parser.add_argument(
        "--sin-color",
        action="store_true",
        help="Desactiva los códigos de color ANSI"
    )
    parser.add_argument(
        "--sin-decoracion",
        action="store_true",
        help="Muestra únicamente las letras sin el marco ni símbolos matemáticos"
    )

    args = parser.parse_args()

    usar_color = False if args.sin_color else None

    mostrar_banner(
        estilo=args.estilo,
        decoracion=not args.sin_decoracion,
        usar_color=usar_color,
        color=args.color
    )

if __name__ == "__main__":
    main()

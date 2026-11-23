"""Programa mínimo del ejercicio «Hola mundo con Jenkins».

Se separa la lógica (:func:`saludo`) de la impresión para poder probarla sin
depender de la consola: así el pipeline de Jenkins valida algo real y no un
simple ``echo``.

Uso::

    python3 hola.py            # Hola Mundo desde Jenkins!!!
    python3 hola.py Ana        # Hola Mundo desde Jenkins!!! (Ana)
"""

from __future__ import annotations

import sys

MENSAJE_POR_DEFECTO = "Hola Mundo desde Jenkins!!!"


def saludo(nombre: str = "") -> str:
    """Devuelve el mensaje de bienvenida, con el nombre entre paréntesis."""
    nombre = nombre.strip()
    if nombre:
        return f"{MENSAJE_POR_DEFECTO} ({nombre})"
    return MENSAJE_POR_DEFECTO


def main(argv: list[str] | None = None) -> int:
    """Imprime el saludo y devuelve el código de salida del proceso."""
    argumentos = sys.argv[1:] if argv is None else argv
    nombre = argumentos[0] if argumentos else ""
    print(saludo(nombre))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Pruebas del programa ``hola.py`` para el ejercicio de Jenkins.

Se ejecutan en segundos y sin dependencias externas, así que sirven tanto en
local como dentro del pipeline (``pytest -q``).
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

from hola import MENSAJE_POR_DEFECTO, saludo

RAIZ = Path(__file__).resolve().parent.parent


def test_saludo_sin_nombre_usa_el_mensaje_por_defecto():
    assert saludo() == MENSAJE_POR_DEFECTO


def test_saludo_con_nombre_agrega_el_nombre_entre_parentesis():
    assert saludo("Ana") == f"{MENSAJE_POR_DEFECTO} (Ana)"


@pytest.mark.parametrize("entrada", ["  Ana  ", "Ana", "\tAna\n"])
def test_saludo_ignora_espacios_alrededor_del_nombre(entrada):
    assert saludo(entrada) == f"{MENSAJE_POR_DEFECTO} (Ana)"


def test_saludo_ignora_un_nombre_vacio_o_solo_espacios():
    assert saludo("   ") == MENSAJE_POR_DEFECTO


def test_ejecucion_como_script_devuelve_codigo_cero():
    resultado = subprocess.run(
        [sys.executable, "hola.py"],
        cwd=RAIZ,
        capture_output=True,
        text=True,
        check=False,
    )

    assert resultado.returncode == 0, resultado.stderr
    assert resultado.stdout.strip() == MENSAJE_POR_DEFECTO


def test_ejecucion_como_script_acepta_un_nombre():
    resultado = subprocess.run(
        [sys.executable, "hola.py", "Jenkins"],
        cwd=RAIZ,
        capture_output=True,
        text=True,
        check=False,
    )

    assert resultado.returncode == 0
    assert "Jenkins" in resultado.stdout

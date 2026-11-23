# Hola mundo con Jenkins 🐧

Ejercicio de **Jenkins (OCY1102)**: el programa más pequeño posible que sirve
para entender cómo funciona un *pipeline* real, desde el `git push` hasta ver
las pruebas en verde.

## ¿Qué contiene?

| Archivo | Rol |
| :--- | :--- |
| `hola.py` | Programa: imprime `Hola Mundo desde Jenkins!!!` (acepta un nombre opcional). |
| `tests/test_hola.py` | 8 pruebas con `pytest` que validan la lógica y la ejecución del script. |
| `Jenkinsfile` | Pipeline declarativo: clona, prepara el entorno, ejecuta el programa, corre las pruebas y archiva el reporte. |
| `requirements-dev.txt` | Dependencia de desarrollo (`pytest`). El programa solo usa la biblioteca estándar. |

## Ejecutar en local

```bash
python3 -m venv .venv
. .venv/bin/activate            # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt

python hola.py                  # Hola Mundo desde Jenkins!!!
python hola.py Ana              # Hola Mundo desde Jenkins!!! (Ana)
pytest -q                       # 8 passed
```

## Crear el job en Jenkins

1. **New Item** → nombre `hola-mundo` → tipo **Pipeline** → *OK*.
2. En *Pipeline*:
   - **Definition**: `Pipeline script from SCM`
   - **SCM**: `Git`
   - **Repository URL**: `https://github.com/0kmango/jenkins-hola-mundo.git`
   - **Branch Specifier**: `*/main`
   - **Script Path**: `Jenkinsfile`
3. *Save* → **Build Now**.

### Qué hace el pipeline

| Etapa | Acción | Falla si... |
| :--- | :--- | :--- |
| Clonar código | `checkout scm` | no se puede clonar el repositorio |
| Preparar entorno | crea `.venv` e instala `requirements-dev.txt` | falta Python 3.11+ en el agente o falla la instalación |
| Ejecutar programa | `python hola.py` | el script lanza una excepción |
| Pruebas automatizadas | `pytest -q --junitxml=resultados/pruebas.xml` | alguna prueba no pasa |

Al final, el reporte XML queda archivado como artefacto del build.

## Requisitos

- Jenkins con el plugin **Pipeline** (viene por defecto) y `git`.
- **Python 3.11 o superior** en el agente (`python3 --version` debe responder).
- Sistema operativo del agente: Linux o macOS (el `Jenkinsfile` usa
  `python3 -m venv`). En un agente Windows habría que cambiar los pasos `sh`
  por `bat` y usar `.venv\Scripts\python.exe`.

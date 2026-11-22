# Proyecto de Aula: Método de Bisección (Grupo 5 - Paracaidista)

Aplicación de escritorio desarrollada en **Python** y **PySide6 (Qt Designer)** para la asignatura **Cálculo Numérico (MECATR24)** — Quinto Nivel, Ingeniería Mecatrónica.

## Integrantes y Roles
* **Bravo Vaca Maholy Liceth**: Programación de la lógica numérica (`metodo/biseccion.py`) e integración.
* **Quijije Zambrano Willian Xavier**: Diseño visual en Qt Designer (`ui/ventana_principal.ui`) y gráficas con Matplotlib (`graficas.py`).
* **García García Jordy Aaron**: Casos de validación (`tests/test_metodo.py`), pruebas con `pytest` y documentación.

## Descripción del Caso de Aplicación (Grupo 5)
Un paracaidista de masa $m = 68.1\text{ kg}$ cae bajo la influencia de la gravedad ($g = 9.81\text{ m/s}^2$). Su velocidad en el tiempo $t$ está dada por:
$$v(t) = \frac{g \cdot m}{c} \left(1 - e^{-(c/m)t}\right)$$

Se desea hallar el coeficiente de arrastre $c\text{ (kg/s)}$ necesario para que alcance una velocidad $v = 40\text{ m/s}$ en $t = 10\text{ s}$, resolviendo la ecuación no lineal:
$$f(c) = \frac{9.81 \cdot 68.1}{c} \left(1 - e^{-(c/68.1)\cdot 10}\right) - 40 = 0$$

Con el intervalo inicial $[12, 20]$ y tolerancia $\varepsilon_s = 0.5\%$, el método converge en **7 iteraciones** a **$c = 14.8125\text{ kg/s}$** (valor de alta precisión: $14.8011\text{ kg/s}$).

## Estructura del Repositorio
```text
CN-ParaleloA-Grupo5/
├── README.md
├── requirements.txt
├── main.py
├── ui_ventana_principal.py
├── graficas.py
├── ui/
│   └── ventana_principal.ui
├── metodo/
│   ├── __init__.py
│   └── biseccion.py
├── tests/
│   └── test_metodo.py
└── capturas/
```

## Instalación y Ejecución
1. Crear y activar el entorno virtual:
   ```bash
   python -m venv .venv
   # En Windows:
   .venv\Scripts\activate
   # En Linux/macOS:
   source .venv/bin/activate
   ```
2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecutar la aplicación:
   ```bash
   python main.py
   ```
4. Ejecutar pruebas unitarias:
   ```bash
   pytest
   ```

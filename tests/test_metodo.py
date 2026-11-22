import pytest
from metodo.biseccion import biseccion, busqueda_incremental

def test_caso_grupo5_paracaidista():
    """Valida el caso obligatorio del Grupo 5 (Sección 8 de la guía): c = 14.8125 kg/s en 7 iteraciones."""
    expr = "(9.81*68.1/x)*(1-exp(-(x/68.1)*10))-40"
    res = biseccion(expr_str=expr, xl=12.0, xu=20.0, es=0.5, max_iter=50, v_verdadero=14.8011)
    assert res["iteraciones_totales"] == 7
    assert pytest.approx(res["raiz"], rel=1e-4) == 14.8125

def test_ejemplo_libro_chapra():
    """Valida el ejemplo clásico de bisección f(x) = exp(-x) - x en [0, 1]."""
    res = biseccion(expr_str="exp(-x) - x", xl=0.0, xu=1.0, es=0.05, max_iter=50, v_verdadero=0.56714329)
    assert pytest.approx(res["raiz"], abs=1e-3) == 0.567143

def test_sin_cambio_de_signo():
    """Verifica que lance ValueError cuando f(xl)*f(xu) >= 0."""
    with pytest.raises(ValueError, match="cambio de signo"):
        biseccion(expr_str="x^2 + 4", xl=-2.0, xu=2.0, es=0.5)

def test_sintaxis_invalida():
    """Verifica el manejo de errores al ingresar una expresión inválida."""
    with pytest.raises(ValueError, match="sintaxis"):
        biseccion(expr_str="9.81 * ((x +", xl=1.0, xu=5.0, es=0.5)

def test_busqueda_incremental():
    """Verifica que la búsqueda incremental detecte el intervalo [14, 15] para el paracaidista."""
    expr = "(9.81*68.1/x)*(1-exp(-(x/68.1)*10))-40"
    intervalos = busqueda_incremental(expr, 12.0, 20.0, 1.0)
    assert (14.0, 15.0) in intervalos

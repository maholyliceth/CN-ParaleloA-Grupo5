import math
import numpy as np
import sympy as sp

def parsear_funcion(expr_str: str):
    """Convierte una expresión de texto en una función evaluable f(x) usando SymPy."""
    if not expr_str or not expr_str.strip():
        raise ValueError("La función f(x) no puede estar vacía.")
    expr_clean = expr_str.strip().replace("^", "**")
    x = sp.Symbol('x')
    # Permitir e y pi como constantes simbólicas
    local_dict = {'x': x, 'e': sp.E, 'pi': sp.pi}
    try:
        expr = sp.sympify(expr_clean, locals=local_dict)
    except Exception as exc:
        raise ValueError(f"Error de sintaxis en la función: {exc}")
    
    free_syms = expr.free_symbols
    if not free_syms.issubset({x}):
        raise ValueError(f"La función solo debe depender de la variable 'x'. Variables detectadas: {free_syms}")
    
    func_num = sp.lambdify(x, expr, modules=["numpy"])
    
    def f(val):
        try:
            res = func_num(val)
            return res
        except Exception as exc:
            raise ValueError(f"Error al evaluar f({val}): {exc}")
            
    return f, expr

def busqueda_incremental(expr_str: str, x_inicio: float, x_fin: float, delta_x: float):
    """Busca subintervalos [a, b] donde f(a)*f(b) < 0 con paso delta_x."""
    if delta_x <= 0:
        raise ValueError("El paso Δx debe ser mayor que 0.")
    if x_inicio >= x_fin:
        raise ValueError("El límite inferior de búsqueda debe ser menor que el superior.")
        
    f, _ = parsear_funcion(expr_str)
    puntos = np.arange(x_inicio, x_fin + delta_x, delta_x)
    intervalos = []
    
    for i in range(len(puntos) - 1):
        a, b = float(puntos[i]), float(puntos[i+1])
        fa, fb = float(f(a)), float(f(b))
        if np.isnan(fa) or np.isnan(fb) or np.isinf(fa) or np.isinf(fb):
            continue
        if fa == 0.0:
            intervalos.append((a, a))
        elif fa * fb < 0:
            intervalos.append((round(a, 6), round(b, 6)))
            
    return intervalos

def biseccion(expr_str: str, xl: float, xu: float, es: float, max_iter: int = 100, v_verdadero: float = None):
    """
    Implementación manual del Método de Bisección (Chapra & Canale, Cap. 5).
    Retorna un diccionario con las iteraciones, la raíz estimada, errores y criterios.
    """
    if xl >= xu:
        raise ValueError("El límite inferior xl debe ser estrictamente menor que xu.")
    if es <= 0:
        raise ValueError("La tolerancia εs (%) debe ser mayor que 0.")
    if max_iter < 1:
        raise ValueError("El máximo de iteraciones debe ser al menos 1.")
        
    f, _ = parsear_funcion(expr_str)
    
    f_xl = float(f(xl))
    f_xu = float(f(xu))
    
    if math.isnan(f_xl) or math.isnan(f_xu) or math.isinf(f_xl) or math.isinf(f_xu):
        raise ValueError("La función no está definida (NaN o Inf) en los extremos del intervalo.")
        
    if f_xl * f_xu >= 0:
        raise ValueError(
            f"No existe cambio de signo en el intervalo [{xl}, {xu}].\n"
            f"f({xl}) = {f_xl:.6g}, f({xu}) = {f_xu:.6g}.\n"
            "El método de bisección requiere que f(xl) · f(xu) < 0."
        )
        
    # Cálculo teórico de iteraciones según fórmula de la guía:
    # n = log2(Delta_x0 / E_{a,d}) donde E_{a,d} es el error absoluto deseado.
    # Como es (%) = (E_{a,d} / |x_raiz|) * 100, estimamos |x_raiz| con el punto medio inicial o v_verdadero
    dx0 = xu - xl
    ref_val = abs(v_verdadero) if (v_verdadero is not None and v_verdadero != 0) else abs((xl + xu) / 2.0)
    if ref_val == 0:
        ref_val = 1.0
    ea_deseado = (es / 100.0) * ref_val
    n_teorico = math.ceil(math.log2(dx0 / ea_deseado)) if ea_deseado > 0 else max_iter
    
    iteraciones = []
    xr_anterior = None
    criterio_cumplido = "Máximo de iteraciones alcanzado"
    
    xl_curr = float(xl)
    xu_curr = float(xu)
    
    for i in range(1, max_iter + 1):
        xr = (xl_curr + xu_curr) / 2.0
        f_xl = float(f(xl_curr))
        f_xr = float(f(xr))
        prod = f_xl * f_xr
        
        if i == 1 or xr == 0:
            ea = None
        else:
            ea = abs((xr - xr_anterior) / xr) * 100.0
            
        if v_verdadero is not None and v_verdadero != 0:
            et = abs((v_verdadero - xr) / v_verdadero) * 100.0
        else:
            et = None
            
        if prod < 0:
            subintervalo = "Izquierdo [xl, xr]"
            sig_xl, sig_xu = xl_curr, xr
        elif prod > 0:
            subintervalo = "Derecho [xr, xu]"
            sig_xl, sig_xu = xr, xu_curr
        else:
            subintervalo = "Raíz exacta"
            sig_xl, sig_xu = xr, xr
            ea = 0.0
            
        iteraciones.append({
            "i": i,
            "xl": xl_curr,
            "xu": xu_curr,
            "xr": xr,
            "f_xl": f_xl,
            "f_xr": f_xr,
            "producto": prod,
            "ea": ea,
            "et": et,
            "subintervalo": subintervalo
        })
        
        if prod == 0:
            criterio_cumplido = "Raíz exacta encontrada (f(xr) = 0)"
            break
            
        if ea is not None and ea < es:
            criterio_cumplido = f"Tolerancia alcanzada (εa = {ea:.6f}% < εs = {es}%)"
            break
            
        xr_anterior = xr
        xl_curr, xu_curr = sig_xl, sig_xu
        
    ultimo = iteraciones[-1]
    return {
        "raiz": ultimo["xr"],
        "iteraciones_totales": ultimo["i"],
        "n_teorico": n_teorico,
        "ea_final": ultimo["ea"],
        "et_final": ultimo["et"],
        "criterio": criterio_cumplido,
        "tabla": iteraciones
    }

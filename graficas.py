import numpy as np
from metodo.biseccion import parsear_funcion

def graficar_funcion_y_raices(fig, expr_str: str, xl: float, xu: float, historial: list = None):
    """Dibuja f(x) en [xl, xu] y marca las aproximaciones xr de cada iteración."""
    fig.clear()
    ax = fig.add_subplot(111)
    f, _ = parsear_funcion(expr_str)
    
    margen = (xu - xl) * 0.1
    x_vals = np.linspace(xl - margen, xu + margen, 400)
    y_vals = []
    for val in x_vals:
        try:
            y_vals.append(float(f(val)))
        except Exception:
            y_vals.append(np.nan)
            
    ax.plot(x_vals, y_vals, label=f"f(x) = {expr_str}", color="#1f77b4", linewidth=2)
    ax.axhline(0, color="black", linewidth=1, linestyle="--")
    ax.axvline(xl, color="#7f7f7f", linestyle=":", label=f"xl = {xl}")
    ax.axvline(xu, color="#7f7f7f", linestyle=":", label=f"xu = {xu}")
    
    if historial:
        xrs = [fila["xr"] for fila in historial]
        fxrs = [fila["f_xr"] for fila in historial]
        ax.scatter(xrs[:-1], fxrs[:-1], color="#ff7f0e", zorder=4, label="Iteraciones xr", alpha=0.75)
        ax.scatter([xrs[-1]], [fxrs[-1]], color="#d62728", s=80, zorder=5, label=f"Raíz ≈ {xrs[-1]:.6f}")
        
    ax.set_title("Gráfica de f(x) y convergencia de xr")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.legend(loc="best", fontsize="small")
    fig.tight_layout()

def graficar_error(fig, historial: list, es: float):
    """Dibuja el error aproximado εa (%) contra la iteración i en escala semilogarítmica."""
    fig.clear()
    ax = fig.add_subplot(111)
    
    iters = [fila["i"] for fila in historial if fila["ea"] is not None and fila["ea"] > 0]
    eas = [fila["ea"] for fila in historial if fila["ea"] is not None and fila["ea"] > 0]
    
    if iters:
        ax.semilogy(iters, eas, marker="o", color="#2ca02c", linewidth=2, label="Error aproximado εa (%)")
        ax.axhline(es, color="#d62728", linestyle="--", label=f"Tolerancia εs = {es}%")
        ax.set_xticks(iters)
    else:
        ax.text(0.5, 0.5, "Se requieren al menos 2 iteraciones con εa > 0\npara graficar el error en escala logarítmica.",
                ha="center", va="center", transform=ax.transAxes)
        
    ax.set_title("Convergencia del Error Aproximado (Escala Semilogarítmica)")
    ax.set_xlabel("Iteración (i)")
    ax.set_ylabel("Error relativo aproximado εa (%)")
    ax.grid(True, which="both", linestyle="--", alpha=0.5)
    ax.legend(loc="best", fontsize="small")
    fig.tight_layout()

import csv
import sys
from PySide6.QtWidgets import (
    QApplication, QFileDialog, QHeaderView, QMainWindow,
    QMessageBox, QTableWidgetItem, QVBoxLayout
)
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from ui_ventana_principal import Ui_MainWindow
from metodo.biseccion import biseccion, busqueda_incremental
from graficas import graficar_error, graficar_funcion_y_raices

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ultimo_resultado = None
        
        # Lienzo Matplotlib 1: Gráfica de f(x)
        self.fig_func = Figure(figsize=(5, 3.5))
        self.canvas_func = FigureCanvasQTAgg(self.fig_func)
        QVBoxLayout(self.ui.widgetGrafica).addWidget(self.canvas_func)
        
        # Lienzo Matplotlib 2: Gráfica de Error
        self.fig_err = Figure(figsize=(5, 3.5))
        self.canvas_err = FigureCanvasQTAgg(self.fig_err)
        QVBoxLayout(self.ui.widgetGraficaError).addWidget(self.canvas_err)
        
        # Configurar encabezados de tabla
        columnas = [
            "i", "xl", "xu", "xr", "f(xl)", "f(xr)",
            "f(xl)·f(xr)", "εa (%)", "εt (%)", "Subintervalo"
        ]
        self.ui.tablaResultados.setColumnCount(len(columnas))
        self.ui.tablaResultados.setHorizontalHeaderLabels(columnas)
        self.ui.tablaResultados.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.tablaResultados.horizontalHeader().setStretchLastSection(True)
        
        # Conectar señales
        self.ui.cmbEjemplos.currentIndexChanged.connect(self.cargar_ejemplo)
        self.ui.btnCalcular.clicked.connect(self.calcular)
        self.ui.btnLimpiar.clicked.connect(self.limpiar)
        self.ui.btnExportar.clicked.connect(self.exportar_csv)
        self.ui.btnBuscarIntervalos.clicked.connect(self.sugerir_intervalos)
        
        # Cargar caso del Grupo 5 por defecto
        self.cargar_ejemplo(0)
        self.ui.statusbar.showMessage("Listo | Cálculo Numérico (MECATR24) - Grupo 5: Paracaidista")

    def cargar_ejemplo(self, index: int):
        if index == 0:
            # Caso obligatorio Grupo 5: Paracaidista
            self.ui.txtFuncion.setText("(9.81*68.1/x)*(1-exp(-(x/68.1)*10))-40")
            self.ui.spnXl.setValue(12.0)
            self.ui.spnXu.setValue(20.0)
            self.ui.spnEs.setValue(0.5)
            self.ui.spnMaxIter.setValue(50)
            self.ui.txtValorVerdadero.setText("14.8011")
            self.ui.txtUnidades.setText("kg/s")
            self.ui.spnDeltaX.setValue(1.0)
        elif index == 1:
            # Ejemplo clásico del libro Chapra (Cap. 5)
            self.ui.txtFuncion.setText("exp(-x) - x")
            self.ui.spnXl.setValue(0.0)
            self.ui.spnXu.setValue(1.0)
            self.ui.spnEs.setValue(0.05)
            self.ui.spnMaxIter.setValue(50)
            self.ui.txtValorVerdadero.setText("0.567143")
            self.ui.txtUnidades.setText("adimensional")
            self.ui.spnDeltaX.setValue(0.2)

    def sugerir_intervalos(self):
        try:
            expr_str = self.ui.txtFuncion.text()
            xl = self.ui.spnXl.value()
            xu = self.ui.spnXu.value()
            dx = self.ui.spnDeltaX.value()
            
            # Graficar el intervalo actual previamente
            graficar_funcion_y_raices(self.fig_func, expr_str, xl, xu)
            self.canvas_func.draw()
            
            intervalos = busqueda_incremental(expr_str, xl, xu, dx)
            if not intervalos:
                QMessageBox.information(
                    self, "Búsqueda Incremental",
                    f"No se detectaron cambios de signo en [{xl}, {xu}] con paso Δx = {dx}."
                )
            else:
                lista_str = "\n".join([f"• [{a}, {b}]" for a, b in intervalos])
                QMessageBox.information(
                    self, "Intervalos Sugeridos",
                    f"Subintervalos con cambio de signo detectados:\n{lista_str}"
                )
                # Aplicar automáticamente el primer subintervalo encontrado
                self.ui.spnXl.setValue(intervalos[0][0])
                self.ui.spnXu.setValue(intervalos[0][1])
                self.ui.statusbar.showMessage(f"Intervalo actualizado a [{intervalos[0][0]}, {intervalos[0][1]}]")
        except Exception as e:
            QMessageBox.warning(self, "Error en búsqueda incremental", str(e))

    def calcular(self):
        try:
            expr_str = self.ui.txtFuncion.text()
            xl = self.ui.spnXl.value()
            xu = self.ui.spnXu.value()
            es = self.ui.spnEs.value()
            max_iter = self.ui.spnMaxIter.value()
            unidades = self.ui.txtUnidades.text().strip()
            
            v_verd_txt = self.ui.txtValorVerdadero.text().strip()
            v_verd = float(v_verd_txt) if v_verd_txt else None
            
            res = biseccion(expr_str, xl, xu, es, max_iter, v_verd)
            self.ultimo_resultado = res
            
            # Llenar tabla
            tabla = res["tabla"]
            self.ui.tablaResultados.setRowCount(len(tabla))
            for row_idx, fila in enumerate(tabla):
                ea_str = f"{fila['ea']:.6f}%" if fila["ea"] is not None else "---"
                et_str = f"{fila['et']:.6f}%" if fila["et"] is not None else "---"
                valores = [
                    str(fila["i"]),
                    f"{fila['xl']:.7f}",
                    f"{fila['xu']:.7f}",
                    f"{fila['xr']:.7f}",
                    f"{fila['f_xl']:.7f}",
                    f"{fila['f_xr']:.7f}",
                    f"{fila['producto']:.7f}",
                    ea_str,
                    et_str,
                    fila["subintervalo"]
                ]
                for col_idx, val in enumerate(valores):
                    self.ui.tablaResultados.setItem(row_idx, col_idx, QTableWidgetItem(val))
                    
            # Panel de resultado final
            ea_fin = f"{res['ea_final']:.6f}%" if res["ea_final"] is not None else "N/A"
            et_fin = f"{res['et_final']:.6f}%" if res["et_final"] is not None else "N/A"
            
            interpretacion = ""
            if self.ui.cmbEjemplos.currentIndex() == 0:
                interpretacion = (
                    f"\nInterpretación física: Para que un paracaidista de 68.1 kg alcance 40 m/s "
                    f"en 10 s, se requiere un coeficiente de arrastre c ≈ {res['raiz']:.4f} {unidades}."
                )
                
            texto_res = (
                f"Raíz estimada: {res['raiz']:.6f} {unidades}\n"
                f"Iteraciones realizadas: {res['iteraciones_totales']} (Teóricas n ≈ {res['n_teorico']})\n"
                f"Error aproximado final (εa): {ea_fin}\n"
                f"Error verdadero final (εt): {et_fin}\n"
                f"Criterio de parada: {res['criterio']}"
                f"{interpretacion}"
            )
            self.ui.txtResultadoFinal.setPlainText(texto_res)
            
            # Actualizar gráficas
            graficar_funcion_y_raices(self.fig_func, expr_str, xl, xu, tabla)
            self.canvas_func.draw()
            
            graficar_error(self.fig_err, tabla, es)
            self.canvas_err.draw()
            
            self.ui.statusbar.showMessage(f"Cálculo completado en {res['iteraciones_totales']} iteraciones.")
            
        except ValueError as ve:
            QMessageBox.warning(self, "Validación de Datos", str(ve))
        except Exception as e:
            QMessageBox.critical(self, "Error Inesperado", str(e))

    def limpiar(self):
        self.ui.tablaResultados.setRowCount(0)
        self.ui.txtResultadoFinal.clear()
        self.fig_func.clear()
        self.canvas_func.draw()
        self.fig_err.clear()
        self.canvas_err.draw()
        self.ultimo_resultado = None
        self.ui.statusbar.showMessage("Resultados limpiados.")

    def exportar_csv(self):
        if not self.ultimo_resultado:
            QMessageBox.warning(self, "Exportar CSV", "Primero debe ejecutar un cálculo para exportar resultados.")
            return
            
        ruta, _ = QFileDialog.getSaveFileName(self, "Guardar tabla como CSV", "resultados_biseccion_grupo5.csv", "Archivos CSV (*.csv)")
        if not ruta:
            return
            
        try:
            with open(ruta, mode="w", newline="", encoding="utf-8") as archivo:
                writer = csv.writer(archivo)
                writer.writerow(["i", "xl", "xu", "xr", "f(xl)", "f(xr)", "f(xl)*f(xr)", "ea (%)", "et (%)", "Subintervalo"])
                for fila in self.ultimo_resultado["tabla"]:
                    writer.writerow([
                        fila["i"], fila["xl"], fila["xu"], fila["xr"],
                        fila["f_xl"], fila["f_xr"], fila["producto"],
                        fila["ea"] if fila["ea"] is not None else "",
                        fila["et"] if fila["et"] is not None else "",
                        fila["subintervalo"]
                    ])
            QMessageBox.information(self, "Exportación Exitosa", f"Tabla exportada correctamente a:\n{ruta}")
        except Exception as e:
            QMessageBox.critical(self, "Error al exportar", str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())

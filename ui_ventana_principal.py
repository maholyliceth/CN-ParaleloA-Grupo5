# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'ui/ventana_principal.ui'
# Generated for PySide6

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize
from PySide6.QtWidgets import (
    QAbstractItemView, QComboBox, QDoubleSpinBox, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSpinBox, QStatusBar, QTabWidget, QTableWidget,
    QTextEdit, QVBoxLayout, QWidget
)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1180, 760)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutMain = QVBoxLayout(self.centralwidget)
        self.verticalLayoutMain.setObjectName("verticalLayoutMain")
        
        self.tabPrincipal = QTabWidget(self.centralwidget)
        self.tabPrincipal.setObjectName("tabPrincipal")
        
        # Tab 1: Método
        self.tabMetodo = QWidget()
        self.tabMetodo.setObjectName("tabMetodo")
        self.horizontalLayoutMetodo = QHBoxLayout(self.tabMetodo)
        self.horizontalLayoutMetodo.setObjectName("horizontalLayoutMetodo")
        
        # Panel Izquierdo
        self.panelIzquierdo = QWidget(self.tabMetodo)
        self.panelIzquierdo.setObjectName("panelIzquierdo")
        self.panelIzquierdo.setMaximumSize(QSize(390, 16777215))
        self.verticalLayoutIzq = QVBoxLayout(self.panelIzquierdo)
        self.verticalLayoutIzq.setObjectName("verticalLayoutIzq")
        
        # GroupBox Ejemplos
        self.grpEjemplos = QGroupBox(self.panelIzquierdo)
        self.grpEjemplos.setObjectName("grpEjemplos")
        self.verticalLayoutEj = QVBoxLayout(self.grpEjemplos)
        self.cmbEjemplos = QComboBox(self.grpEjemplos)
        self.cmbEjemplos.setObjectName("cmbEjemplos")
        self.cmbEjemplos.addItem("")
        self.cmbEjemplos.addItem("")
        self.cmbEjemplos.addItem("")
        self.verticalLayoutEj.addWidget(self.cmbEjemplos)
        self.verticalLayoutIzq.addWidget(self.grpEjemplos)
        
        # GroupBox Parámetros
        self.grpParametros = QGroupBox(self.panelIzquierdo)
        self.grpParametros.setObjectName("grpParametros")
        self.gridLayoutParams = QGridLayout(self.grpParametros)
        
        self.lblFuncion = QLabel(self.grpParametros)
        self.gridLayoutParams.addWidget(self.lblFuncion, 0, 0, 1, 1)
        self.txtFuncion = QLineEdit(self.grpParametros)
        self.txtFuncion.setObjectName("txtFuncion")
        self.gridLayoutParams.addWidget(self.txtFuncion, 0, 1, 1, 1)
        
        self.lblXl = QLabel(self.grpParametros)
        self.gridLayoutParams.addWidget(self.lblXl, 1, 0, 1, 1)
        self.spnXl = QDoubleSpinBox(self.grpParametros)
        self.spnXl.setObjectName("spnXl")
        self.spnXl.setDecimals(6)
        self.spnXl.setRange(-100000.0, 100000.0)
        self.spnXl.setValue(12.0)
        self.gridLayoutParams.addWidget(self.spnXl, 1, 1, 1, 1)
        
        self.lblXu = QLabel(self.grpParametros)
        self.gridLayoutParams.addWidget(self.lblXu, 2, 0, 1, 1)
        self.spnXu = QDoubleSpinBox(self.grpParametros)
        self.spnXu.setObjectName("spnXu")
        self.spnXu.setDecimals(6)
        self.spnXu.setRange(-100000.0, 100000.0)
        self.spnXu.setValue(20.0)
        self.gridLayoutParams.addWidget(self.spnXu, 2, 1, 1, 1)
        
        self.lblEs = QLabel(self.grpParametros)
        self.gridLayoutParams.addWidget(self.lblEs, 3, 0, 1, 1)
        self.spnEs = QDoubleSpinBox(self.grpParametros)
        self.spnEs.setObjectName("spnEs")
        self.spnEs.setDecimals(6)
        self.spnEs.setRange(0.000001, 100.0)
        self.spnEs.setValue(0.5)
        self.gridLayoutParams.addWidget(self.spnEs, 3, 1, 1, 1)
        
        self.lblMaxIter = QLabel(self.grpParametros)
        self.gridLayoutParams.addWidget(self.lblMaxIter, 4, 0, 1, 1)
        self.spnMaxIter = QSpinBox(self.grpParametros)
        self.spnMaxIter.setObjectName("spnMaxIter")
        self.spnMaxIter.setRange(1, 1000)
        self.spnMaxIter.setValue(50)
        self.gridLayoutParams.addWidget(self.spnMaxIter, 4, 1, 1, 1)
        
        self.lblVVerdadero = QLabel(self.grpParametros)
        self.gridLayoutParams.addWidget(self.lblVVerdadero, 5, 0, 1, 1)
        self.txtValorVerdadero = QLineEdit(self.grpParametros)
        self.txtValorVerdadero.setObjectName("txtValorVerdadero")
        self.gridLayoutParams.addWidget(self.txtValorVerdadero, 5, 1, 1, 1)
        
        self.lblUnidades = QLabel(self.grpParametros)
        self.gridLayoutParams.addWidget(self.lblUnidades, 6, 0, 1, 1)
        self.txtUnidades = QLineEdit(self.grpParametros)
        self.txtUnidades.setObjectName("txtUnidades")
        self.gridLayoutParams.addWidget(self.txtUnidades, 6, 1, 1, 1)
        
        self.verticalLayoutIzq.addWidget(self.grpParametros)
        
        # GroupBox Búsqueda Incremental
        self.grpIncremental = QGroupBox(self.panelIzquierdo)
        self.grpIncremental.setObjectName("grpIncremental")
        self.horizontalLayoutInc = QHBoxLayout(self.grpIncremental)
        self.lblDeltaX = QLabel(self.grpIncremental)
        self.horizontalLayoutInc.addWidget(self.lblDeltaX)
        self.spnDeltaX = QDoubleSpinBox(self.grpIncremental)
        self.spnDeltaX.setObjectName("spnDeltaX")
        self.spnDeltaX.setDecimals(4)
        self.spnDeltaX.setRange(0.0001, 1000.0)
        self.spnDeltaX.setValue(1.0)
        self.horizontalLayoutInc.addWidget(self.spnDeltaX)
        self.btnBuscarIntervalos = QPushButton(self.grpIncremental)
        self.btnBuscarIntervalos.setObjectName("btnBuscarIntervalos")
        self.horizontalLayoutInc.addWidget(self.btnBuscarIntervalos)
        self.verticalLayoutIzq.addWidget(self.grpIncremental)
        
        # Botones
        self.horizontalLayoutBotones = QHBoxLayout()
        self.btnCalcular = QPushButton(self.panelIzquierdo)
        self.btnCalcular.setObjectName("btnCalcular")
        self.horizontalLayoutBotones.addWidget(self.btnCalcular)
        self.btnLimpiar = QPushButton(self.panelIzquierdo)
        self.btnLimpiar.setObjectName("btnLimpiar")
        self.horizontalLayoutBotones.addWidget(self.btnLimpiar)
        self.btnExportar = QPushButton(self.panelIzquierdo)
        self.btnExportar.setObjectName("btnExportar")
        self.horizontalLayoutBotones.addWidget(self.btnExportar)
        self.verticalLayoutIzq.addLayout(self.horizontalLayoutBotones)
        
        # GroupBox Resultados
        self.grpResultados = QGroupBox(self.panelIzquierdo)
        self.grpResultados.setObjectName("grpResultados")
        self.verticalLayoutRes = QVBoxLayout(self.grpResultados)
        self.txtResultadoFinal = QTextEdit(self.grpResultados)
        self.txtResultadoFinal.setObjectName("txtResultadoFinal")
        self.txtResultadoFinal.setReadOnly(True)
        self.verticalLayoutRes.addWidget(self.txtResultadoFinal)
        self.verticalLayoutIzq.addWidget(self.grpResultados)
        
        self.horizontalLayoutMetodo.addWidget(self.panelIzquierdo)
        
        # Panel Derecho
        self.panelDerecho = QWidget(self.tabMetodo)
        self.panelDerecho.setObjectName("panelDerecho")
        self.verticalLayoutDer = QVBoxLayout(self.panelDerecho)
        
        self.tabGraficas = QTabWidget(self.panelDerecho)
        self.tabGraficas.setObjectName("tabGraficas")
        
        self.tabGraficaFuncion = QWidget()
        self.verticalLayoutGraf1 = QVBoxLayout(self.tabGraficaFuncion)
        self.widgetGrafica = QWidget(self.tabGraficaFuncion)
        self.widgetGrafica.setObjectName("widgetGrafica")
        self.verticalLayoutGraf1.addWidget(self.widgetGrafica)
        self.tabGraficas.addTab(self.tabGraficaFuncion, "")
        
        self.tabGraficaError = QWidget()
        self.verticalLayoutGraf2 = QVBoxLayout(self.tabGraficaError)
        self.widgetGraficaError = QWidget(self.tabGraficaError)
        self.widgetGraficaError.setObjectName("widgetGraficaError")
        self.verticalLayoutGraf2.addWidget(self.widgetGraficaError)
        self.tabGraficas.addTab(self.tabGraficaError, "")
        
        self.verticalLayoutDer.addWidget(self.tabGraficas)
        
        self.tablaResultados = QTableWidget(self.panelDerecho)
        self.tablaResultados.setObjectName("tablaResultados")
        self.tablaResultados.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablaResultados.setAlternatingRowColors(True)
        self.verticalLayoutDer.addWidget(self.tablaResultados)
        
        self.horizontalLayoutMetodo.addWidget(self.panelDerecho)
        self.tabPrincipal.addTab(self.tabMetodo, "")
        
        # Tab 2: Acerca de
        self.tabAcercaDe = QWidget()
        self.verticalLayoutAcerca = QVBoxLayout(self.tabAcercaDe)
        self.txtAcercaDe = QTextEdit(self.tabAcercaDe)
        self.txtAcercaDe.setObjectName("txtAcercaDe")
        self.txtAcercaDe.setReadOnly(True)
        self.verticalLayoutAcerca.addWidget(self.txtAcercaDe)
        self.tabPrincipal.addTab(self.tabAcercaDe, "")
        
        self.verticalLayoutMain.addWidget(self.tabPrincipal)
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.retranslateUi(MainWindow)
        self.tabPrincipal.setCurrentIndex(0)
        self.tabGraficas.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Método de Bisección - Cálculo Numérico (Grupo 5: Paracaidista)"))
        self.grpEjemplos.setTitle(_translate("MainWindow", "Casos Precargados"))
        self.cmbEjemplos.setItemText(0, _translate("MainWindow", "Caso Grupo 5: Paracaidista (arrastre c)"))
        self.cmbEjemplos.setItemText(1, _translate("MainWindow", "Ejemplo Libro: f(x) = exp(-x) - x"))
        self.cmbEjemplos.setItemText(2, _translate("MainWindow", "Personalizado"))
        self.grpParametros.setTitle(_translate("MainWindow", "Parámetros de Entrada"))
        self.lblFuncion.setText(_translate("MainWindow", "Función f(x):"))
        self.txtFuncion.setPlaceholderText(_translate("MainWindow", "Ej: (9.81*68.1/x)*(1-exp(-(x/68.1)*10))-40"))
        self.lblXl.setText(_translate("MainWindow", "Límite inferior (xl):"))
        self.lblXu.setText(_translate("MainWindow", "Límite superior (xu):"))
        self.lblEs.setText(_translate("MainWindow", "Tolerancia εs (%):"))
        self.lblMaxIter.setText(_translate("MainWindow", "Máx. iteraciones:"))
        self.lblVVerdadero.setText(_translate("MainWindow", "Valor verdadero (opc.):"))
        self.txtValorVerdadero.setPlaceholderText(_translate("MainWindow", "Opcional (ej: 14.8011)"))
        self.lblUnidades.setText(_translate("MainWindow", "Unidades físicas:"))
        self.txtUnidades.setText(_translate("MainWindow", "kg/s"))
        self.grpIncremental.setTitle(_translate("MainWindow", "Método Gráfico / Búsqueda Incremental"))
        self.lblDeltaX.setText(_translate("MainWindow", "Paso Δx:"))
        self.btnBuscarIntervalos.setText(_translate("MainWindow", "Sugerir Intervalos"))
        self.btnCalcular.setText(_translate("MainWindow", "Calcular"))
        self.btnLimpiar.setText(_translate("MainWindow", "Limpiar"))
        self.btnExportar.setText(_translate("MainWindow", "Exportar CSV"))
        self.grpResultados.setTitle(_translate("MainWindow", "Resumen de Resultados"))
        self.tabGraficas.setTabText(self.tabGraficas.indexOf(self.tabGraficaFuncion), _translate("MainWindow", "Gráfica f(x) y Raíz"))
        self.tabGraficas.setTabText(self.tabGraficas.indexOf(self.tabGraficaError), _translate("MainWindow", "Convergencia del Error (εa)"))
        self.tabPrincipal.setTabText(self.tabPrincipal.indexOf(self.tabMetodo), _translate("MainWindow", "Método de Bisección"))
        self.tabPrincipal.setTabText(self.tabPrincipal.indexOf(self.tabAcercaDe), _translate("MainWindow", "Acerca de / Caso de Estudio"))
        self.txtAcercaDe.setHtml(_translate("MainWindow", """
        <h2>Proyecto de Aula: Cálculo Numérico (MECATR24)</h2>
        <p><b>Asignatura:</b> Cálculo Numérico - Quinto Nivel, Ingeniería Mecatrónica</p>
        <p><b>Unidad 1:</b> Software para cálculo numérico, teoría del error y ecuaciones no lineales</p>
        <p><b>Grupo 5 - Proyecto B:</b> Método de Bisección aplicado al coeficiente de arrastre de un paracaidista.</p>
        <p><b>Integrantes:</b></p>
        <ul>
        <li>Bravo Vaca Maholy Liceth (Lógica numérica e integración)</li>
        <li>Quijije Zambrano Willian Xavier (Diseño Qt Designer y gráficas)</li>
        <li>García García Jordy Aaron (Validación, pruebas y documentación)</li>
        </ul>
        <hr/>
        <h3>Descripción Física del Caso de Aplicación (Grupo 5)</h3>
        <p>Un paracaidista de masa <b>m = 68.1 kg</b> salta en caída libre bajo gravedad <b>g = 9.81 m/s²</b>. Se busca el coeficiente de arrastre <b>c (kg/s)</b> para alcanzar <b>v = 40 m/s</b> en <b>t = 10 s</b>:</p>
        <p><code>f(c) = (9.81 · 68.1 / c) · (1 - e^(-(c/68.1)·10)) - 40 = 0</code></p>
        """))

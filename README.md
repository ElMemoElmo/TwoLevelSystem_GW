# Proyecto FIS205: Simulación Cuántica de la Interacción Espín-Onda Gravitacional

Este repositorio contiene el desarrollo computacional y los informes del **Proyecto Semestral de Física Computacional (FIS205)**. El objetivo principal de este proyecto es simular y visualizar la dinámica de un sistema cuántico de dos niveles (espín 1/2) perturbado por la métrica de una onda gravitacional incidente.

## Descripción del Proyecto

A diferencia de la interferometría óptica kilométrica tradicional (como LIGO), este proyecto explora la detección localizada de ondas gravitacionales a escala cuántica. Basándose en el marco teórico de las Coordenadas Normales de Fermi y la analogía gravito-electromagnética, se modela cómo el espaciotiempo induce transiciones cuánticas coherentes.

La dinámica del sistema se resuelve numéricamente abandonando el vector de estado puro clásico y adoptando el **Formalismo de la Matriz Densidad**. La evolución temporal se rige por la ecuación de Liouville-von Neumann, integrada paso a paso mediante algoritmos adaptativos de Runge-Kutta.

## Características y Resultados Actuales (Avance 2)

* **Integración de la Matriz Densidad:** Resolución del conmutador de Liouville-von Neumann vectorizando el operador densidad matricial.
* **Oscilaciones de Rabi:** Comprobación numérica de transiciones completas entre el estado base y el estado excitado bajo condición de resonancia gravitomagnética.
* **Visualización en la Esfera de Bloch:** Proyección en 3D de la trayectoria geométrica continua del estado cuántico (precesión nutacional).
* **Fuerza de Stern-Gerlach:** Extracción de la coherencia transversal del espín para modelar la fuerza mecánica oscilatoria inducida por el gradiente de la onda gravitacional.
* **Interactividad:** Implementación de herramientas interactivas (`ipywidgets`) para modificar el *strain* y la frecuencia de la onda en tiempo real.

## Tecnologías y Librerías Utilizadas

El simulador está desarrollado íntegramente en **Python** dentro del entorno de **Jupyter Notebooks**. Las dependencias principales son:

* `numpy`: Operaciones de álgebra lineal, manejo de matrices de Pauli y cálculos tensoriales.
* `scipy.integrate.solve_ivp`: Integrador numérico adaptativo (RK45) con control estricto de tolerancias absolutas y relativas.
* `matplotlib`: Generación de gráficos 2D para las probabilidades y 3D para la Esfera de Bloch.
* `ipywidgets`: Interfaz gráfica interactiva mediante barras deslizables (*sliders*).


## Trabajo Futuro (100% del Proyecto)

Para las etapas finales de la investigación, el simulador se expandirá para incluir:

* **Magnetización Macroscópica:** Escalamiento de la señal cuántica individual a un ensamble termodinámico.
* **Sistemas Abiertos (Decoherencia):** Implementación de la Ecuación de Lindblad para evaluar la supervivencia de la señal frente al ruido térmico del entorno.
* **Fases Geométricas Cuánticas:** Incorporación de un modelo optomecánico para detectar efectos de memoria en el espaciotiempo mediante interferometría de Ramsey y Fases de Berry.

---
**Autor:** Guillermo Reyes  
**Curso:** FIS205 - Universidad Técnica Federico Santa María  
**Profesor:** Ariel Norambuena, Nicolás Viaux  

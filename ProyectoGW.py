import numpy as np 
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp  

#Objetivo 1, resolver la ecuación de Schrödinger dependiente del tiempo para un sistema de dos niveles con un hamiltoniano constante

E_1 = 1.0
E_2 = 1.5
V= 0.0
omega_GWResonante = E_2 - E_1


H0 = np.array([[E_1, V], [V, E_2]], dtype=complex)
psi_0 = np.array([1, 0], dtype=complex)

print("Estado  inicial:", psi_0)
print("Hamiltoniano inicial:\n", H0)

#asumimos h\bar = 1 y demas constantes para simplificar 

def schrodinger(t, psi): 
    dpsi_dt = -1j * np.dot(H0, psi)
    return dpsi_dt

tiempos = np.linspace(0, 40, 100) 

resultados = solve_ivp(schrodinger, [0, 40], psi_0, t_eval = tiempos, rtol = 1e-9, atol = 1e-9)

P_Nivel_1 = np.abs(resultados.y[0])**2
P_Nivel_2 = np.abs(resultados.y[1])**2

P_total = P_Nivel_1 + P_Nivel_2

plt.plot(resultados.t, P_Nivel_1, label='Estado base (Nivel 1)', color = 'blue')

plt.plot(resultados.t, P_Nivel_2, label = 'Estado excitado (Nivel 2)', color = 'green')
plt.plot(resultados.t, P_total, label = "Probabilidad total", linestyle = ':', color = 'gray')

plt.xlabel('Tiempo')
plt.ylabel('Probabilidad')

plt.legend()
plt.title('Evolución temporal de un sistema de dos niveles')

plt.show() 

#Objetivo 2, resolver ahora para un Hamiltoniano dependiente del tiempo

#primero definimos los parametros que nos permitiran simular la perturbacion de la onda gravitacional

omega_GW = 5.0 
Amplitud_GW = 0.05

def schrodinger_GW(t, psi):
    H_t = H0 + Amplitud_GW * np.cos(omega_GWResonante*t) * np.array([[0, 1], [1, 0]], dtype=complex)
    dpsi_dt = -1j * (H_t @ psi)

    return dpsi_dt

resultados_GW = solve_ivp(schrodinger_GW, [0, 40], psi_0, t_eval = tiempos, rtol = 1e-9, atol= 1e-9)

P1GW = np.abs(resultados_GW.y[0])**2
P2GW = np.abs(resultados_GW.y[1])**2
P_total_GW = P1GW + P2GW

plt.plot(resultados_GW.t, P1GW, label='Nivel 1 con perturbación', color = 'red')
plt.plot(resultados_GW.t, P2GW, label='Nivel 2 con perturbación', color = 'orange')

plt.plot(resultados_GW.t, P_total_GW, label='Probabilidad total con perturbación', linestyle = ':', color = 'gray')

plt.xlabel('Tiempo')
plt.ylabel('Probabilidad')
plt.legend()

plt.title('Evolución temporal con perturbación')

plt.show()



#Ahora nos interesa ver como se comporta el sistema, principalmente el segundo nivel para diferentes frecuencias de la onda gravitacional, especialmente cerca de la frecuencia de resonancia

frecuencias_de_prueba = np.linspace(0.1, 3.0, 100)

Probabilidades_maximas = []

print("Calculando para diferentes frecuencias de la onda gravitacional...")

def schrodinger_GW(t, psi, omega):
        H_t = H0 + Amplitud_GW * np.cos(omega*t) * np.array([[0, 1], [1, 0]], dtype=complex)
        dpsi_dt = -1j * (H_t @ psi)

        return dpsi_dt

for omega in frecuencias_de_prueba:
    omega_GW = omega
    
    resultados_loop = solve_ivp(schrodinger_GW, [0, 40], psi_0, t_eval= tiempos,args=(omega_GW,), rtol = 1e-9, atol= 1e-9)

    p2_loop = np.abs(resultados_loop.y[1])**2
    maximo_alcanzado = np.max(p2_loop)
    Probabilidades_maximas.append(maximo_alcanzado)

print("Cálculo completado.")    

plt.figure(figsize=(8, 5))

plt.plot(frecuencias_de_prueba, Probabilidades_maximas, label= 'Probabilidad maxima del nievl 2', color = 'purple', linewidth = 2)
plt.axvline(x=omega_GWResonante, color='red', linestyle='--', label='Frecuencia de resonancia')

plt.xlabel('Frecuencia de la onda gravitacional')
plt.ylabel('Probabilidad máxima del nivel 2')

plt.title('Respuesta del sistema a diferentes frecuencias de la onda gravitacional')

plt.legend()

plt.show()




#Ahora incorporamos el strain de la onda gravitacional, y del acople con la onda 



E_1 = 1.0
E_2 = 1.5
V = 0.0
omega_GWResonante = E_2 - E_1

H0 = np.array([[E_1, V], [V, E_2]], dtype=complex)
psi_0 = np.array([1, 0], dtype=complex)

h_strain = 0.01

kappa = 5.0

Amplitud_GW = kappa * h_strain

psi_0 = np.array([1.0, 0.0], dtype=complex)

print('bloque 1 cargado correctamente')
print(f'amplitud de interaccion calculada: {Amplitud_GW}')

tiempo_simulacion = np.linspace(0, 130, 1000)

def schrodinger_GW_strain(t, psi, omega):
    perturbacion = Amplitud_GW * np.cos(omega*t) * np.array([[0, 1], [1, 0]], dtype=complex)
    H_t = H0 + perturbacion
    dpsi_dt = -1j * (H_t @ psi)
    return dpsi_dt

omega_resonante = np.abs(E_2 - E_1)

print(f'frecuencia de resonancia: {omega_resonante}')

resultados_strain = solve_ivp(schrodinger_GW_strain, [0, 130], psi_0, t_eval=tiempo_simulacion, args=(omega_resonante,), rtol=1e-9, atol=1e-9)

P1_strain = np.abs(resultados_strain.y[0])**2

P2_strain = np.abs(resultados_strain.y[1])**2

P_total_strain = P1_strain + P2_strain 

print('Simulación con strain completada.')  
print(f'Probabilidad máxima del nivel 2 con strain: {np.max(P2_strain):}')
print(f'simulacion de probablididad total: min={np.min(P_total_strain):}, max={np.max(P_total_strain):}')


plt.figure(figsize=(10, 6))

#Ayuda de gemini para hacer graficos un poco mas bonitos...

plt.plot(tiempo_simulacion, P1_strain, label=r'Estado Base $P_1$', color='#1f77b4', linewidth=2)
plt.plot(tiempo_simulacion, P2_strain, label=r'Estado Excitado $P_2$', color='#ff7f0e', linewidth=2)
plt.plot(tiempo_simulacion, P_total_strain, label='Probabilidad Total', color='gray', linestyle='--', linewidth=1.5)


plt.title(r'Dinámica de Transición en Resonancia ($\omega_{GW} = \Delta E$)', fontsize=15, pad=15)
plt.xlabel(r'Tiempo de interacción $t$', fontsize=13)
plt.ylabel(r'Probabilidad de transición $P(t)$', fontsize=13)


plt.grid(True, alpha=0.3)
plt.legend(fontsize=11, loc='center right')
plt.xlim(0, 130)
plt.ylim(0, 1.05) 


plt.tight_layout()
plt.show()



#--- BLOQUE: RELATIVIDAD GENERAL (PAPER RUGGIERO) ---

# 1. Constantes Trabajamos en unidades naturales (se dejan como variables por si se quiere ajustar en un futuro))
c = 1.0
hbar = 1.0

# 2. Parámetros del sistema de dos niveles (nuevamente)
E_1 = 1.0
E_2 = 1.5
H0 = np.array([[E_1, 0], [0, E_2]], dtype=complex)
psi_0 = np.array([1.0, 0.0], dtype=complex)

# 3. Parámetros Del paper de Ruggiero
A_cross = 0.1  # Amplitud del Strain (h_x)
k_0 = 1.0      # Distancia desde el centro del laboratorio (Y^2 + Z^2)^(1/2)


def schrodinger_RG(t, psi, omega):
    # ECUACIÓN 18 del paper
  
    W_cross = (omega**2 / (4 * c)) * A_cross * k_0 * hbar
    
    # ECUACIÓN 17 (Asumimos fase theta=0 para simplificar)
    perturbacion_t = W_cross * np.cos(omega * t)
    H_t = H0 + np.array([[0, perturbacion_t], [perturbacion_t, 0]], dtype=complex)
    
    dpsi_dt = -1j * (H_t @ psi)
    return dpsi_dt

# 5. Simulamos en Resonancia
omega_res = np.abs(E_2 - E_1)
tiempos_RG = np.linspace(0, 50, 1000)

print(f"Calculando evolución con RG exacta (omega = {omega_res})...")

resultados_RG = solve_ivp(
    schrodinger_RG, [0, 50], psi_0, t_eval=tiempos_RG, args=(omega_res,), rtol=1e-9, atol=1e-9)

P2_RG = np.abs(resultados_RG.y[1])**2

plt.figure(figsize=(9, 5))
plt.plot(tiempos_RG, P2_RG, label=r'Probabilidad $P_2$ (Modelo RG)', color='teal', linewidth=2)
plt.title(r'Interacción Espín-GW vía Coordenadas Normales de Fermi', fontsize=14)
plt.xlabel('Tiempo', fontsize=12)
plt.ylabel('Probabilidad de Transición', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()



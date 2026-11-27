def bytes_a_Mbps(Bpm):
    Mbps = ((Bpm * 8) / 60) / 10**6
    return Mbps

def promedio_trafico_tx(fila_interfaz):
    suma = 0
    cantidad = 0
    for fila in fila_interfaz:
        suma += bytes_a_Mbps(fila["bytes_tx"])
        cantidad += 1
    promedio = suma / cantidad
    return promedio

def promedio_trafico_rx(fila_interfaz):
    suma = 0
    cantidad = 0
    for fila in fila_interfaz:
        suma += bytes_a_Mbps(fila["bytes_rx"])
        cantidad += 1
    promedio = suma / cantidad
    return promedio

bytes_por_paquete = 1024

def perdida_paquetes(fila_interfaz):
    porcentaje_perdida = []
    for fila in fila_interfaz:
        perdida = fila["paquetes_descartados"] * bytes_por_paquete
        total_transferencia = fila["bytes_tx"] + fila["bytes_rx"]

        if total_transferencia > 0:
            porcentaje = (perdida * 100) / total_transferencia
        else: 
            porcentaje = 0.0

        porcentaje_perdida.append(round(porcentaje, 2))
    return porcentaje_perdida

def pico_trafico(fila_interfaz):
    pico = 0
    for fila in fila_interfaz:
        tx = bytes_a_Mbps(fila["bytes_tx"])
        rx = bytes_a_Mbps(fila["bytes_rx"])
        mayor = max(tx, rx)
        if mayor > pico:
            pico = mayor
    return pico

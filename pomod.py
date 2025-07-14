import time
from datetime import datetime, timedelta
from plyer import notification

# Configuración del Pomodoro
hora_inicio = datetime.strptime("07:30", "%H:%M").time()
hora_fin = datetime.strptime("16:30", "%H:%M").time()
duracion_estudio = 25 * 60  # 25 minutos en segundos
duracion_descanso = 5 * 60   # 5 minutos en segundos

# Función para mostrar alertas por consola y notificación de escritorio
def alerta(mensaje):
    print("\n" + "="*50)
    print(f"🔔 {mensaje}")
    print("="*50 + "\n")

    # Notificación en escritorio
    notification.notify(
        title="⏰ Pomodoro",
        message=mensaje,
        timeout=10  # segundos
    )

# Verifica si estamos dentro del horario válido
def es_hora_valida():
    ahora = datetime.now().time()
    return hora_inicio <= ahora <= hora_fin

# Espera con contador visual por minutos
def esperar(segundos):
    for restante in range(segundos, 0, -60):
        minutos_restantes = restante // 60
        print(f"🕒 Tiempo restante: {minutos_restantes} min...")
        time.sleep(60)  # Espera 1 minuto

# Ciclo principal Pomodoro
def pomodoro():
    print(f"\n⏳ Iniciando el ciclo Pomodoro a las {datetime.now().strftime('%H:%M:%S')}")
    while True:
        if not es_hora_valida():
            print("\n✅ Jornada finalizada. ¡Buen trabajo!")
            break

        alerta("¡Hora de estudiar por 25 minutos! 💻")
        esperar(duracion_estudio)

        if not es_hora_valida():
            print("\n✅ Jornada finalizada durante el estudio. ¡Buen trabajo!")
            break

        alerta("¡Hora de descansar por 5 minutos! 🛌")
        esperar(duracion_descanso)

# Inicio del script
if __name__ == "__main__":
    try:
        while True:
            ahora = datetime.now().time()
            if ahora >= hora_inicio:
                pomodoro()
                break
            else:
                diferencia = datetime.combine(datetime.today(), hora_inicio) - datetime.now()
                minutos_espera = int(diferencia.total_seconds() // 60)
                print(f"⏳ Esperando al inicio del día Pomodoro a las 7:30 a.m. ({minutos_espera} min restantes)...")
                time.sleep(60)
    except Exception as e:
        print(f"\n🚨 Error inesperado: {e}")
        input("Presiona Enter para cerrar...")



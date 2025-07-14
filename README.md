
# 🕒 Pomodoro App en Python

Una aplicación Pomodoro sencilla y efectiva, desarrollada en Python. Muestra alertas por consola y notificaciones de escritorio. Puede ser convertida a `.exe` para ejecutarse automáticamente en Windows, ideal para mejorar tu productividad diaria.

---

## 🚀 Funcionalidades

- ✅ Temporizador Pomodoro (25 min estudio / 5 min descanso)
- ✅ Notificaciones de escritorio (con `plyer`)
- ✅ Consola visible todo el tiempo
- ✅ Ejecutable `.exe` con ícono personalizado
- ✅ Compatible para ejecutar al iniciar Windows

---

## 🧠 ¿Cómo funciona?

### ⏳ Ciclo Pomodoro
1. Comienza a las 07:30 a.m.
2. Cada ciclo:
   - Muestra un mensaje en consola
   - Muestra una notificación en escritorio
   - Espera 25 minutos (estudio)
   - Notifica descanso y espera 5 minutos
   - Repite mientras la hora esté entre 07:30 a.m. y 04:30 p.m.

### 🔔 Alertas
- La función `alerta()` imprime en consola y lanza una notificación tipo globo usando `plyer`.

### 💤 Antes de la hora de inicio
- Si ejecutas antes de las 07:30 a.m., esperará mostrando los minutos restantes hasta comenzar.

### 🧯 Seguridad
- Captura errores y evita que la consola se cierre inesperadamente.

---

## 🛠 Requisitos

Instala las siguientes dependencias:

```bash
pip install plyer pyinstaller
```

---

## ⚙️ Crear el .exe

1. Asegúrate de tener el ícono `pomo.ico` en la misma carpeta que tu script `pomod.py`.

2. Ejecuta en terminal:

```bash
pyinstaller --onefile --icon=pomo.ico --hidden-import=plyer.platforms.win.notification pomod.py
```

3. Encuentra el ejecutable en la carpeta `dist`.

---

## 🪪 Agregar a inicio automático (Windows)

1. Presiona `Win + R`
2. Escribe `shell:startup` y presiona Enter
3. Coloca un acceso directo al `.exe` dentro de esa carpeta

---

## 🧾 Archivos importantes

- `pomod.py`: Script principal
- `pomo.ico`: Ícono personalizado para el `.exe`
- `README.md`: Este archivo

---

## 🧑‍💻 Autor

Desarrollado por **Cristian Camilo**  


---

## 📈 Ideas futuras

- Sonidos de alerta
- Interfaz gráfica con tkinter
- Estadísticas diarias de tiempo trabajado
- Exportar ciclos a un archivo CSV

---

## 💡 Licencia

Este proyecto es de uso libre y educativo. ¡Mejora tu enfoque y domina tu día con Pomodoro!

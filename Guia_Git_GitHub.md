
# 🧭 GUÍA PRÁCTICA DE GIT + GITHUB PARA DESARROLLADORES Y ANALISTAS

---

## 🔧 1. INSTALAR GIT EN WINDOWS

1. Ve a [https://git-scm.com/download/win](https://git-scm.com/download/win)
2. Descarga e instala Git (deja las opciones por defecto)
3. Verifica que funciona: abre `CMD` o `PowerShell` y escribe:

```bash
git --version
```

---

## 📁 2. CREAR UN REPOSITORIO LOCAL

Supongamos que tienes una carpeta:

```
C:\MisProyectos\PomodoroApp
```

Abre la terminal y ejecuta:

```bash
cd "C:\MisProyectos\PomodoroApp"
git init
```

✅ Esto convierte esa carpeta en un repositorio Git local.

---

## 📥 3. AGREGAR ARCHIVOS AL CONTROL DE VERSIONES

```bash
git add .
```

✅ Agrega todos los archivos del proyecto para ser versionados.

---

## 📝 4. HACER UN COMMIT (Guardar una versión)

```bash
git commit -m "Primera versión del temporizador Pomodoro"
```

✅ Guarda una instantánea del estado actual del proyecto con un mensaje descriptivo.

---

## ☁️ 5. ENLAZAR CON GITHUB

En GitHub:

1. Crea un repositorio nuevo (sin README)
2. Copia la URL HTTPS, por ejemplo:

```bash
https://github.com/GTB0006/PomodoroApp.git
```

Luego en tu terminal:

```bash
git remote add origin https://github.com/GTB0006/PomodoroApp.git
git branch -M main
git push -u origin main
```

---

## 🔁 6. FLUJO DE TRABAJO DIARIO

Cada vez que hagas cambios:

```bash
git add .
git commit -m "Descripción del cambio"
git push
```

---

## 🧠 7. COMANDOS ÚTILES

| Comando         | ¿Qué hace?                              |
|----------------|------------------------------------------|
| `git status`   | Ver qué archivos han cambiado            |
| `git log`      | Ver historial de commits                 |
| `git diff`     | Ver diferencias entre versiones          |
| `git pull`     | Traer cambios desde GitHub               |
| `git clone`    | Clonar un repo remoto en tu PC           |

---

## 🧰 8. IGNORAR ARCHIVOS CON `.gitignore`

Crea un archivo llamado `.gitignore` y coloca dentro:

```
__pycache__/
dist/
*.exe
*.ico
.env
```

---

## 🧩 BONUS: TEMAS AVANZADOS

- **Ramas (`git branch`)**: Trabajar en nuevas versiones
- **Pull Requests**: Colaborar sin pisarse el código
- **CI/CD**: Automatizar pruebas y despliegues

---

## ✅ CONCLUSIÓN

Git + GitHub son esenciales para organizar, respaldar y colaborar en proyectos de desarrollo e integración. Úsalo para tu código en Python, SQL, APIs, automatizaciones y más.

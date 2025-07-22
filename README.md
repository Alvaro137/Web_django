# 🌐 Web Django — Aplicación Didáctica Full Stack

**Proyecto de app web desarrollada con Django y Python (2023)**
Diseñado como práctica completa de desarrollo web: incluye modelo de datos, formularios, procesamiento de archivos, envío de correos y despliegue.

---

## 🧠 Sobre el proyecto

Este proyecto fue desarrollado con fines didácticos para consolidar habilidades en:

* Backend con **Django (Python)**
* Gestión de base de datos con **SQLite**
* Operaciones **CRUD** completas (Create, Read, Update, Delete)
* Subida y procesamiento de archivos
* Automatización de **emails**
* Despliegue en servicios cloud (**Heroku** y **PythonAnywhere**)

> Aunque los despliegues fueron eliminados posteriormente por motivos de coste, el proyecto permanece listo para subir a producción.

---

## ⚙ Cómo instalar

Clona el repositorio:

```bash
git clone https://github.com/Alvaro137/Web_django.git
cd Web_django
```

Crea y activa un entorno virtual:

```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

Instala las dependencias:

```bash
pip install -r requirements.txt
```

Aplica las migraciones:

```bash
python manage.py migrate
```

Lanza el servidor de desarrollo:

```bash
python manage.py runserver
```
